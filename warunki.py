# odp = input("Czy znasz Pythona(t/n)")
# # if - instrukcja sterowania przepływem programu
# if odp.lower() == 't':  # sprawdzenie ==
#     print('Brawo')
# else:
#     print("Idz sie uczyc")
#
# print("Koniec")
# ctrl + /(?) komentarz grupowy

"""
komentarz wielolinijkowy
"""
# # zrobic podatek 65% dla powyzej 100000
# # dla dochodu od 10 do 30 tys podatek 15%
# podatek = 0.0  # float
# zarobki = int(input("Dochod"))  # str na int
# if zarobki < 10000:
#     podatek = 0.05
# elif zarobki < 30000:
#     podatek = 0.15
# elif zarobki < 100000:
#     podatek = 0.4
# else:
#     podatek = 0.65
#
# print(f"Zapłacisz {zarobki * podatek} zł")
#
# suma_zam = 67
# if suma_zam > 100:
#     rabacik = 25
# else:
#     rabacik = 0
#
# print("Rabacik", rabacik)
#
# rabacik = 25 if suma_zam > 100 else 0
# print("Rabacik", rabacik)

lista_bledow = []
alert_system = 'email'
error = 'inny'
error_message = "Stało sie coś strasznego"

# dodac bład 'critical' zeby był dodawany do listy
if alert_system == 'console':
    print(error_message)
elif alert_system == 'email':
    if error == 'medium':
        lista_bledow.append('medium')
    else:
        lista_bledow.append('nieznany')

print(lista_bledow)

odp = input("Podaj date Chrztu Polski")
if odp == '966':
    print("Ok")
else:
    print("Masz w ksiazce na stronie 23")
