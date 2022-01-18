KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        self._kasvatuskoko = self._validoi(kasvatuskoko)
        self._alkiot = [0] * self._validoi(kapasiteetti)
        self._mahtavuus = 0

    def _validoi(self, arvo):
        if not isinstance(arvo, int) or arvo < 0:
            raise ValueError(f"Arvo '{arvo}' ei ole positiivinen kokonaisluku")
        return arvo
        
    def kuuluu(self, n):
        return n in self._alkiot[:self._mahtavuus]

    def lisaa(self, n):
        if not self.kuuluu(n):
            self._alkiot[self._mahtavuus] = n
            self._mahtavuus += 1

            if self._mahtavuus % len(self._alkiot) == 0:
                self._alkiot.extend([0] * self._kasvatuskoko)

            return True
        else:
            return False

    def poista(self, n):
        if n != 0 and n in self._alkiot[:self._mahtavuus]:
            self._alkiot.remove(n)
            self._mahtavuus -= 1
            return True
        else:
            return False

    def mahtavuus(self):
        return self._mahtavuus

    def to_int_list(self):
        return self._alkiot[:self._mahtavuus]

    @staticmethod
    def yhdiste(a, b):
        yhdiste = IntJoukko()
        [yhdiste.lisaa(n) for n in a.to_int_list() + b.to_int_list()]    
        return yhdiste

    @staticmethod
    def leikkaus(a, b):
        leikkaus = IntJoukko()
        [leikkaus.lisaa(n) for n in set(a.to_int_list()).intersection(set(b.to_int_list()))]    
        return leikkaus

    @staticmethod
    def erotus(a, b):
        erotus = IntJoukko()
        [erotus.lisaa(n) for n in set(a.to_int_list()).difference(set(b.to_int_list()))]    
        return erotus

    def __str__(self):
        return str(set(self._alkiot[:self._mahtavuus])) if self._mahtavuus > 0 else "{}"
