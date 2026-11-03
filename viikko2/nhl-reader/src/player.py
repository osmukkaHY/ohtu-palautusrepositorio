import requests



class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.team = dict['team']
        self.games = dict['games']
        self.id = dict['id']
        self.points = self.assists + self.goals
    
    def __str__(self):
        return f"Name: {self.name} Team: {self.team} Goals: {self.goals} Assists: {self.assists} Points: {self.points}"


class PlayerReader:
    def __init__(self, url: str) -> None:
        self.url = url

    def get_players(self) -> list[Player]:
        res = requests.get(self.url).json()
        players = []
        for player_dict in res:
            player = Player(player_dict)
            players.append(player)
        return players


class PlayerStats:
    def __init__(self, reader: PlayerReader) -> None:
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nat: str) -> list[Player]:
        filtered = list(filter(lambda p: p.nationality == nat, self.players))
        return sorted(filtered, key=lambda p: -p.points)

