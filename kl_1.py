# klasa - szablon

class Human:
    """
    To jest klasa Humn opisującego człowieka w klasie
    """
    imie = ""
    wiek = None
    wzrost = None
    plec = 'k'

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


cz_1 = Human()  # tworzenie obiektu klasy Human
print(Human.__doc__)
print(cz_1)
print(cz_1.plec)
cz_1.imie = "Radek"
cz_1.wiek = 50
cz_1.wzrost = 174
cz_1.plec = 'm'
print(cz_1.wzrost)
cz_1.powitanie()
cz_1.ruszaj()
cz_2 = Human()
cz_2.plec = 'k'
cz_2.ruszaj()
