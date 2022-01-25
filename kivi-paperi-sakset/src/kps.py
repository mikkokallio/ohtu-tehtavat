from tuomari import Tuomari
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu


class KPS:
    def __init__(self) -> None:
        self._tuomari = Tuomari()
    
    @staticmethod
    def luo_ihmisten_peli():
        return KPSPelaajaVsPelaaja()

    @staticmethod
    def luo_peli_tekoalya_vastaan():
        return KPSTekoaly()

    @staticmethod
    def luo_peli_parempaa_tekoalya_vastaan():
        return KPSParempiTekoaly()

    def pelaa(self):
        while True:
            ekan_siirto = self._ensimmaisen_siirto()
            tokan_siirto = self._toisen_siirto(ekan_siirto)
            
            if not self._onko_ok_siirto(ekan_siirto) or not self._onko_ok_siirto(tokan_siirto):
                break

            self._tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(self._tuomari)

        print("Kiitos!")
        print(self._tuomari)

    def _ensimmaisen_siirto(self):
      return input("Ensimmäisen pelaajan siirto: ")

    # tämän metodin toteutus vaihtelee eri pelityypeissä
    def _toisen_siirto(self, ensimmaisen_siirto):
        # metodin oletustoteutus
        return "k"

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"


class KPSPelaajaVsPelaaja(KPS):
    def __init__(self) -> None:
        super().__init__()

    def _toisen_siirto(self, ekan_siirto):
        return input("Toisen pelaajan siirto: ")


class KPSTekoaly(KPS):
    def __init__(self) -> None:
        super().__init__()
        self._tekoaly = Tekoaly()

    def _toisen_siirto(self, ekan_siirto):
        tokan_siirto = self._tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        return tokan_siirto


class KPSParempiTekoaly(KPS):
    def __init__(self) -> None:
        super().__init__()
        self._tekoaly = TekoalyParannettu(10)

    def _toisen_siirto(self, ekan_siirto):
        tokan_siirto = self._tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        self._tekoaly.aseta_siirto(ekan_siirto)
        return tokan_siirto
