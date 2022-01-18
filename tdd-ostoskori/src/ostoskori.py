from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._ostokset = {}
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

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
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return list(self._ostokset.values())
