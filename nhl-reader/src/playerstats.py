class PlayerStats:
    def __init__(self, reader) -> None:
        self._reader = reader
    
    def top_scorers_by_nationality(self, nationality):
        players = self._reader.get_players()
        players = [p for p in players if p.nationality=='FIN']
        players.sort(reverse=True, key=lambda p : p.total)
        return players
