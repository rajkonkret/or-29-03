# ZeroDivisionError
try:
    print(2 / 1)
except ZeroDivisionError:
    print("Dzielenie przez zero")
except TypeError:
    print("Błąd typu")
except Exception as e:
    print(e)
else:
    print("Nie ma")
finally:        # wykonuje sie zawsze
    print("Zawsze")

print("Program działa dalej")
