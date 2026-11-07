import requests



class Player:
    def __init__(self, data):
        self.name = data['name']
        self.nationality = data['nationality']
        self.assists = data['assists']
        self.goals = data['goals']
        self.team = data['team']
        self.games = data['games']
        self.points = self.assists + self.goals

    def print_foo(self):
        print("foo")

    def __str__(self):
        return f"Name: {self.name} Team: {self.team} Goals: {self.goals} Assists: {self.assists} Points: {self.points}"


class PlayerReader:
    def __init__(self, url: str) -> None:
        self.url = url

    def get_players(self) -> list[Player]:
        res = requests.get(self.url, timeout=30).json()
        players = []
        for player_dict in res:
            player = Player(player_dict)
            players.append(player)
        return players

    def print_foo(self):
        print("foo")


class PlayerStats:
    def __init__(self, reader: PlayerReader) -> None:
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nat: str) -> list[Player]:
        filtered = list(filter(lambda p: p.nationality == nat, self.players))
        return sorted(filtered, key=lambda p: -p.points)

    def top_scorers_by_team(self, team: str) -> list[Player]:
        filtered = list(filter(lambda p: p.team == team, self.players))
        return sorted(filtered, key=lambda p: -p.points)

    def print_foo(self):
        print("foo")

    def top_goal_scorers(self, count: int) -> list[Player]:
        """Returns <count> players with the most goals in descending order"""
        return sorted(self.players, key=lambda p: -p.goals)[:count]
