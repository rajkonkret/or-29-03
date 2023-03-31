from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    Klasa opisujaca ptaka w Pythonie
    """

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def lataj(self):
        print("Tu", self.gatunek, "lece z szybkoscia", self.szybkosc)

    @abstractmethod
    def wydaj_odglos(self):
        pass


class Orzel(Ptak):
    """
    To jest orzeł
    """

    def poluj(self):
        print("Tu", self.gatunek, " Rozpoczynam polowanie")

    def wydaj_odglos(self):
        print("piiiiiiiiiiiii")


class Kura(Ptak):
    """
    To jest kura
    """

    def __init__(self, gatunek):
        super().__init__(gatunek, 0)  # uzycie konstruktora z klasy nadrzędnej
        self.gatunek = gatunek

    def lataj(self):
        print("Tu", self.gatunek, "Ja nie latam")

    def dziobanie(self):
        print("Tu", self.gatunek, "Ide sobie podziobać")

    def wydaj_odglos(self):
        print("kookokokokoko")


# 13:30

# orzel = Ptak("orzel", 2)
# print(orzel.gatunek)
or_2 = Orzel("orzel", 10)
print(or_2.szybkosc)
or_2.poluj()
or_2.wydaj_odglos()
# kura = Ptak("kura", 0)
# kura.lataj()
kura_2 = Kura("kura")
kura_2.lataj()
kura_2.dziobanie()
kura_2.wydaj_odglos()
