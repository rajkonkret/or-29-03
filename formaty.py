user = "Radek"
wiek = 39
wersja = 3.90001
liczba = 134562344532

print(type(liczba))

print("Witaj %s masz teraz %d lat" % (user, wiek))
# %s - string, %d digit
print("Witaj %(user)s masz teraz %(age)d lat" % {'user': user, "age": wiek})
print(f'Witaj {user} masz teraz {wiek} lat')

print("Używamy wersji Python %i" % 3)
print("Używamy wersji Python %f" % 3.9)
print("Używamy wersji Python %.1f" % 3.9)
print("Używamy wersji Python %.f" % 3.9)  # bez czesci ułamkowej, zaokrągla
print("Uzywamy wersji Python {}".format(wersja))
print(f"Uzywamy wersji Python {wersja:.1f}")
print(f"Uzywamy wersji Python {wersja:.2f}")

print(f"{user:>10}")
print(f"{user:>20}")
print(f"{user:<20}")
print("Nasza duza liczba {:,}".format(liczba).replace(',', '.'))
print("Nasza duza liczba {:,}".format(liczba).replace(',', ' '))
print("Nasza duza liczba {:,}".format(liczba))

print(f"""
{user:>10}
""")
# 11:10
