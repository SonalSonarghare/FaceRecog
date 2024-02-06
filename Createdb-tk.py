import tkinter as tk
from subprocess import call
from tkinter import ttk, messagebox
from tkinter import filedialog
import os

import mysql.connector as con


class CreateMainWindow:
    def browse_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            file_name = os.path.basename(file_path)
            self.selected_file.set(file_name)
            self.file_path = file_path

    def store_image(self):
        if hasattr(self, "file_path"):
            file_name = os.path.basename(self.file_path)
            os.rename(self.file_path, f"faces/{file_name}")

            # Open a database connection and insert a new record
            try:
                db = con.connect(host='localhost', user='root', password='123456', database='facerecog')
                cursor = db.cursor()

                # Prepare the SQL statement to insert a new record
                sql = "INSERT INTO criminaldb (CriminalName, Gender, Crime, LastFound) VALUES (%s, %s, %s, %s)"
                values = (self.Name.get(), self.gender_var.get(), self.crime_var.get(), self.location_var.get())
                cursor.execute(sql, values)
                db.commit()
                messagebox.showinfo("Success", "Criminal data saved successfully!")
                call(['python', "Home-tk.py"])
                self.root.destroy()  # Use self.root instead of root

            except con.Error as e:
                messagebox.showerror("Error", f"Error occurred while inserting record into the database: {e}")



    def __init__(self):

        self.root = tk.Tk()
        self.root.geometry("1629x880")
        self.root.title("CreateMainWindow")

        # Frame
        self.frame = tk.Frame(self.root)
        self.frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Label
        self.label = tk.Label(self.frame)
        self.label.place(x=70, y=-80, relwidth=1, relheight=1)

        # LineEdits
        self.Name = tk.Entry(self.frame)
        self.Name.place(x=280, y=160, width=301, height=41)

        self.Crime = tk.Entry(self.frame)
        self.Crime.place(x=280, y=290, width=301, height=41)

        self.LastFound = tk.Entry(self.frame)
        self.LastFound.place(x=790, y=290, width=301, height=41)

        # Drop-down menus
        self.crime_var = tk.StringVar(value="Select crime type")
        crimes = ["Arson", "Mafia", "CyberCrime", "Fraud", "Corruption", "Homicide", "Vandalism",
                  "Treason", "Trafficking", "Murder", "Terrorist", "Blackmail", "Money Laundering"]
        self.crime_dropdown = ttk.Combobox(self.frame, textvariable=self.crime_var, values=crimes,
                                           foreground="#00004d", font=(
                "Georgia", 12))  # Set the color, font size, and font type of the dropdown menu text

        self.crime_dropdown.place(x=280, y=290, width=301, height=41)

        self.location_var = tk.StringVar(value="Select last found location")
        locations = ["UK", "USA", "India", "Australia", "Canada", "Pakistan"]


        self.location_dropdown = ttk.Combobox(self.frame, textvariable=self.location_var, values=locations,
                                              foreground="#00004d", font=(
            "Georgia", 12))  # Set the color, font size, and font type of the dropdown menu text
        self.location_dropdown.place(x=790, y=290, width=301, height=41)

        # Labels
        self.CriminalName = tk.Label(self.frame, text="Criminal Name", font=("Georgia", 14, " bold"), fg="#00004d")
        self.CriminalName.place(x=120, y=155)

        self.Gender = tk.Label(self.frame, text="Gender", font=("Georgia", 14, " bold"), fg="#00004d")
        self.Gender.place(x=660, y=160)

        self.Crime = tk.Label(self.frame, text="Crime", font=("Georgia", 14, " bold"), fg="#00004d")
        self.Crime.place(x=120, y=290)

        self.LastFound = tk.Label(self.frame, text="Last Found", font=("Georgia", 14, " bold"), fg="#00004d")
        self.LastFound.place(x=660, y=290)

        self.Createlabel = tk.Label(self.frame, text="CREATE CRIMINAL DATABASE ", font=("Georgia", 16, "bold"),
                                    fg="#00004d")
        self.Createlabel.place(x=520, y=60)

        self.selected_file = tk.StringVar()

        self.UploadImage = tk.Label(self.frame, text="Upload Image: ", font=("Georgia", 14, " bold"), fg="#00004d")
        self.UploadImage.place(x=120, y=400)

        self.browse_btn = tk.Button(self.frame, text="UPLOAD", font=("Georgia", 14, "bold"), bg="#00004d", fg="white",
                                    command=self.browse_image)
        self.browse_btn.place(x=280, y=390, width=150, height=50)



        # RadioButtons
        self.gender_var = tk.StringVar()
        self.radioButton1 = tk.Radiobutton(self.frame, text="Male", font=("Georgia", 14, " bold"), fg="#00004d",
                                           variable=self.gender_var, value="Male")
        self.radioButton1.place(x=790, y=160)

        self.radioButton2 = tk.Radiobutton(self.frame, text="Female", font=("Georgia", 14, " bold"), fg="#00004d",
                                           variable=self.gender_var, value="Female")

        self.radioButton2.place(x=790, y=200)


        self.create_btn = tk.Button(self.frame, text="CREATE", font=("Georgia", 14, "bold"), bg="#00004d", fg="white",
                                    command=self.store_image)
        self.create_btn.place(x=550, y=600, width=150, height=50)





    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = CreateMainWindow()
    app.run()
