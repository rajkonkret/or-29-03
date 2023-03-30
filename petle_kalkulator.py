while True:
    print("""
    1. Dodawanie
    2. Odejmowanie
    3. Mnożenie
    4. DZielenie
    5. Koniec
    """)
    odp = input("Podaj dzialanie")
    if odp == "5":
        break
    try:
        a = int(input("Podaj pierwsza liczbe"))
        b = int(input("Podaj druga liczbe"))
    except TypeError:
        print("Błąd typu")
        continue
    if odp == "1":
        print(f"Wynik działania {a} + {b} = {a + b}")
        # wynik działania 5 + 4 = 9
    elif odp == "2":
        print(f"Wynik działania {a} - {b} = {a - b}")
    elif odp == "3":
        print(f"Wynik działania {a} * {b} = {a * b}")
    elif odp == "4":
        try:
            print(f"Wynik działania {a} / {b} = {a / b}")
        except ZeroDivisionError:
            print("Dzielenie przez zero")
    else:
        print("Nie znam takiego działania")
