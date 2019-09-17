"""This app will be used by the company to add data to the database when vehicles are bought, sold, stolen or get
written off. The program will be built as a GUI that will give the user instructions on how to fill in information.
Vehicle ids remain with the vehicle even after sale or loss and id will not be replaced. Id number dies with vehicle
in the database."""

from tkinter import *
from tkinter import messagebox
from pg8000 import connect


# The main class where all the programs functionality comes from.
class VehicleApp:
    def __init__(self, master, is_active):
        self.master = master
        self.string_it = StringVar
        # This generates and sets up the window
        self.frame = Frame(self.master, width=1200, height=720)
        self.frame.grid()  # places the frame onto the window

        # Variables used later in the program
# ---------------------------------------------------------------------------------------------------------------------
        self.car_manufacturer_ent = ""
        self.model_ent = ""
        self.vehicle_type_ent = ""
        self.license_plate_ent = ""
        self.vin_number_ent = ""
# ---------------------------------------------------------------------------------------------------------------------

        self.is_active = is_active
        if self.is_active is False:
            try:
                # Collects the password for the database
                f = open("Password.txt", "r")
                read_line = f.readline()
                f.close()

                # Collects my db name
                db = open("database.txt", "r")
                read_db = db.readline()
                db.close()

                # Creates a connection to my database
                self.conn = connect(user='postgres', password=read_line, database=read_db)
                # Creates a cursor used to carry out any SQL commands
                self.cursor = self.conn.cursor()

                # Calls my first method that generates the home screen
                self.home_page()

                # Brings up a text box that warns that a connection can not be established then it stops the program.
                # Then it closes the program
            except Exception as e:
                print(e)
                messagebox.showerror("Connection error", "There is no connection available.")
                quit()
        else:
            pass

    # Instructs the user how to use the program as well as stores the buttons for the instructions.
    def home_page(self):
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

        remove_car = Button(self.frame, text="Remove car", font="bold 12", command=self.des_home_remove_vehicles)
        remove_car.place(x=140, y=400)

        quit_button = Button(self.frame, text="quit", font="bold 12", command=self.leave)
        quit_button.place(y=400, x=900)

# Section for window rebuilds and ending the program
# --------------------------------------------------------------------------------------------------------------------
    # Destroys the frame then rebuilds it as a blank frame, then it finally fills the frame with the widgets from
    # the add_vehicle method.
    def des_home_add_vehicles(self):
        self.frame.destroy()
        self.__init__(self.master, True)
        self.add_vehicle()

    # Does the same as the above but fills the empty frame with the widgets from the remove_vehicle method.
    def des_home_remove_vehicles(self):
        self.frame.destroy()
        self.__init__(self.master, True)
        self.remove_vehicle()

    # Destroys the current frame the builds the home-screen frame.
    def back_to_home(self):
        self.frame.destroy()
        self.__init__(self.master, False)

    # closes all connections to the database then safely shuts down the program.
    def leave(self):
        self.cursor.close()
        self.conn.close()
        quit()
# ---------------------------------------------------------------------------------------------------------------------

# Section for add vehicle window and remove vehicle window and their widgets
# ---------------------------------------------------------------------------------------------------------------------
    # Method used to add vehicles to the database I created. Ordered in the same order as the database to make life
    # easier.
    def add_vehicle(self):
        new_vehicle_heading = Label(self.frame, text="New Vehicle", font="bold 30")
        new_vehicle_heading.place(x=10, y=10)

        # User input is collected from these widgets.
    # -----------------------------------------------------------------------------------------------------------------
        car_manufacturer = Label(self.frame, text="Car Manufacturer:", font="bold 17")
        car_manufacturer.place(x=0, y=80)

        self.car_manufacturer_ent = Entry(self.frame, font="bold 17")
        self.car_manufacturer_ent.place(x=200, y=80)

        model = Label(self.frame, text="Model:", font="bold 17")
        model.place(x=0, y=140)

        self.model_ent = Entry(self.frame, font="bold 17")
        self.model_ent.place(x=200, y=140)

        vehicle_type = Label(self.frame, text="Vehicle type:", font="bold 17")
        vehicle_type.place(x=0, y=200)

        self.vehicle_type_ent = Entry(self.frame, font="bold 17")
        self.vehicle_type_ent.place(x=200, y=200)

        license_plate = Label(self.frame, text="License plate:", font="bold 17")
        license_plate.place(x=0, y=260)

        self.license_plate_ent = Entry(self.frame, font="bold 17")
        self.license_plate_ent.place(x=200, y=260)

        vin_number = Label(self.frame, text="Vin number:", font="bold 17")
        vin_number.place(x=0, y=320)

        self.vin_number_ent = Entry(self.frame, font="bold 17")
        self.vin_number_ent.place(x=200, y=320)
    # -----------------------------------------------------------------------------------------------------------------

        return_home_btn = Button(self.frame, text="Return to Home", font="bold 12", command=self.back_to_home)
        return_home_btn.place(x=300, y=370)

        add_button = Button(self.frame, text="Add Vehicle", font="bold 12", command=self.enter_vehicle_information)
        add_button.place(x=150, y=370)

    # Method used to remove a vehicle if it is destroyed, stolen or sold
    def remove_vehicle(self):
        remove_veh_header = Label(self.frame, text="Remove vehicle", font="bold 30")
        remove_veh_header.place(x=10, y=0)

        vehicle_remove = Label(self.frame, text="Vehicle to remove:", font="bold 17")
        vehicle_remove.place(x=0, y=70)

        return_home_btn = Button(self.frame, text="Return to Home", font="bold 12", command=self.back_to_home)
        return_home_btn.place(x=300, y=120)
# ---------------------------------------------------------------------------------------------------------------------

# Database tasks for creating a new vehicle in the vehicles table.
# ---------------------------------------------------------------------------------------------------------------------
    def enter_vehicle_information(self):
        get_manufacturer = self.car_manufacturer_ent.get()
        get_model = self.model_ent.get()
        get_vehicle_type = self.vehicle_type_ent.get()
        get_license_plate = self.license_plate_ent.get()
        get_vin = self.vin_number_ent.get()

        get_manufacturer = str(get_manufacturer)
        get_model = str(get_model)
        get_vehicle_type = str(get_vehicle_type)
        get_license_plate = str(get_license_plate)
        get_vin = int(get_vin)

        if get_manufacturer == "" or get_model == "" or get_vehicle_type == "" or get_license_plate == ""\
                or get_vin == "":
            messagebox.showerror("Missing information", "Please fill in all the boxes")
            self.des_home_add_vehicles()
        else:
            if len(str(get_vin)) > 6 or len(str(get_vin)) < 6:
                messagebox.showerror("Vin incorrect", """The vin number entered is too short or too long. It has to 
consist of 6 numbers""")
                self.des_home_add_vehicles()
            else:
                # Inserts the data entered above into the database using the cursor to execute the statement below.
                insert_into_database = f"""INSERT INTO vehicles(manufacturer, model, vehicle_type, licence_plate_num, vin_num
                , availability) VALUES('{get_manufacturer.upper()}', '{get_model.capitalize()}', '{get_vehicle_type}', 
                '{get_license_plate.upper()}', '{get_vin}', 'true')"""

                # The try section of this block only executes if the above statement has no errors
                try:
                    self.cursor.execute(insert_into_database)
                    self.conn.commit()
                    messagebox.showinfo("Success", "You successfully added a new car.")
                # If an error is picked up in the try block it is printed out in the except block below
                except Exception as e:
                    print(e)
                    messagebox.showerror("Insertion error", "There was a problem with something in your entered data.")

                self.cursor.close()
                self.conn.close()

                self.des_home_add_vehicles()
# ---------------------------------------------------------------------------------------------------------------------


# Generates the window that the GUI is built on
window = Tk()
window.title("Vehicle App")
window.geometry("1200x720+0+0")  # The windows width and height are configured here.
app = VehicleApp(window, False)  # Calls the class I built above

window.mainloop()






