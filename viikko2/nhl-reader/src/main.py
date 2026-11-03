import requests
from player import Player, PlayerReader, PlayerStats

def main():
    reader = PlayerReader("https://studies.cs.helsinki.fi/nhlstats/2024-25/players")
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)


if __name__ == "__main__":
    main()

