# GUI of main window without functionality

import tkinter as tk
from tkinter.font import Font
from tkinter import *
from tkmacosx import Button, CircleButton
from PIL import Image, ImageTk

root = tk.Tk()
root.title('To-do List')
root.geometry('370x500+600+75')
root.resizable(False, False)

# Title (1)
# Font size and weight for the title
title_label_font = Font(
    family="SF Pro Rounded",
    size=20,
    weight="bold"
)
# Title name
title_label = tk.Label(root, text="To-do List",
                       font=title_label_font)
title_label.place(x=30, y=25)

# Inputs (1)
# Task name entry
new_task_entry = Entry(root, width=11)
new_task_entry.place(x=35, y=75)
# Time entry
new_task_entry = Entry(root, width=5)
new_task_entry.place(x=156, y=75)
# Date entry
new_task_entry = Entry(root, width=7)
new_task_entry.place(x=223, y=75)

# List (1)
list_tasks = tk.Listbox(width=29, height=16)
list_tasks.place(x=35, y=125)

# Buttons (1)
# Add task button
add_image = ImageTk.PhotoImage(
    Image.open("/Users/vic/PycharmProjects/todo/images/add.png"))
add_task_button = CircleButton(root, image=add_image, bg='#ffffff',
                               fg='#000000', borderless=1, width=35)
add_task_button.place(x=308, y=71)
# Delete selected task button
delete_selected = Button(root, text="Delete", bg='#ffffff',
                         fg='#000000', borderless=1,
                         activebackground=('#C96666', '#C96666'))
delete_selected.place(x=35, y=423)
# Delete all tasks
delete_all = Button(root, text="Delete all", bg='#ffffff',
                    fg='#000000', borderless=1,
                    activebackground=('#C96666', '#C96666'))
delete_all.place(x=134, y=423)
# Settings button
settings_image = ImageTk.PhotoImage(
    Image.open("/Users/vic/PycharmProjects/todo/images/settings.png"))
settings_button = CircleButton(root, image=settings_image, bg='#ffffff',
                               fg='#000000', borderless=1, width=35)
settings_button.place(x=308, y=418)

root.mainloop()
