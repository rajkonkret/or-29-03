class Dom:
    """
    To jest klasa opisujaca dom
    """

    def __init__(self, metraz, kolor, liczba_okien):
        self.__metraz = metraz  # __ pole prywatne
        self.kolor = kolor
        self.liczba_okien = liczba_okien

    def wypisz_metraz(self):
        print("Metraż wynosi", self.__metraz)

    def zmien_metraz(self):
        wybor = int(input("Podaj metraz"))
        self.__metraz = wybor
        print("Metraz wynosi", self.__metraz)

    def zmien_kolor(self):
        wybor = input("Podaj kolor")
        self.kolor = wybor
        print("Metraz wynosi", self.kolor)
        self.__farba()

    def zmien_liczbe_okien(self):
        wybor = int(input("Podaj liczbe_okien"))
        self.liczba_okien = wybor
        print("Liczba okien wynosi", self.liczba_okien)

    def __farba(self):
        print("Skonczyłą sie farba")


dom_1 = Dom(123, "czerwony", 6)
print(dom_1.kolor)
dom_1.kolor = "żółty"
dom_1.wypisz_metraz()
dom_1.zmien_metraz()
dom_1.wypisz_metraz()
dom_1.zmien_kolor()
