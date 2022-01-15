import unittest
from statistics import Statistics
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.stat = Statistics(
            PlayerReaderStub()
        )

    # ...

    def test_search_returns_player(self):
        player = self.stat.search("Seme")
        self.assertEqual(player.name, "Semenko")

    def test_search_nonexistent_returns_none(self):
        player = self.stat.search("Jorma")
        self.assertEqual(player, None)

    def test_team_returns_players(self):
        team = self.stat.team("EDM")
        self.assertEqual(len(team), 3)

    def test_top_scorers_returns(self):
        scorers = self.stat.top_scorers(3)
        self.assertEqual(scorers[-1].name, "Kurri")
