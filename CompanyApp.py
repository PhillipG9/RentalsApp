"""This app will be used by the company to add data to the database when vehicles are bought, sold, stolen or get
written off. The program will be built as a GUI that will give the user instructions on how to fill in information.
Vehicle ids remain with the vehicle even after sale or loss and id will not be replaced. Id number dies with vehicle
in the database."""

import time
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from pg8000 import connect


class VehicleApp:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.string_it = StringVar
        self.frame = Frame(self.master, width=1200, height=720)
        self.frame.grid()
        try:
            f = open("Password.txt", "r")
            read_line = f.readline()
            f.close()

            db = open("database.txt", "r")
            read_db = db.readline()
            db.close()

            self.conn = connect(user='postgres', password=read_line, database=read_db)
            self.cursor = self.conn.cursor()
            print("Connection successful")
            self.widgets()
        except Exception as e:
            print(e)
            messagebox.showerror("Connection error", "There is no connection available.")
            quit()

    def widgets(self):
        head = Label(self.frame, text="Vehicles", font="bold 30")
        head.place(x=0, y=0)

        information = Text(self.frame, height=9)
        information.insert(INSERT, """This page gives you two options. The fist option is to add a car. If you need to
add a new vehicle you will be redirected to a page that allows you to enter the
new vehicles information such as car model, car type and license plate number. 
The second option allows you to remove vehicles from the database and requires
the reason for removal and all the other information.""")
        information.insert(END, """ Please be careful of what
information is entered!""")
        information.place(x=20, y=100)

        add_car = Button(self.frame, text="Add Vehicle", font="bold 12", command=self.add_vehicle)
        add_car.place(x=20, y=400)

        remove_car = Button(self.frame, text="Remove car", font="bold 12", command="")
        remove_car.place(x=140, y=400)

        quit_button = Button(self.frame, text="quit", font="bold 12", command=quit)
        quit_button.place(y=400, x=900)

    def add_vehicle(self):
        self.frame.destroy()
        self.__init__(self.new_master)
        print("Hello world")
        print("This is my home")

        self.cursor.close()
        self.conn.close()

    def new_master(self):
        header = Label(self.frame, text="Hello world", font="bold 13")
        header.place(x=0, y=0)


window = Tk()
window.title("Vehicle App")
window.geometry("1200x720+0+0")
app = VehicleApp(window)

window.mainloop()






