while True:
    print("""
    1. Dodawanie
    2. Odejmowanie
    5. Koniec
    """)
    odp = input("Podaj dzialanie")
    if odp == "5":
        break
    a = int(input("Podaj pierwsza liczbe"))
    b = int(input("Podaj druga liczbe"))
    if odp == "1":
        print(a + b)
        # wynik działania 5 + 4 = 9
    else:
        print("Nie znam takiego działąnia")