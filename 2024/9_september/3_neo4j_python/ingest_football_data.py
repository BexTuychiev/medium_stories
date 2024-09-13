import os
import json
from neo4j import GraphDatabase
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

NEO4J_URI = os.getenv("NEO4J_CONNECTION_URI")
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

# Connect to Neo4j Aura DB
driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))


def create_league(tx, league_name):
    tx.run("MERGE (l:League {name: $name})", name=league_name)


def create_clubs_and_coaches_batch(tx, clubs, league_name):
    tx.run(
        """
        UNWIND $clubs AS club
        MERGE (c:Club {name: club.name, founded_year: club.founded_year})
        MERGE (l:League {name: $league_name})
        MERGE (c)-[:PLAYS_IN]->(l)
        MERGE (co:Coach {name: club.coach.name, age: club.coach.age})
        MERGE (co)-[:MANAGES]->(c)
        """,
        clubs=clubs,
        league_name=league_name,
    )


def create_players_batch(tx, players, club_name):
    tx.run(
        """
        UNWIND $players AS player
        MERGE (p:Player {name: player.name, age: player.age, position: player.position})
        MERGE (c:Club {name: $club_name})
        MERGE (p)-[:PLAYS_FOR]->(c)
        """,
        players=players,
        club_name=club_name,
    )


def create_matches_batch(tx, matches, league_name):
    tx.run(
        """
        UNWIND $matches AS match
        MERGE (m:Match {date: date(match.date), home_team: match.home_team, away_team: match.away_team, score: match.score})
        SET m.possession_home = match.statistics.possession.home,
            m.possession_away = match.statistics.possession.away,
            m.shots_on_target_home = match.statistics.shots_on_target.home,
            m.shots_on_target_away = match.statistics.shots_on_target.away
        MERGE (l:League {name: $league_name})
        MERGE (m)-[:PART_OF]->(l)
        MERGE (home:Club {name: match.home_team})
        MERGE (away:Club {name: match.away_team})
        MERGE (home)-[:HOME_MATCH]->(m)
        MERGE (away)-[:AWAY_MATCH]->(m)
        """,
        matches=matches,
        league_name=league_name,
    )


def ingest_data():
    with open("football_dataset.json", "r") as file:
        data = json.load(file)

    with driver.session() as session:
        for league in data["leagues"]:
            league_name = league["name"]
            print(f"Processing league: {league_name}")

            # Create League node
            session.execute_write(create_league, league_name)

            # Create Clubs and Coaches (batched)
            print(f"Creating clubs and coaches for {league_name}")
            session.execute_write(
                create_clubs_and_coaches_batch, league["clubs"], league_name
            )

            # Create Players (batched)
            print(f"Creating players for {league_name}")
            for club in league["clubs"]:
                session.execute_write(
                    create_players_batch, club["players"], club["name"]
                )

            # Create Matches (batched)
            print(f"Creating matches for {league_name}")
            session.execute_write(create_matches_batch, league["matches"], league_name)

            print(f"Finished processing {league_name}")


if __name__ == "__main__":
    try:
        print("Starting data ingestion...")
        ingest_data()
        print("Data ingestion completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.close()
