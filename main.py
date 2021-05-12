# To-do List

# Imports
# GUI
import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import *
from tkinter.font import Font
from tkmacosx import Button, CircleButton

# Date and time
import datetime

# Images
from PIL import Image, ImageTk

# Data storage
import json

# Email
import smtplib

# Email verification
from verify_email import verify_email


# Housing of the program
class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("To-do List")  # Title of the window
        self.root.geometry('370x500+600+75')  # Window size
        self.root.resizable(False, False)  # Disable window resizing
        self.root.mainloop()

        # Main body (1)
        def home(self):
            try:
                self.root.destroy()
            except:
                pass
            with open("data.json", "r") as file:
                self.data = json.load(file)

            # Sets up the ability for theming on the main page
            self.root = tk.Frame(self.root, width=370, height=500,
                                 bg=self.data["bg_colour"])
            self.root.place(x=0, y=0)

            # Title (1)
            # Font size and weight for the title
            self.title_label_font = Font(
                family="SF Pro Rounded",
                size=20,
                weight="bold"
            )
            # Title name and colour
            self.title_label = tk.Label(self.root, text="To-do List",
                                        font=self.title_label_font,
                                        fg=self.data["fg_colour"],
                                        bg=self.data["bg_colour"])
            self.title_label.place(x=30, y=25)


main = Window()

