"""This application is used by a customer. Whenever a customer uses the app all required data is entered into the
databases. This is a GUI application that allows the user to enter their name, surname, email address, phone and number
and then allows them to select the vehicle they wish to rent."""

from tkinter import *


class RentalApp:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.string_it = StringVar
        self.frame = Frame(self.master, width=1200, height=720)
        self.frame.grid()


window = Tk()
window.title("Rentals App")
window.geometry("1200x720+0+0")
app = RentalApp(window)

window.mainloop()




