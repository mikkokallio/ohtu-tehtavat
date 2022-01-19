RELATIVE_SCORES = ["Deuce", "Advantage ", "Win for "]
INDIVIDUAL_SCORES = ["Love", "Fifteen", "Thirty", "Forty"]


class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.scores = {player1_name: 0, player2_name: 0}

    def won_point(self, player_name):
        if player_name in self.scores:
            self.scores[player_name] += 1

    def get_score(self):
        a, b = [self.scores[player] for player in self.scores]
        if max(a, b) > 3:
            leading_player = "" if a==b else max(self.scores, key=self.scores.get)
            difference = min(abs(a-b), 2)
            return f"{RELATIVE_SCORES[difference]}{leading_player}"
        elif a == b:
            return f"{INDIVIDUAL_SCORES[a]}-All"
        else:
            return f"{INDIVIDUAL_SCORES[a]}-{INDIVIDUAL_SCORES[b]}"
