# passmanager.py
# By: Haani Saiyed

import tkinter
from tkinter.constants import DISABLED, END
from typing import Text
import json
from tkinter import filedialog
import string
import random


class passManager:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Password Manager")
        self.main_window.geometry("600x515")

        self.page_frame = tkinter.Frame(self.main_window)

        self.website_frame = tkinter.Frame(self.main_window)

        self.username_frame = tkinter.Frame(self.main_window)
        self.password_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.message_frame = tkinter.Frame(self.main_window)
        self.view_frame = tkinter.Frame(self.main_window)
        self.data_frame = tkinter.Frame(self.main_window)

        self.page_label = tkinter.Label(
            self.page_frame, text="Password Manager",  font=("Arial", 25))
        self.website_label = tkinter.Label(
            self.website_frame, text="Website:     ", bg='#003366', fg="#FFFFFF")
        self.website_entry = tkinter.Entry(
            self.website_frame, width=50)
        self.website_entry.insert(0, "https://www.")

        self.username_label = tkinter.Label(
            self.username_frame, text="Username:  ", bg='#003366', fg="#FFFFFF")
        self.username_entry = tkinter.Entry(self.username_frame, width=50)

        self.password_label = tkinter.Label(
            self.password_frame, text="Password: ", bg='#003366', fg="#FFFFFF")
        self.password_entry = tkinter.Entry(self.password_frame, width=35)
        self.passGen_button = tkinter.Button(
            self.password_frame, text="Generate Password", command=self.genPass)

        self.add_Button = tkinter.Button(
            self.bottom_frame, text="Add Password", command=self.getData)
        self.message_label = tkinter.Label(self.message_frame, text="")

        self.view_Button = tkinter.Button(
            self.view_frame, text="View All Passwords", command=self.viewAllPass)

        self.data_label = tkinter.Text(
            self.data_frame, bg='#003366', fg="#FFFFFF")

        self.page_label.pack(side="left")
        self.website_label.pack(side="left")
        self.website_entry.pack(side="left")

        self.username_label.pack(side="left")
        self.username_entry.pack(side="left")
        self.password_label.pack(side="left")
        self.password_entry.pack(side="left")
        self.passGen_button.pack(side="left")
        self.add_Button.pack(side="top")
        self.message_label.pack(side="left")
        self.view_Button.pack(side="top")
        self.data_label.pack(side="bottom")

        self.page_frame.pack()
        self.website_frame.pack()
        self.username_frame.pack()
        self.password_frame.pack()
        self.bottom_frame.pack()
        self.message_frame.pack()
        self.view_frame.pack()
        self.data_frame.pack()

        tkinter.mainloop()

    def getData(self):
        website = str(self.website_entry.get())
        username = str(self.username_entry.get())
        password = str(self.password_entry.get())
        newSite = {
            website: {
                'username ': username,
                'password ': password
            }
        }
        if(len(website) != 12 and len(password) != 0 and len(username) != 0):
            try:
                with open("passwordData.txt", 'r') as passwordData_file:
                    newData = json.load(passwordData_file)
                    newData.update(newSite)
            except FileNotFoundError:
                with open("passwordData.txt", "w") as passwordData_file:
                    json.dump(newSite, passwordData_file, indent=4)

            else:
                with open("passwordData.txt", "w") as passwordData_file:
                    json.dump(newData, passwordData_file, indent=4)
                    self.website_entry.delete(0, END)
                    self.username_entry.delete(0, END)
                    self.password_entry.delete(0, END)
                    self.website_entry.insert(0, "https://www.")
            self.message_label.config(text="Password Successfully Added")
        else:
            self.message_label.config(text="Password Not Added")

    def viewAllPass(self):
        if self.data_label.compare("end-1c", "!=", "1.0"):
            self.data_label.delete(0, END)

        # INITIALDIR IS INITIAL DIRECTORY FOR MY COMPUTER
        # WILL BE DIFFERENT FOR EACH DEVICE SO I MOVED IT OUT OF THE PARENTHESIS
        ## initialdir='/Users/Haani/Documents/Org. of Prog. Languages/project'
        file = tkinter.filedialog.askopenfilename()

        f = open(file, 'r')
        for line in f:
            self.data_label.insert('end', line)
        self.data_label.config(state=DISABLED)

    def genPass(self):
        lowerLetters = string.ascii_lowercase
        upperLetters = string.ascii_uppercase
        digits = string.digits
        specialChar = string.punctuation

        randLower = random.sample(lowerLetters, 6)
        randUpper = random.sample(upperLetters, 3)
        randDig = random.sample(digits, 3)
        randSpec = random.sample(specialChar, 3)

        passW = randLower + randUpper + randDig + randSpec
        random.shuffle(passW)
        password = "".join(passW)
        self.password_entry.insert(0, password)


pass_manager = passManager()
