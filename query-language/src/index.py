from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, All, HasAtLeast, HasFewerThan, Not, Or, PlaysIn

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher = And(
        HasFewerThan(5, "goals"),
        PlaysIn("EDM")
    )

    matcher = And(
        Not(HasAtLeast(1, "goals")),
        PlaysIn("NYR")
    )
    
    matcher = And(
        HasFewerThan(1, "goals"),
        PlaysIn("NYR")
    )

    matcher = All()
    
    matcher = Or(
        HasAtLeast(30, "goals"),
        HasAtLeast(50, "assists")
    )

    matcher = And(
        HasAtLeast(40, "points"),
        Or(
            PlaysIn("NYR"),
            PlaysIn("NYI"),
            PlaysIn("BOS")
        )
    )

    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
