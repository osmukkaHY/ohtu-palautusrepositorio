from player import Player, PlayerStats


class DummyPlayerReader:
    def __init__(self, players):
        self.players = players

    def get_players(self):
        return self.players


def make_player(name, nationality, team, goals, assists):
    return Player(
        {
            "name": name,
            "nationality": nationality,
            "team": team,
            "goals": goals,
            "assists": assists,
            "games": 1,
        }
    )


def make_stats():
    players = [
        make_player("A", "FIN", "Tappara", goals=10, assists=5),
        make_player("B", "SWE", "Frölunda", goals=7, assists=10),
        make_player("C", "FIN", "Tappara", goals=12, assists=3),
        make_player("D", "USA", "Frölunda", goals=5, assists=1),
        make_player("E", "FIN", "HIFK", goals=20, assists=0),
    ]
    return PlayerStats(DummyPlayerReader(players))


def test_top_scorers_by_nationality_filters_and_sorts_by_points():
    stats = make_stats()

    result = stats.top_scorers_by_nationality("FIN")

    assert [player.name for player in result] == ["E", "A", "C"]


def test_top_scorers_by_nationality_returns_empty_list_for_unknown_nationality():
    assert make_stats().top_scorers_by_nationality("CAN") == []


def test_top_scorers_by_team_filters_and_sorts_by_points():
    stats = make_stats()

    result = stats.top_scorers_by_team("Tappara")

    assert [player.name for player in result] == ["A", "C"]


def test_top_scorers_by_team_returns_empty_list_for_unknown_team():
    assert make_stats().top_scorers_by_team("Unknown") == []


def test_top_goal_scorers_returns_requested_number_in_descending_goal_order():
    stats = make_stats()

    result = stats.top_goal_scorers(2)

    assert [player.name for player in result] == ["E", "C"]


def test_top_goal_scorers_returns_all_players_when_count_exceeds_team_size():
    stats = make_stats()

    result = stats.top_goal_scorers(10)

    assert [player.name for player in result] == ["E", "C", "A", "B", "D"]


def test_top_goal_scorers_returns_empty_list_for_zero_count():
    assert make_stats().top_goal_scorers(0) == []
