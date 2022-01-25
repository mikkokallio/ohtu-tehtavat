from kps import KPS


class KPSPelaajaVsPelaaja(KPS):
    def __init__(self) -> None:
        super().__init__()

    def _toisen_siirto(self, ekan_siirto):
        return input("Toisen pelaajan siirto: ")
