import tkinter as tk


class Kalkulator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.wynik = tk.StringVar()

        self._stworz_interfejs()

    def _stworz_interfejs(self):
        self.title("Kalkulator")
        self.geometry("250x200")

        # Pole tekstowe do wyświetlania wyniku
        pole_tekstowe = tk.Entry(self, textvariable=self.wynik, justify='right')
        pole_tekstowe.grid(row=0, column=0, columnspan=4)

        # Przyciski
        przyciski = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
        ]

        for (tekst, rzad, kolumna) in przyciski:
            przycisk = tk.Button(self, text=tekst, command=lambda t=tekst: self._przycisk_nacisniety(t))
            przycisk.grid(row=rzad, column=kolumna, sticky="nsew")

        # Dopasowanie rozmiaru przycisków do okna
        for i in range(5):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)

    def _przycisk_nacisniety(self, tekst):
        if tekst == '=':
            try:
                wynik = eval(self.wynik.get())
                self.wynik.set(wynik)
            except Exception:
                self.wynik.set("Błąd")
        elif tekst == 'C':
            self.wynik.set("")
        else:
            self.wynik.set(self.wynik.get() + tekst)


if __name__ == "__main__":
    app = Kalkulator()
    app.mainloop()
