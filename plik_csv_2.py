import csv

filename = 'records.csv'

fields = []
rows = []

with open(filename, 'r') as csv_f:
    csvreader = csv.reader(csv_f, delimiter=',')

    fields = next(csvreader)    # next() - pobierz i ustaw wskaznik na nastepny obiekt
    for row in csvreader:
        rows.append(row)
    print("Liczba odczytanych wierszy", csvreader.line_num)

print(fields)
print(rows)
print(rows[0])
print(rows[0][0])
