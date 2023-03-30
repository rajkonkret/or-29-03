# ZeroDivisionError
try:
    print(2 / "a")
except ZeroDivisionError:
    print("Dzielenie przez zero")
except TypeError:
    print("Błąd typu")
except Exception as e:
    print(e)

print("Program działa dalej")
