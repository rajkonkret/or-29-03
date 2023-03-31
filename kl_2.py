class Human:

    # własny konstruktor klasy
    def __init__(self, imie, wiek, plec='k'):
        self.imie = imie
        self.wiek = wiek
        self.plec = plec

    def powitanie(self):
        """
        metoda witajaca
        :return: None
        """
        print("Nazywam sie", self.imie)

    def ruszaj(self):
        if self.plec == 'm':
            print("Ruszyłem w droge")
        else:
            print("Ruszyłam w droge")


cz_1 = Human("Radek", 39, "m")
print(cz_1.imie)
cz_1.powitanie()
cz_1.ruszaj()
