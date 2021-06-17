# To-do List

# Imports
# GUI
import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import *
from tkinter.font import Font
from tkmacosx import Button, CircleButton

# Audio
from playsound import playsound

# Date and time
import datetime

# Images
from PIL import Image, ImageTk

# Data storage
import json

# Notifications
import os

# Email
import smtplib

# Email verification
from validate_email import validate_email

# Math
import math

# Location detection
import geocoder

# API
import requests
API_KEY = "413ddc96f3900cda7e59f97f89395675"

# Title and message for 'email sent' confirmation
title = "To-do List"
message = "Success; email has been sent"


# Housing of the program
class ToDo:
    def __init__(self):
        self.root_1 = tk.Tk()
        self.root_1.title("To-do List")  # Title of the window
        self.root_1.geometry('370x500+600+75')  # Window size
        self.root_1.resizable(False, False)  # Disable window resizing

    # Main body (1)
    # Switching between the home page and the settings page will be done so by
    # creating a frame, then deleting the prior frame
    def home(self):
        # Reading the JSON file (denoted by "r")
        with open("data.json", "r") as file:
            self.data = json.load(file)

        # Creates a new frame for the home page
        self.root = tk.Frame(self.root_1, width=370, height=500,
                             bg=self.data["bg_colour"])
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
                                    font=self.title_label_font,
                                    fg=self.data["text_colour"],
                                    bg=self.data["bg_colour"])
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
        self.current_time = datetime.datetime.now()
        # Converts the time using strftime where we are able to denote hours
        # by %H and minutes by %M
        self.current_time = self.current_time.strftime(
            "%H") + ":" + self.current_time.strftime("%M")
        self.new_task_time_var.set(str(self.current_time))
        self.new_task_time = Entry(self.root,
                                   textvariable=self.new_task_time_var,
                                   width=5)
        self.new_task_time.place(x=156, y=75)
        # Date entry
        self.date_var = tk.StringVar()
        # Places the current date into the input field
        self.current_day = datetime.datetime.now()
        # Identifies "locale’s appropriate date representation" (%x)
        self.current_day = self.current_day.strftime("%x")
        self.date_var.set(self.current_day)
        self.data_entry = Entry(self.root, textvariable=self.date_var, width=7)
        self.data_entry.place(x=223, y=75)

        # List (1)
        # Displays all inputted tasks
        self.list_tasks = tk.Listbox(self.root, width=29, height=16,
                                     selectmode='single')
        self.list_tasks.place(x=35, y=125)

        # Buttons (1)
        # Button which adds a task
        self.add_image = ImageTk.PhotoImage(Image.open("/Users/vic"
                                                       "/PycharmProjects"
                                                       "/todo/images/add.png"))
        self.add_task_button = CircleButton(self.root, image=self.add_image,
                                            bg='#ffffff', fg='#000000',
                                            borderless=1,
                                            width=35, command=self.add_task)
        self.add_task_button.place(x=308, y=71)

        # Makes it so the tasks which are stored in data.json show up in the
        # list of the GUI
        for i in self.data["data"]:
            # inserts tasks so that task: name - time date
            self.list_tasks.insert(tk.END, i[0] + " - " + i[1] + " " + i[2])

        # Button which deletes the selected task
        self.delete_selected = Button(self.root, text="Delete", bg='#ffffff',
                                      fg='#000000', borderless=1,
                                      activebackground=('#CD3F5D', '#CD3F5D'),
                                      command=self.delete_selected_func)
        self.delete_selected.place(x=35, y=423)
        # Button which deletes all inputted tasks
        self.delete_all = Button(self.root, text="Delete All", bg='#ffffff',
                                 fg='#000000', borderless=1,
                                 activebackground=('#CD3F5D', '#CD3F5D'),
                                 command=self.delete_all_func)
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
        # Button which opens up the widgets page
        self.widgets_image = ImageTk.PhotoImage(
            Image.open("/Users/vic/PycharmProjects/todo/images/widgets.png"))
        self.widgets_button = CircleButton(self.root,
                                           image=self.widgets_image,
                                           bg='#ffffff', fg='#000000',
                                           borderless=1, width=35,
                                           command=self.widgets)
        self.widgets_button.place(x=268, y=418)

        self.root_1.after(50, self.send_email())

        self.root_1.mainloop()

    # Deletes selected task
    def delete_selected_func(self):
        playsound("/Users/vic/PycharmProjects/todo/audio/delete.mp3")
        # Identifies selected task from listbox
        for i in self.list_tasks.curselection():
            self.data["data"].pop(i)
        # Removes from listbox
        self.list_tasks.delete(tk.ANCHOR)

        # Writing to the JSON file (denoted by the "w") - removing selected
        # task
        with open("data.json", "w") as file:
            json.dump(self.data, file)

    # Deletes all inputted tasks
    def delete_all_func(self):
        playsound("/Users/vic/PycharmProjects/todo/audio/delete_all.mp3")
        # Deletes first task - last task that was inputted
        self.list_tasks.delete("0", "end")
        # Rewrites JSON / makes data section blank
        self.data["data"] = []
        with open("data.json", "w") as file:
            json.dump(self.data, file)

    # Adds task
    def add_task(self):
        playsound("/Users/vic/PycharmProjects/todo/audio/add.mp3")
        # If there is an email inputted
        if self.data["email"]:
            # If the entry task is blank, (\ for syntax purposes)
            if self.new_task_entry_var.get() == "" or \
                    self.new_task_time_var.get() == "" or \
                    self.date_var.get() == "":
                messagebox.showinfo("Invalid Input!",
                                    "An input appears to be blank")
                return
            try:
                # Removes : and / from time and date to make them "simple"
                int(self.new_task_time_var.get().replace(":", ""))
                int(self.date_var.get().replace("/", ""))

                # i  = task name, time, date
                i = ["", self.new_task_time_var.get(),
                     self.date_var.get()]

                # Python lists start at 0
                # e.g. i[2][-2] will go to the second element of JSON which is
                # the date, and take the last 2 numbers ([-2] and [-1])
                # (index)
                year = "20" + i[2][-2] + i[2][-1]
                year = int(year)
                month = i[2][-5] + i[2][-4]
                month = int(month)
                day = i[2][0] + i[2][1]
                day = int(day)
                hour = i[1][0] + i[1][1]
                hour = int(hour)
                minute = i[1][-2] + i[1][-1]
                minute = int(minute)

                date_old = datetime.datetime(year, day, month, hour, minute)

                if datetime.datetime.now() > date_old:
                    messagebox.showinfo("Invalid Input!",
                                        "Inputted time and/or date is before "
                                        "the actual time")
                    return
                else:
                    self.list_tasks.insert(tk.END,
                                           self.new_task_entry_var.get() +
                                           " - " +
                                           self.new_task_time_var.get() + " " +
                                           self.date_var.get())
                    # Appending the added task into the JSON
                    self.data["data"].append([self.new_task_entry_var.get(),
                                              self.new_task_time_var.get(),
                                              self.date_var.get(), "1"])
                    with open("data.json", "w") as file:
                        json.dump(self.data, file)

            except:
                messagebox.showinfo("Invalid Input!",
                                    "Invalid date or time format")
                return

        else:
            messagebox.showinfo("Invalid Input!",
                                "An email has not been inputted. Please do so"
                                "in the preferences menu")

    # Settings page (2)
    def settings(self):
        # Creates a new frame for the preferences page
        self.root = tk.Frame(self.root_1, width=370, height=500,
                             bg=self.data["bg_colour"])
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
                                    font=self.title_label_font,
                                    fg=self.data["text_colour"],
                                    bg=self.data["bg_colour"])
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
                                   font=self.title_label_font,
                                   fg=self.data["text_colour"],
                                   bg=self.data["bg_colour"])
        self.pref_label.place(x=30, y=80)

        # Button which alters the theme and text colour
        # The self.change_bg("bg, text") refers back to the def
        # White background, black text
        self.colour_white = Button(self.root, font="15",
                                   bg='#F4F3F1', fg='#F4F3F1', borderless=1,
                                   width=25, highlightbackground='#2E2F30',
                                   command=lambda: self.change_bg('#F4F3F1',
                                                                  "black"))
        self.colour_white.place(x=35, y=125)
        # Black background, white text
        self.colour_black = Button(self.root, font="15",
                                   bg='#232326', fg='#232326', borderless=1,
                                   width=25,
                                   command=lambda: self.change_bg('#232326',
                                                                  "white"))
        self.colour_black.place(x=65, y=125)
        # Red background, black text
        self.colour_red = Button(self.root, font="15",
                                 bg='#CD3F5D',
                                 fg='#CD3F5D', borderless=1, width=25,
                                 highlightbackground='#CD3F5D',
                                 command=lambda: self.change_bg('#CD3F5D',
                                                                "black"))
        self.colour_red.place(x=95, y=125)
        # Green background, black text
        self.colour_green = Button(self.root, font="15",
                                   bg='#00AD92', fg='#00AD92',
                                   borderless=1,
                                   width=25,
                                   highlightbackground='#00AD92',
                                   command=lambda: self.change_bg(
                                       '#00AD92', "black"))
        self.colour_green.place(x=125, y=125)
        # Blue background, black text
        self.colour_blue = Button(self.root, font="15",
                                  bg='#728EE3', fg='#728EE3',
                                  borderless=1,
                                  width=25,
                                  highlightbackground='#728EE3',
                                  command=lambda: self.change_bg(
                                      '#728EE3', "black"))
        self.colour_blue.place(x=155, y=125)

        # Email
        # Title name and colour - Email
        self.email_label = tk.Label(self.root, text="Email",
                                    font=self.title_label_font,
                                    fg=self.data["text_colour"],
                                    bg=self.data["bg_colour"])
        self.email_label.place(x=30, y=190)
        # Email entry
        self.email_entry_var = tk.StringVar()
        self.email_entry_var.set(self.data["email"])
        self.email_entry = Entry(self.root, textvariable=self.email_entry_var,
                                 width=32)
        self.email_entry.place(x=35, y=235)
        # Button which changes the set email
        self.change = Button(self.root, text="Change", bg='#ffffff',
                             fg='#000000', borderless=1,
                             command=self.change_func)
        self.change.place(x=32, y=285)

        # Help
        # Title name and colour - Help
        self.instructions_label = tk.Label(self.root, text="Help",
                                           font=self.title_label_font,
                                           fg=self.data["text_colour"],
                                           bg=self.data["bg_colour"])
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

    # Changes the theme
    def change_bg(self, background, foreground):
        # Sets position in JSON file to refer to
        self.data["bg_colour"] = background
        self.data["text_colour"] = foreground
        # Writes to JSON file
        with open("data.json", "w") as file:
            json.dump(self.data, file)
        messagebox.showinfo("Done!", "The theme has been altered")
        self.settings()

    # Changes the email
    def change_func(self):
        playsound("/Users/vic/PycharmProjects/todo/audio/add.mp3")
        # If the inputted email is valid
        if validate_email(self.email_entry_var.get()):
            # If the amount of tasks in the list is 0 (denoted by len),
            # proceed to change the email, otherwise, present an error
            # message
            if len(self.data["data"]) == 0:
                self.data["email"] = self.email_entry_var.get()
                with open("data.json", "w") as file:
                    json.dump(self.data, file)
                messagebox.showinfo("Done!",
                                    "Email changed to " +
                                    self.email_entry_var.get())
            else:
                messagebox.showinfo("Error!",
                                    "Please to do not alter the email"
                                    " address when there are active"
                                    " tasks")
                return
        else:
            messagebox.showinfo("Error!", "The email entered is invalid")
            self.settings()

    # Email functionality
    def send_email(self):

        for i in self.data["data"]:
            if bool(int(i[3])):
                year = "20" + i[2][-2] + i[2][-1]
                year = int(year)
                month = i[2][-5] + i[2][-4]
                month = int(month)
                day = i[2][0] + i[2][1]
                day = int(day)
                hour = i[1][0] + i[1][1]
                hour = int(hour)
                minute = i[1][-2] + i[1][-1]
                minute = int(minute)

                date_old = datetime.datetime(year, day, month, hour, minute)

                try:
                    if datetime.datetime.now() > date_old:
                        # SMTP port number: 587
                        self.smtp_session = smtplib.SMTP('smtp.gmail.com', 587)
                        self.smtp_session.starttls()
                        # Mailing address (email and password)
                        self.smtp_session.login("mailtemp025@gmail.com",
                                                "Fluffy15010hi")
                        # Confirmation that email has been sent
                        command = f'''
                                osascript -e 'display notification "
                                {message}" with title "{title}"'
                                '''
                        os.system(command)
                        # Email message sent (f-string)
                        # i[0] refers to the message i[1] refers to th time
                        # i[2] refers to the date, i[3] refers to the
                        # indicator
                        self.message = f"The task '{i[0]}' is due right now"

                        self.smtp_session.sendmail("mailtemp025@gmail.com",
                                                   self.data["email"],
                                                   self.message)

                        self.smtp_session.quit()
                        # Set the 1 to 0 in the data.json to indicate an email
                        # has been sent
                        i[3] = "0"
                        with open("data.json", "w") as file:
                            json.dump(self.data, file)
                # needed to fix syntax issue with 'with'
                except:
                    pass

        self.root.after(50, self.send_email)

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
                            "\n \n 3. Clicking the widgets or settings button "
                            "will open up their respective menus.")

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

    # Widgets page (3)
    def widgets(self):
        # Creates a new Canvas for the widgets page
        self.root = tk.Canvas(self.root_1, width=370, height=500,
                              bg=self.data["bg_colour"], highlightthickness=0)
        self.root.grid(row=0, column=0)

        # Days
        self.week = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
        ]

        # Months
        self.year = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
        ]

        # Calculation to determine what day corresponds to what date in the
        # weekly view
        self.week_days = []
        self.current_day = datetime.datetime.today()
        start = self.current_day.weekday()
        end = 7 - start
        for i in range(-start, end):
            self.week_days.append(
                (self.current_day + datetime.timedelta(days=i)).day)

        # Auto detect location
        self.city = geocoder.ip("me").city

        # OpenWeather API format
        # https://openweathermap.org/current
        self.weatherAPI = "https://api.openweathermap.org/data/2.5/weather?q" \
                          "=" + \
                          self.city + "&appid=" + API_KEY

        # Weather report
        self.weather = requests.get(url=self.weatherAPI).json()
        self.condition = self.weather["weather"][0]["main"]
        # Weather icon
        code = self.weather["weather"][0]["icon"]
        self.weather_image = "/Users/vic/PycharmProjects/todo/" \
                             "weather/" + code + "@2x.png"
        # Weather temperature (-273.15 to convert from kelvin)
        self.celsius = float(self.weather["main"]["temp"])
        self.temperature = math.floor(self.celsius - 273.15)

        # Title (3)
        # Font
        self.title_label_font = Font(
            family="SF Pro Rounded",
            size=20,
            weight="bold"
        )
        # Title name and colour - Widgets
        self.title_label = tk.Label(self.root, text="Widgets",
                                    font=self.title_label_font,
                                    fg=self.data["text_colour"],
                                    bg=self.data["bg_colour"])
        self.title_label.place(x=30, y=35)

        # Buttons (3)
        # Button which returns back to the home page
        self.back_button = Button(self.root, text="Back", bg='#ffffff',
                                  fg='#000000', borderless=1,
                                  command=self.home)
        self.back_button.place(x=3, y=3)

        # Calendar
        # Title name and colour - Calendar
        self.cal_label = tk.Label(self.root, text="Calendar",
                                  font=self.title_label_font,
                                  fg=self.data["text_colour"],
                                  bg=self.data["bg_colour"])
        self.cal_label.place(x=30, y=80)
        self.show_week()

        # Weather
        # Title name and colour - Weather
        self.weather_label = tk.Label(self.root, text="Weather",
                                      font=self.title_label_font,
                                      fg=self.data["text_colour"],
                                      bg=self.data["bg_colour"])
        self.weather_label.place(x=30, y=280)
        self.show_weather()

    # Calendar - weekly view
    def show_week(self):
        # Widget box
        self.root.create_rectangle(
            35, 120, 333, 255, outline="#D7D7D7", width=4, fill="#F0F0F0")

        # Month
        m = self.current_day.month - 1
        self.root.create_text(
            47, 128, text=self.year[m], font=("SF Pro Rounded", 15, "bold"),
            anchor="nw")

        box_size = 38
        border_colour = "#D7D7D7"

        for i in range(7):
            # Monday to Sunday
            self.root.create_text(
                (box_size + box_size * i) + 32, 165, text=self.week[i][0],
                font=("SF Pro Rounded", 15, "bold"))
            # Dates
            self.root.create_text(
                (box_size + box_size * i) + 32, 200,
                text=str(self.week_days[i]),
                font=("SF Pro Rounded", 15, "bold"))
            # Dates boxes
            self.root.create_rectangle(
                (box_size / 2 + box_size * i) + 32, 180,
                (box_size / 2 + box_size + box_size * i) + 32, 180 + box_size,
                outline=border_colour, width=4)

        # Highlight the current box
        self.root.create_rectangle(
            box_size / 2 + box_size * (self.current_day.weekday()) + 32, 180,
            box_size / 2 + box_size + box_size * (
                self.current_day.weekday()) + 32,
            180 + box_size, outline="#CD3F5D", width=4)

    # Current weather
    def show_weather(self):
        # Widget box
        self.root.create_rectangle(
            35, 320, 333, 455, outline="#D7D7D7", width=4, fill="#F0F0F0")

        # Weather adjustments
        self.root.create_text(
            47, 329, text=self.city, font=("SF Pro Rounded", 15, "bold"),
            justify="left", anchor="nw")
        self.root.create_text(
            47, 352, text=str(self.temperature) + "°",
            font=("SF Pro Rounded", 15, "bold"), anchor="nw")
        img = Image.open(self.weather_image)
        self.weather_image = ImageTk.PhotoImage(image=img)
        self.root.create_image(185, 383, image=self.weather_image)
        self.root.create_text(
            185, 420, text=self.condition, font=("SF Pro Rounded", 15, "bold"))


main = ToDo()
main.home()
