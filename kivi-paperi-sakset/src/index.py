from kps import KPS

pelit = {
    'a': {'kuvaus': 'Ihmistä vastaan', 'peli': KPS.luo_ihmisten_peli},
    'b': {'kuvaus': 'Tekoälyä vastaan', 'peli': KPS.luo_peli_tekoalya_vastaan},
    'c': {'kuvaus': 'Parannettua tekoälyä vastaan', 'peli': KPS.luo_peli_parempaa_tekoalya_vastaan},
}

def main():
    while True:
        print("Valitse pelataanko")
        [print(f" ({peli}) {pelit[peli]['kuvaus']}") for peli in pelit]
        print("Muilla valinnoilla lopetetaan")

        vastaus = input()
        
        if len(vastaus) > 0 and vastaus[-1] in pelit:
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )
            peli = pelit[vastaus[-1]]['peli']()
            peli.pelaa()
        else:
            break 

if __name__ == "__main__":
    main()
