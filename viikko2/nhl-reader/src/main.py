import requests
from rich.console import Console
from rich.table import Table

from player import Player, PlayerReader, PlayerStats

def main():
    console = Console()
    reader = PlayerReader("https://studies.cs.helsinki.fi/nhlstats/2024-25/players")
    stats = PlayerStats(reader)
    nationalities = sorted(list(set([p.nationality for p in reader.get_players()])))
    print(nationalities)

    while True:
        nat = console.input(f"Enter nationality{'/'.join(nationalities)}")
        players = stats.top_scorers_by_nationality(nat)
        table = Table(title=f"players from {nat}")
        table.add_column("Name")
        table.add_column("Teams")
        table.add_column("Goals")
        table.add_column("Assists")
        table.add_column("Points")

        for p in players:
            table.add_row(p.name, p.team, str(p.goals), str(p.assists), str(p.points))
        console.print(table)


if __name__ == "__main__":
    main()

