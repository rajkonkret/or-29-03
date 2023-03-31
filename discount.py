from datetime import date, timedelta, datetime

today = date.today()
time = datetime.now()
print(today)
print(time)
print(today.year)
print(today.timetuple())
tomorrow = today + timedelta(days=1)
print(tomorrow)
products = [
    {'sku': '1', 'exp_date': today, 'price': 100.0},
    {'sku': '2', 'exp_date': tomorrow, 'price': 50.0},
    {'sku': '3', 'exp_date': today, 'price': 20.0}
]

for product in products:
    if product['exp_date'] != today:
        continue        # zakoncz w tym miejscu i wroc na poczatek petli
    product['price'] *= 0.8  # p = p * 0.8
    print(f"""
    Price for sku= {product['sku']}
    is now {product['price']}
""")
