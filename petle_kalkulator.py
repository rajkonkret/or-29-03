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
    a = int(input("Podaj pierwsza liczbe"))
    b = int(input("Podaj druga liczbe"))
    if odp == "1":
        print(f"Wynik działania {a} + {b} = {a + b}")
        # wynik działania 5 + 4 = 9
    elif odp == "2":
        print(f"Wynik działania {a} - {b} = {a - b}")
    elif odp == "3":
        print(f"Wynik działania {a} * {b} = {a * b}")
    elif odp == "4":
        if b != 0:
            print(f"Wynik działania {a} / {b} = {a / b}")
        else:
            print("nie dzielimy przez zero")
    else:
        print("Nie znam takiego działania")
