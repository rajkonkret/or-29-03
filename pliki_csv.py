import csv

# pliki csv to pliki gdzie dane oddzielone sa znakiem ,;tab itd


fields = ['name', 'surname']
# radek, Kowalski ['RAdek', 'Kowalski']
my_dict = [
    {'name': 'Radek', 'surname': 'Kowalski'},
    {'name': 'Zenek', 'surname': 'Martyniuk'},
    {'name': 'Jarek', 'surname': 'K.'}

]
file = 'records.csv'

with open(file, 'w', newline="") as csv_f:
    csvwriter = csv.DictWriter(csv_f, fieldnames=fields)
    csvwriter.writeheader()
    csvwriter.writerows(my_dict)
