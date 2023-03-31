import tkinter


class MyGui:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Dodawanie")
        self.main_window.geometry("250x250")
        self.label1 = tkinter.Entry(self.main_window, width=10)
        self.label2 = tkinter.Entry(self.main_window, width=10)
        self.calc_button = tkinter.Button(self.main_window, text="Oblicz", command=self.oblicz)

        self.value = tkinter.StringVar()
        self.result = tkinter.Label(self.main_window, textvariable=self.value)

        self.label1.pack(side='left')
        self.label2.pack(side='left')
        self.calc_button.pack(side='bottom')
        self.result.pack(side='bottom')
        tkinter.mainloop()

    def oblicz(self):
        a = self.label1.get()
        b = self.label2.get()
        self.value.set(int(a) + int(b))


my_gui = MyGui()
