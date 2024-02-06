import tkinter as tk


from subprocess import call, Popen


class HomeMainWindow:
    def __init__(self, master):
        self.master = master
        master.title("HomeMainWindow")
        master.geometry("1200x800")

        self.frame = tk.Frame(master)
        self.frame.place(x=-20, y=0, width=950, height=1000)
        self.frame.config(relief=tk.SOLID, bd=2)

        self.label = tk.Label(self.frame)
        self.label.place(x=100, y=-40, width=1000, height=890)
        self.label.config(image=image)

        self.create_btn = tk.Button(self.frame, text="Create", command=self.Create)
        self.create_btn.place(x=550, y=210, width=181, height=35)
        self.create_btn.config(font=("Georgia", 12), bg="#00004d", fg="white")

        self.detect_btn = tk.Button(self.frame, text="Detect", command=self.detectImage)
        self.detect_btn.place(x=550, y=365, width=181, height=35)
        self.detect_btn.config(font=("Georgia", 12), bg="#00004d", fg="white")

        self.start_btn = tk.Button(self.frame, text="Start", command=self.Start)
        self.start_btn.place(x=550, y=535, width=181, height=35)
        self.start_btn.config(font=("Georgia", 12), bg="#00004d", fg="white")

        self.view_btn = tk.Button(self.frame, text="View")
        self.view_btn.place(x=550, y=705, width=181, height=35)
        self.view_btn.config(font=("Georgia", 12),  bg="#00004d", fg="white")

        self.signout_button = tk.Button(self.frame, text="Signout", command=self.login)
        self.signout_button.place(x=700, y=50, width=70, height=30)
        self.signout_button.config(font=("Georgia", 10), fg="#00004d", bg="white")

        self.about_button = tk.Button(self.frame, text="About")
        self.about_button.place(x=780, y=50, width=70, height=30)
        self.about_button.config(font=("Georgia", 10), fg="#00004d", bg="white")

        self.contact_button = tk.Button(self.frame, text="Contact")
        self.contact_button.place(x=860, y=50, width=70, height=30)
        self.contact_button.config(font=("Georgia", 10), fg="#00004d", bg="white")

        self.CriminalEye_label = tk.Label(self.frame, text="CriminalEye")
        self.CriminalEye_label.place(x=350, y=50, width=150, height=35)
        self.CriminalEye_label.config(font=("Georgia", 18), fg="#00004d", bg="white")

    def Create(self):
        call(['python', "Createdb-tk.py"])

    def login(self):
        call(['python', "login-tk.py"])

    def Start(self):
        call(['python', "test.py"])

    def detectImage(self):
        Popen(['python', 'Image-detect.py'])

root = tk.Tk()
image = tk.PhotoImage(file="Home-re.png")
HomeMainWindow(root)
root.mainloop()
