# 15:00
kurs_eur = 4.69
kurs_usd = 4.35


def kantor(waluta):
    print("Uruchomienie kantoru")

    def usd(kwota):
        print(f"Przeliczam dolary kurs: {kurs_usd}, kwota {kwota}, dostajesz {kurs_usd * kwota}")

    def eur(kwota):
        print(f"Przeliczam euro kurs: {kurs_eur}, kwota {kwota}, dostajesz {kurs_eur * kwota}")

    if waluta.upper() == "EUR":
        return eur
    else:
        return usd


# kurs dolara, naprawic funkcje wymiany dolarów
# pobrac od uzytkownika walute i kwote i wg tego przeliczyc
waluta = input("Podaj walute(usd/eur)")
kwota = int(input("Podaj kwote"))
moj_kantor = kantor(waluta)
moj_kantor(kwota)
