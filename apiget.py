import requests as re

# pip install requests

# http://api.nbp.pl/api/exchangerates/rates/{table}/{code}/

response = re.get("http://api.nbp.pl/api/exchangerates/rates/A/EUR/")
print(response)
# 2.. poprawne
# 4.. błedy np błedne dane wysłane
# 5.. wewnetrne błedy serwera
table = response.json()
print(table)
print(table['rates'][0]['mid'])