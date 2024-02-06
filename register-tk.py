import tkinter as tk
from tkinter import *
from tkinter import messagebox
import mysql.connector as con
from subprocess import call, Popen


class RegisterMainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Register")
        self.root = master  # Save the Tk object as an attribute


        self.label = Label(master, image=image)
        self.label.pack()

        self.Name_label = Label(master, text="Name", font=("Georgia", 12), fg="#00004d", bg="white")
        self.Name_label.place(x=200, y=250)

        self.Name_edit = Entry(master, font=("Georgia", 14), fg="#00004d")
        self.Name_edit.place(x=200, y=280, width=260, height=45)

        self.Email_label = Label(master, text="Email", font=("Georgia", 12), fg="#00004d", bg="white")
        self.Email_label.place(x=200, y=350)

        self.Email_edit = tk.Entry(master, font=("Georgia", 14), fg="#00004d")
        self.Email_edit.place(x=200, y=380, width=260, height=45)

        self.Username_label = Label(master, text="Username", font=("Georgia", 12), fg="#00004d", bg="white")
        self.Username_label.place(x=550, y=250)

        self.Username_edit = Entry(master, font=("Georgia", 14), fg="#00004d")
        self.Username_edit.place(x=550, y=280, width=260, height=45)

        self.Pass_label = Label(master, text="Password", font=("Georgia", 12), fg="#00004d", bg="white")
        self.Pass_label.place(x=550, y=350)

        self.Pass_edit = tk.Entry(master, font=("Georgia", 14),fg="#00004d", show="*")
        self.Pass_edit.place(x=550, y=380,width=260, height=45)

        self.Mobile_label = Label(master, text="Mobile", font=("Georgia", 12), fg="#00004d", bg="white")
        self.Mobile_label.place(x=200, y=450)

        self.Mobile_edit = tk.Entry(master, font=("Georgia", 14), fg="#00004d")
        self.Mobile_edit.place(x=200, y=480,width=260, height=45)

        self.desig_label = Label(master, text="Designation", font=("Georgia", 12), fg="#00004d", bg="white")
        self.desig_label.place(x=550, y=450)

        self.desig_edit = tk.Entry(master, font=("Georgia", 14), fg="#00004d")
        self.desig_edit.place(x=550, y=480,width=260, height=45)



        self.sign_button= Button(master, text="SIGNUP", font=("Georgia", 14), fg="#00004d", command=self.signup)
        self.sign_button.place(x=450, y=580,width=100, height=45)

    def signup(self):

        try:
            db = con.connect(host='localhost', user='root', password='123456', database='facerecog')
            c = db.cursor()

            Name = self.Name_edit.get()
            Username = self.Username_edit.get()
            Email = self.Email_edit.get()
            Password = self.Pass_edit.get()
            Mobile = self.Mobile_edit.get()
            Designation = self.desig_edit.get()


            query = "INSERT INTO register (Name, UserName, Email,Password ,Mobile,Designation) VALUES(%s,%s,%s,%s,%s,%s)"
            value = (Name, Username, Email,Password,Mobile, Designation)

            c.execute(query, value)
            db.commit()
            messagebox.showinfo('Success', 'Successfullu Inserted')
            call(['python', "login-tk.py"])
            self.root.destroy()  # Use self.root instead of root

        except con.Error as e:
            messagebox.showinfo('Unsuccessful', 'Try Again')



        self.root.mainloop()


root = Tk()
root.geometry("1040x840")
root.configure(bg="white")
image = PhotoImage(file="register.png")
login = RegisterMainWindow(root)

root.mainloop()