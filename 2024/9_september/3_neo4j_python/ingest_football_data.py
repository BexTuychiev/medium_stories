import pandas as pd
import neo4j
from dotenv import load_dotenv
import os
from tqdm import tqdm
import logging

# CSV file paths
results_csv_path = "https://raw.githubusercontent.com/martj42/international_results/refs/heads/master/results.csv"
goalscorers_csv_path = "https://raw.githubusercontent.com/martj42/international_results/refs/heads/master/goalscorers.csv"
shootouts_csv_path = "https://raw.githubusercontent.com/martj42/international_results/refs/heads/master/shootouts.csv"

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Loading data...")

# Load data
results_df = pd.read_csv(results_csv_path, parse_dates=["date"])
goalscorers_df = pd.read_csv(goalscorers_csv_path, parse_dates=["date"])
shootouts_df = pd.read_csv(shootouts_csv_path, parse_dates=["date"])

# Set up Neo4j connection
load_dotenv()

uri = os.getenv("NEO4J_URI")
user = os.getenv("NEO4J_USERNAME")
password = os.getenv("NEO4J_PASSWORD")

try:
    driver = neo4j.GraphDatabase.driver(uri, auth=(user, password))
    print("Connected to Neo4j instance successfully!")
except Exception as e:
    print(f"Failed to connect to Neo4j: {e}")


BATCH_SIZE = 5000


def create_indexes(session):
    indexes = [
        "CREATE INDEX IF NOT EXISTS FOR (t:Team) ON (t.name)",
        "CREATE INDEX IF NOT EXISTS FOR (m:Match) ON (m.id)",
        "CREATE INDEX IF NOT EXISTS FOR (p:Player) ON (p.name)",
        "CREATE INDEX IF NOT EXISTS FOR (t:Tournament) ON (t.name)",
        "CREATE INDEX IF NOT EXISTS FOR (c:City) ON (c.name)",
        "CREATE INDEX IF NOT EXISTS FOR (c:Country) ON (c.name)",
    ]
    for index in indexes:
        session.run(index)
    print("Indexes created.")


def ingest_matches(session, df):
    query = """
    UNWIND $batch AS row
    MERGE (m:Match {id: row.id})
    SET m.date = date(row.date), m.home_score = row.home_score, m.away_score = row.away_score, m.neutral = row.neutral
    MERGE (home:Team {name: row.home_team})
    MERGE (away:Team {name: row.away_team})
    MERGE (t:Tournament {name: row.tournament})
    MERGE (c:City {name: row.city})
    MERGE (country:Country {name: row.country})
    MERGE (home)-[:PLAYED_HOME]->(m)
    MERGE (away)-[:PLAYED_AWAY]->(m)
    MERGE (m)-[:PART_OF]->(t)
    MERGE (m)-[:PLAYED_IN]->(c)
    MERGE (c)-[:LOCATED_IN]->(country)
    WITH m, home, away, row.home_score AS hs, row.away_score AS as
    FOREACH(_ IN CASE WHEN hs > as THEN [1] ELSE [] END |
        MERGE (home)-[:WON]->(m)
        MERGE (away)-[:LOST]->(m)
    )
    FOREACH(_ IN CASE WHEN hs < as THEN [1] ELSE [] END |
        MERGE (away)-[:WON]->(m)
        MERGE (home)-[:LOST]->(m)
    )
    FOREACH(_ IN CASE WHEN hs = as THEN [1] ELSE [] END |
        MERGE (home)-[:DREW]->(m)
        MERGE (away)-[:DREW]->(m)
    )
    """
    for i in tqdm(range(0, len(df), BATCH_SIZE), desc="Ingesting matches"):
        batch = df.iloc[i : i + BATCH_SIZE]
        data = []
        for _, row in batch.iterrows():
            match_data = {
                "id": f"{row['date']}_{row['home_team']}_{row['away_team']}",
                "date": row["date"].strftime("%Y-%m-%d"),
                "home_score": int(row["home_score"]),
                "away_score": int(row["away_score"]),
                "neutral": bool(row["neutral"]),
                "home_team": row["home_team"],
                "away_team": row["away_team"],
                "tournament": row["tournament"],
                "city": row["city"],
                "country": row["country"],
            }
            data.append(match_data)
        session.run(query, batch=data)


def ingest_goals(session, df):
    query = """
    UNWIND $batch AS row
    MATCH (m:Match {id: row.id})
    MERGE (p:Player {name: row.scorer})
    MERGE (t:Team {name: row.team})
    CREATE (p)-[s:SCORED_FOR]->(t)
    SET s.own_goal = row.own_goal,
        s.penalty = row.penalty
    FOREACH(_ IN CASE WHEN row.minute IS NOT NULL THEN [1] ELSE [] END |
        SET s.minute = row.minute
    )
    CREATE (p)-[r:SCORED_IN]->(m)
    SET r.own_goal = row.own_goal,
        r.penalty = row.penalty
    FOREACH(_ IN CASE WHEN row.minute IS NOT NULL THEN [1] ELSE [] END |
        SET r.minute = row.minute
    )
    """
    for i in tqdm(range(0, len(df), BATCH_SIZE), desc="Ingesting goals"):
        batch = df.iloc[i : i + BATCH_SIZE]
        data = []
        for _, row in batch.iterrows():
            try:
                goal_data = {
                    "id": f"{row['date']}_{row['home_team']}_{row['away_team']}",
                    "scorer": (
                        row["scorer"]
                        if not pd.isna(row["scorer"])
                        else "Unnamed Player"
                    ),
                    "team": row["team"],
                    "minute": (
                        float(row["minute"]) if pd.notnull(row["minute"]) else None
                    ),
                    "own_goal": bool(row["own_goal"]),
                    "penalty": bool(row["penalty"]),
                }
                data.append(goal_data)
            except Exception as e:
                logger.error(f"Error processing row: {row}")
                logger.error(f"Error details: {str(e)}")

        if data:
            try:
                session.run(query, batch=data)
            except Exception as e:
                logger.error(f"Error executing batch: {str(e)}")
                logger.error(f"Problematic batch: {data}")


def ingest_shootouts(session, df):
    query = """
    UNWIND $batch AS row
    MATCH (m:Match {id: row.id})
    MATCH (w:Team {name: row.winner})
    MERGE (m)-[s:HAD_SHOOTOUT]->(w)
    SET s.winner = row.winner
    FOREACH(_ IN CASE WHEN row.first_shooter IS NOT NULL THEN [1] ELSE [] END |
        SET s.first_shooter = row.first_shooter
    )
    """
    for i in tqdm(range(0, len(df), BATCH_SIZE), desc="Ingesting shootouts"):
        batch = df.iloc[i : i + BATCH_SIZE]
        data = []
        for _, row in batch.iterrows():
            shootout_data = {
                "id": f"{row['date']}_{row['home_team']}_{row['away_team']}",
                "winner": row["winner"],
                "first_shooter": (
                    row["first_shooter"] if pd.notnull(row["first_shooter"]) else None
                ),
            }
            data.append(shootout_data)
        session.run(query, batch=data)


def main():
    with driver.session() as session:
        create_indexes(session)
        ingest_matches(session, results_df)
        ingest_goals(session, goalscorers_df)
        ingest_shootouts(session, shootouts_df)

    print("Data ingestion completed!")
    driver.close()


if __name__ == "__main__":
    main()
