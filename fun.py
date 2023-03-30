# funkcje - kawałek kodu, ktory chcemy wykonywac wielokrotnie
a = 6
b = 7


# defiicja funkcji - oznacz, ze tu kod sie nie wykona
def dodaj():
    print(a + b)


def dodaj_2(a, b):  # dwaa wymagane argumenty a,b
    print(a + b)


def odejmij(a, b, c=0):  # c ma domyslna wartosc
    print(a - b - c)


def mnozenie(a, b):
    print(a * b)


def dzielenie(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("Dzielenie przez zero")


dzielenie(2, 3)
dzielenie(2, 0)
dodaj()  # wywołanie funkcji, tu sie wykona
dodaj_2(2, 3)
odejmij(5, 4, 2)
odejmij(5, 4)
mnozenie(3, 4)
mnozenie(b=5, a=7)  # argumenty po nazwie, nie musimy zachowywac kolejnosci
print(dodaj())      # zwraca None - czyli nic
