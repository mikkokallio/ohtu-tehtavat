from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._ostokset = {}

    def tavaroita_korissa(self):
        return sum([o.lukumaara() for o in self._ostokset.values()])

    def hinta(self):
        return sum([o.hinta() for o in self._ostokset.values()])

    def lisaa_tuote(self, lisattava: Tuote):
        if lisattava not in self._ostokset:
            self._ostokset[lisattava] = Ostos(lisattava)
        else:
            self._ostokset[lisattava].muuta_lukumaaraa(1)

    def poista_tuote(self, poistettava: Tuote):
        if poistettava in self._ostokset:
            self._ostokset[poistettava].muuta_lukumaaraa(-1)
            if self._ostokset[poistettava].lukumaara() == 0:
                del self._ostokset[poistettava]

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return list(self._ostokset.values())
