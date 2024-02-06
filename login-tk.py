from tkinter import *
from tkinter import messagebox
from subprocess import call, Popen

import mysql.connector as con

class LoginWindow:
    def __init__(self, master):
        self.master = master
        master.title("Login")

        self.label = Label(master, image=image)
        self.label.pack()

        self.Username_label = Label(master, text="User Name", font=("Georgia", 12), fg="#00004d", bg="white")
        self.Username_label.place(x=200, y=320)

        self.Username_edit = Entry(master, font=("Georgia", 14),fg="#00004d")
        self.Username_edit.place(x=200, y=350, width=220, height=45)

        self.password_label = Label(master, text="Password", font=("Georgia", 12), fg="#00004d", bg="white")
        self.password_label.place(x=200, y=480)

        self.password_edit = Entry(master, font=("Georgia", 14), show="*")
        self.password_edit.place(x=200, y=510,width=220, height=45)

        self.login_button = Button(master, text="LOGIN", font=("Georgia", 14), fg="#00004d", command=self.login)
        self.login_button.place(x=100, y=630,width=100, height=45)

        self.signup_button = Button(master, text="SIGN UP", font=("Georgia", 14), fg="#00004d", command=self.signup)
        self.signup_button.place(x=280, y=630,width=100, height=45)

    def login(self):

        db = con.connect(host='localhost', user='root', password='123456', database='facerecog')
        c=db.cursor()
        un=self.Username_edit.get()
        pw=self.password_edit.get()

        c.execute("SELECT * FROM register WHERE UserName='"+un+"' AND Password = '"+pw+"'")
        result = c.fetchone()
        if result:
            messagebox.showinfo("Success", "Login Successful")
            call(['python', "Home-tk.py"])
        else:
            messagebox.showerror("Error", "Invalid Login")

    def signup(self):
        call(['python', "register-tk.py"])

root = Tk()
root.geometry("1040x840")
root.configure(bg="white")
image = PhotoImage(file="LoginBg.png")
login = LoginWindow(root)

root.mainloop()
