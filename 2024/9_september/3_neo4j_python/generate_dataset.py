import json
import random
from faker import Faker

fake = Faker()


def generate_players(club_name):
    positions = ["Forward", "Midfielder", "Defender", "Goalkeeper"]
    players = []
    for _ in range(20):
        player = {
            "name": fake.name(),
            "age": random.randint(18, 35),
            "position": random.choice(positions),
        }
        players.append(player)
    return players


def generate_clubs(league_name):
    clubs = []
    for _ in range(20):
        club_name = f"{fake.city()} FC"
        club = {
            "name": club_name,
            "founded_year": random.randint(1880, 2000),
            "coach": {"name": fake.name(), "age": random.randint(40, 65)},
            "players": generate_players(club_name),
        }
        clubs.append(club)
    return clubs


def generate_matches(clubs):
    matches = []
    club_names = [club["name"] for club in clubs]
    for _ in range(38):
        home_team, away_team = random.sample(club_names, 2)
        match = {
            "date": fake.date_between(start_date="-1y", end_date="today").isoformat(),
            "score": f"{random.randint(0, 5)}-{random.randint(0, 5)}",
            "home_team": home_team,
            "away_team": away_team,
            "statistics": {
                "possession": {
                    "home": random.randint(40, 60),
                    "away": random.randint(40, 60),
                },
                "shots_on_target": {
                    "home": random.randint(0, 10),
                    "away": random.randint(0, 10),
                },
                # ... other match statistics
            },
        }
        matches.append(match)
    return matches


def generate_league(name):
    clubs = generate_clubs(name)
    league = {"name": name, "clubs": clubs, "matches": generate_matches(clubs)}
    return league


def main():
    leagues = []
    for league_name in ["La Liga", "Premier League", "Bundesliga"]:
        league = generate_league(league_name)
        leagues.append(league)
    dataset = {"leagues": leagues}
    with open("data/football_dataset.json", "w") as f:
        json.dump(dataset, f, indent=2)


if __name__ == "__main__":
    main()
