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
from validate_email import validate_email


# Housing of the program
class ToDo:
    def __init__(self):
        self.root_1 = tk.Tk()
        self.root_1.title("To-do List")  # Title of the window
        self.root_1.geometry('370x500+600+75')  # Window size
        self.root_1.resizable(False, False)  # Disable window resizing

    # Main body (1)
    def home(self):
        # Creates a new frame for the home page
        self.root = tk.Frame(self.root_1, width=370, height=500)
        self.root.place(x=0, y=0)

        # Title (1)
        # Font
        self.title_label_font = Font(
            family="SF Pro Rounded",  # Font name
            size=20,  # Font size
            weight="bold"  # Font weight
        )
        # Title name and colour
        self.title_label = tk.Label(self.root, text="To-do List",
                                    font=self.title_label_font)

        self.title_label.place(x=30, y=25)

        # Inputs (1)
        # Task name entry
        self.new_task_entry_var = tk.StringVar()  # Holds a string
        self.new_task_entry = Entry(self.root,
                                    textvariable=self.new_task_entry_var,
                                    width=11)
        self.new_task_entry.place(x=35, y=75)
        # Time entry
        self.new_task_time_var = tk.StringVar()
        # Places the current time into the input field
        self.new_task_time = Entry(self.root,
                                   textvariable=self.new_task_time_var,
                                   width=5)
        self.new_task_time.place(x=156, y=75)
        # Date entry
        self.date_var = tk.StringVar()
        self.data_entry = Entry(self.root, textvariable=self.date_var, width=7)
        self.data_entry.place(x=223, y=75)

        # List (1)
        # Displays all inputted tasks
        self.list_tasks = tk.Listbox(self.root, width=29, height=16)
        self.list_tasks.place(x=35, y=125)

        # Buttons (1)
        # Button which adds a task
        self.add_image = ImageTk.PhotoImage(
            Image.open("/Users/vic/PycharmProjects/todo/images/add.png"))
        self.add_task_button = CircleButton(self.root, image=self.add_image,
                                            bg='#ffffff', fg='#000000',
                                            borderless=1,
                                            width=35)
        self.add_task_button.place(x=308, y=71)

        # Button which deletes the selected task
        self.delete_selected = Button(self.root, text="Delete", bg='#ffffff',
                                      fg='#000000', borderless=1,
                                      activebackground=('#C96666', '#C96666')
                                      )
        self.delete_selected.place(x=35, y=423)
        # Button which deletes all inputted tasks
        self.delete_all = Button(self.root, text="Delete All", bg='#ffffff',
                                 fg='#000000', borderless=1,
                                 activebackground=('#C96666', '#C96666')
                                 )
        self.delete_all.place(x=130, y=423)
        # Button which opens up the settings page
        self.settings_image = ImageTk.PhotoImage(
            Image.open("/Users/vic/PycharmProjects/todo/images/settings.png"))
        self.settings_button = CircleButton(self.root,
                                            image=self.settings_image,
                                            bg='#ffffff', fg='#000000',
                                            borderless=1, width=35,
                                            command=self.settings)
        self.settings_button.place(x=308, y=418)

        self.root_1.mainloop()

    # Settings page (2)
    def settings(self):
        # Creates a new frame for the preferences page
        self.root = tk.Frame(self.root_1, width=370, height=500)

        self.root.place(x=0, y=0)

        # Title (2)
        # Font
        self.title_label_font = Font(
            family="SF Pro Rounded",
            size=20,
            weight="bold"
        )
        # Title name and colour - Preferences
        self.title_label = tk.Label(self.root, text="Preferences",
                                    font=self.title_label_font)

        self.title_label.place(x=30, y=35)

        # Buttons (2)
        # Button which returns back to the home page
        self.back_button = Button(self.root, text="Back", bg='#ffffff',
                                  fg='#000000', borderless=1,
                                  command=self.home)
        self.back_button.place(x=3, y=3)

        # Options
        # Themes
        # Title name and colour - Themes
        self.pref_label = tk.Label(self.root, text="Themes",
                                   font=self.title_label_font)

        self.pref_label.place(x=30, y=80)

        # Button which alters the theme and text colour
        # The self.change_bg("bg, text") refers back to the def
        # White background, black text
        self.colour_white = Button(self.root, font="15",
                                   bg='#F4F3F1', fg='#F4F3F1', borderless=1,
                                   width=25, highlightbackground='#2E2F30')

        self.colour_white.place(x=35, y=125)
        # Black background, white text
        self.colour_black = Button(self.root, font="15",
                                   bg='#2E2F30', fg='#2E2F30', borderless=1,
                                   width=25)

        self.colour_black.place(x=65, y=125)
        # Red background, black text
        self.colour_red = Button(self.root, font="15",
                                 bg='#C96666',
                                 fg='#C96666', borderless=1, width=25,
                                 highlightbackground='#C96666')

        self.colour_red.place(x=95, y=125)
        # Green background, black text
        self.colour_green = Button(self.root, font="15",
                                   bg='#B0D8B5', fg='#B0D8B5',
                                   borderless=1,
                                   width=25)

        self.colour_green.place(x=125, y=125)
        # Blue background, black text
        self.colour_blue = Button(self.root, font="15",
                                  bg='#90ADC6', fg='#90ADC6',
                                  borderless=1,
                                  width=25)

        self.colour_blue.place(x=155, y=125)

        # Email
        # Title name and colour - Email
        self.email_label = tk.Label(self.root, text="Email",
                                    font=self.title_label_font)
        self.email_label.place(x=30, y=190)
        # Email entry
        self.email_entry_var = tk.StringVar()
        self.email_entry = Entry(self.root, textvariable=self.email_entry_var,
                                 width=32)
        self.email_entry.place(x=35, y=235)
        # Button which changes the set email
        self.change = Button(self.root, text="Change", bg='#ffffff',
                             fg='#000000', borderless=1
                             )
        self.change.place(x=32, y=285)

        # Help
        # Title name and colour - Help
        self.instructions_label = tk.Label(self.root, text="Help",
                                           font=self.title_label_font)

        self.instructions_label.place(x=30, y=350)
        # Button which opens the instructions window
        self.instructions = Button(self.root, text="Instructions",
                                   bg='#ffffff', fg='#000000', borderless=1,
                                   command=self.instructions_func)
        self.instructions.place(x=32, y=395)
        # Button which opens the requirements window
        self.requirements = Button(self.root, text="Requirements",
                                   bg='#ffffff', fg='#000000', borderless=1,
                                   command=self.requirements_func)
        self.requirements.place(x=32, y=426)
        self.root.mainloop()

    # Help menu
    # Instructions
    def instructions_func(self):
        messagebox.showinfo("Help",
                            "Instructions "
                            "\n \n 1. Input a task by specifying a title, "
                            "date and time. To add a task, click the + button."
                            "\n \n 2. Once the set time is reached, "
                            "an email will be sent. Click the delete button "
                            "to then remove the task from the list."
                            "\n \n 3. Clicking the settings button will "
                            "open up the preferences menu.")

    # Requirements
    def requirements_func(self):
        messagebox.showinfo("Help",
                            "Requirements "
                            "\n \n 1. An email is required in order to input "
                            "tasks."
                            "\n \n 2. This application uses 24 hour time for "
                            "inputs."
                            "\n \n 3. An internet connection is needed for "
                            "email capabilities to function."
                            "\n \n 4. MacOS is the only supported platform")


main = ToDo()
main.home()
