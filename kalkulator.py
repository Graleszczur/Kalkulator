from tkinter import *
from math import sqrt

class kalkulator:

    def __init__(self,master):

        master.title("Fantastyczny kalkulator i jak go znaleźć")
        master.geometry()
        master.config(background='gray35')
        label_entry_text = Label(master, fg='white', bg='gray35', text="Potężne narzedzie do\noperacji matematycznych\n"
                                                                       "(zastępca Matlaba)", font=("Arial", 14, "bold"),
                                 height=4)
        label_entry_text.grid(row=0, column=0, columnspan=4)
        self.entry_window=Entry(master, fg='white', width=9, bd=4, bg='gray35', justify=RIGHT, font=("Arial", 40))
        self.entry_window.grid(row=1, column=0, columnspan=4)
        self.entry_window.focus_set()
        label_memoryb = Label(master, fg='white', bg='gray35',
                              text="\nTe przyciski to nawet nie przyciski(tylko tekst xD)\n"
                                     "MC    |      MR     |     M+     |     M-     |     MS     |      M^",
                              font=("Arial", 8, "bold"), height=3)
        label_memoryb.grid(row=2, column=0, columnspan=4)
        Button(master, text="%", command=lambda: self.entry_window_content("%"), activebackground='gray16', bg='gray12',
               fg='white', padx=5, width=3, height=1, font=("Arial", 20, "bold")).grid(row=3, column=0)
        Button(master, text="√", command=lambda: self.sqrt(),activebackground='gray16',bg='gray12',
               fg='white', padx=5, width=3, height=1, font=("Arial", 20, "bold")).grid(row=3, column=1)
        Button(master, text="x²", command=lambda: self.pow(), activebackground='gray16', bg='gray12',
               fg='white', padx=5, width=3, height=1, font=("Arial", 20, "bold")).grid(row=3, column=2)
        Button(master, text="1/x", command=lambda: self.one_by_x(), activebackground='gray16', bg='gray12',
               fg='white', padx=5, width=3, height=1, font=("Arial", 20, "bold")).grid(row=3, column=3)
        Button(master, text="CE", command=lambda: self.clear_text_window(), activebackground='gray16', bg='gray12',
               fg='white', padx=5, width=3, height=1, font=("Arial", 20, "bold")).grid(row=4, column=0)
        Button(master, text="C", command=lambda: self.clear_one_sign(), activebackground='gray16', bg='gray12',
               fg='white', padx=5, width=3, height=1, font=("Arial", 20, "bold")).grid(row=4, column=1)
        Button(master, text="<", command=lambda: self.clear_one_sign(), activebackground='gray16', bg='gray12',
               fg='white', padx=5, width=3, height=1, font=("Arial", 20, "bold")).grid(row=4, column=2)
        Button(master, text="÷", command=lambda: self.entry_window_content("÷"), activebackground='gray16', bg='gray12',
               fg='white', padx=5, width=3, height=1, font=("Arial", 20, "bold")).grid(row=4, column=3)
        Button(master, text="7", command=lambda: self.entry_window_content(7), activebackground='gray16', bg='gray7',
               fg='white', padx=5, width=3, height=1, font=("Arial", 20, "bold")).grid(row=5, column=0)
        Button(master, text="8", command=lambda: self.entry_window_content(8), activebackground='gray16', bg='gray7',
               fg='white', padx=5, width=3, height=1, font=("Arial", 20, "bold")).grid(row=5, column=1)
        Button(master, text="9", command=lambda: self.entry_window_content(9), activebackground='gray16', bg='gray7',
               fg='white', padx=5, width=3, height=1, font=("Arial", 20, "bold")).grid(row=5, column=2)
        Button(master, text="x", command=lambda: self.entry_window_content("x"), activebackground='gray16', bg='gray12',
               fg='white', padx=5, width=3, height=1, font=("Arial", 20, "bold")).grid(row=5, column=3)
        Button(master, text="4", command=lambda: self.entry_window_content(4), activebackground='gray16', bg='gray7',
               fg='white', padx=5, width=3, height=1, font=("Arial", 20, "bold")).grid(row=6, column=0)
        Button(master, text="5", command=lambda: self.entry_window_content(5), activebackground='gray16', bg='gray7',
               fg='white', padx=5, width=3, height=1, font=("Arial", 20, "bold")).grid(row=6, column=1)
        Button(master, text="6", command=lambda: self.entry_window_content(6), activebackground='gray16', bg='gray7',
               fg='white', padx=5, width=3, height=1, font=("Arial", 20, "bold")).grid(row=6, column=2)
        Button(master, text="-", command=lambda: self.entry_window_content("-"), activebackground='gray16', bg='gray12',
               fg='white', padx=5, width=3, height=1, font=("Arial", 20, "bold")).grid(row=6, column=3)
        Button(master, text="1", command=lambda: self.entry_window_content(1), activebackground='gray16', bg='gray7',
               fg='white', padx=5, width=3, height=1, font=("Arial", 20, "bold")).grid(row=7, column=0)
        Button(master, text="2", command=lambda: self.entry_window_content(2), activebackground='gray16', bg='gray7',
               fg='white', padx=5, width=3, height=1, font=("Arial", 20, "bold")).grid(row=7, column=1)
        Button(master, text="3", command=lambda: self.entry_window_content(3), activebackground='gray16', bg='gray7',
               fg='white', padx=5, width=3, height=1, font=("Arial", 20, "bold")).grid(row=7, column=2)
        Button(master, text="+", command=lambda: self.entry_window_content("+"), activebackground='gray16', bg='gray12',
               fg='white', padx=5, width=3, height=1, font=("Arial", 20, "bold")).grid(row=7, column=3)
        Button(master, text="E", command=lambda: self.tajna_metoda(), activebackground='gray16', bg='gray12',
               fg='white', padx=5, width=3, height=1, font=("Arial", 20, "bold")).grid(row=8, column=0)
        Button(master, text="0", command=lambda: self.entry_window_content(0), activebackground='gray16', bg='gray7',
               fg='white', padx=5, width=3, height=1, font=("Arial", 20, "bold")).grid(row=8, column=1)
        Button(master, text=".", command=lambda: self.entry_window_content("."), activebackground='gray16', bg='gray12',
               fg='white', padx=5, width=3, height=1, font=("Arial", 20, "bold")).grid(row=8, column=2)
        Button(master, text="=", command=lambda: self.calculate(), activebackground='gray16', bg='gray12',
               fg='white', padx=5, width=3, height=1, font=("Arial", 20, "bold")).grid(row=8, column=3)


    def clear_text_window(self):

        self.entry_window.delete(0, END)

    def clear_one_sign(self):

        self.content = self.entry_window.get()
        self.content = self.content[:-1]
        self.entry_window.delete(0, END)
        self.entry_window.insert(0, self.content)

    def entry_window_content(self, content):

        self.entry_window.insert(END, content)

    def tajna_metoda(self):

        self.entry_window.delete(0, END)
        self.entry_window.insert(0, "Duch nie wiedzial o HW")

    def calculate(self):

        self.window_content = self.entry_window.get()
        self.replace_mul_and_div()
        self.entry_window.delete(0, END)
        try:
            self.validated = eval(self.validated)
        except:
            self.entry_window.insert(0, "Error")
        else:
            self.entry_window.insert(0, self.validated)

    def pow(self):
        self.window_content = self.entry_window.get()
        self.replace_mul_and_div()
        self.entry_window.delete(0, END)
        try:
            self.validated = eval(self.validated)
        except:
            self.entry_window.insert(0, "Error")
        else:
            self.validated = self.validated * self.validated
            self.entry_window.insert(0, self.validated)

    def sqrt(self):
        self.window_content = self.entry_window.get()
        self.replace_mul_and_div()
        self.entry_window.delete(0, END)
        try:

            self.validated = eval(self.validated)
        except:

            self.entry_window.insert(0, "Error")
        else:
            try:

                self.validated = sqrt(self.validated)
            except:

                self.entry_window.insert(0, "Error")
            else:

                self.entry_window.insert(0, self.validated)

    def one_by_x(self):
        self.window_content = self.entry_window.get()
        self.replace_mul_and_div()
        self.entry_window.delete(0, END)
        try:

            self.validated = eval(self.validated)
        except:

            self.entry_window.insert(0, "Error")
        else:
            try:

                self.validated = 1/self.validated
            except:

                self.entry_window.insert(0, "Error")
            else:

                self.entry_window.insert(0, self.validated)

    def replace_mul_and_div(self):

        self.validated = self.window_content.replace('÷', '/')
        self.validated = self.validated.replace('x', '*')








init=Tk()
object=kalkulator(init)
init.mainloop()
