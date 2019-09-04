"""This app will be used by the company to add data to the database when vehicles are bought, sold, stolen or get
written off. The program will be built as a GUI that will give the user instructions on how to fill in information.
Vehicle ids remain with the vehicle even after sale or loss and id will not be replaced. Id number dies with vehicle
in the database."""

# import time
from tkinter import *
# from tkinter import ttk
from tkinter import messagebox
# import pg8000
from pg8000 import connect


class VehicleApp:
    def __init__(self, master, is_active, *args, **kwargs):
        self.master = master
        self.string_it = StringVar
        # This generates and sets up the window
        self.frame = Frame(self.master, width=1200, height=720)
        self.frame.grid()
        self.car_manufacturer_ent = ""
        self.model_ent = ""
        self.vehicle_type_ent = ""
        self.license_plate_ent = ""
        self.vin_number_ent = ""
        self.is_active = is_active
        if self.is_active is False:
            try:
                f = open("Password.txt", "r")
                read_line = f.readline()
                f.close()

                db = open("database.txt", "r")
                read_db = db.readline()
                db.close()

                # Creates a connection to my database
                self.conn = connect(user='postgres', password=read_line, database=read_db)
                # Creates a cursor used to carry out any SQL commands
                self.cursor = self.conn.cursor()
                print("Connection successful")
                # Calls my first method that generates the home screen
                self.widgets()
                # self.add_vehicle()

                # Brings up a text box that warns that a connection can not be established then it stops the program.
            except Exception as e:
                print(e)
                messagebox.showerror("Connection error", "There is no connection available.")
                quit()
        else:
            pass

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

        add_car = Button(self.frame, text="Add Vehicle", font="bold 12", command=self.des_home_add_vehicles)
        add_car.place(x=20, y=400)

        remove_car = Button(self.frame, text="Remove car", font="bold 12", command="")
        remove_car.place(x=140, y=400)

        quit_button = Button(self.frame, text="quit", font="bold 12", command=quit)
        quit_button.place(y=400, x=900)

    def des_home_add_vehicles(self):
        self.frame.destroy()
        self.__init__(self.master, True)
        self.add_vehicle()

    def add_vehicle(self):
        new_vehicle_heading = Label(self.frame, text="New Vehicle", font="bold 30")
        new_vehicle_heading.place(x=10, y=10)

        car_manufacturer = Label(self.frame, text="Car Manufacturer:", font="bold 17")
        car_manufacturer.place(x=0, y=70)

        self.car_manufacturer_ent = Entry(self.frame, font="bold 17")
        self.car_manufacturer_ent.place(x=200, y=70)

        model = Label(self.frame, text="Model:", font="bold 17")
        model.place(x=0, y=110)

        self.model_ent = Entry(self.frame, font="bold 17")
        self.model_ent.place(x=200, y=110)

        vehicle_type = Label(self.frame, text="Vehicle type:", font="bold 17")
        vehicle_type.place(x=0, y=150)

        self.vehicle_type_ent = Entry(self.frame, font="bold 17")
        self.vehicle_type_ent.place(x=200, y=150)

        license_plate = Label(self.frame, text="License plate:", font="bold 17")
        license_plate.place(x=0, y=190)

        self.license_plate_ent = Entry(self.frame, font="bold 17")
        self.license_plate_ent.place(x=200, y=190)

        vin_number = Label(self.frame, text="Vin number:", font="bold 17")
        vin_number.place(x=0, y=230)

        self.vin_number_ent = Entry(self.frame, font="bold 17")
        self.vin_number_ent.place(x=200, y=230)

        self.cursor.close()
        self.conn.close()

        return_home_btn = Button(self.frame, text="Return to Home", font="bold 12", command=self.back_to_home)
        return_home_btn.place(x=10, y=600)

    def back_to_home(self):
        self.frame.destroy()
        self.__init__(self.master, False)


window = Tk()
window.title("Vehicle App")
window.geometry("1200x720+0+0")
app = VehicleApp(window, False)

window.mainloop()






