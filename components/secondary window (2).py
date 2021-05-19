# GUI of secondary window without functionality

import tkinter as tk
from tkinter.font import Font
from tkinter import *
from tkmacosx import Button

root_1 = tk.Tk()
root_1.title('To-do List')
root_1.geometry('370x500+600+75')
root_1.resizable(False, False)

# Button which returns back to the main page
back_button = Button(root_1, text="Back", bg='#ffffff',
                     fg='#000000', borderless=1)
back_button.place(x=3, y=3)

# Title (2)
# Font size and weight of title
title_label_font = Font(
    family="SF Pro Rounded",
    size=20,
    weight="bold"
)
# Title name - Preferences
title_label = tk.Label(root_1, text="Preferences",
                       font=title_label_font)
title_label.place(x=30, y=35)

# Themes
# Title name - Themes
pref_label = tk.Label(root_1, text="Themes",
                      font=title_label_font)
pref_label.place(x=30, y=80)
# White background, black text
colour_white = Button(root_1, text="   ", font="15",
                      bg='#F4F3F1', fg='#F4F3F1', borderless=1,
                      width=25, highlightbackground='#2E2F30')

colour_white.place(x=35, y=125)
# Black background, white text
colour_black = Button(root_1, text="   ", font="15",
                      bg='#2E2F30', fg='#2E2F30', borderless=1,
                      width=25)
colour_black.place(x=65, y=125)
# Red background, black text
colour_red = Button(root_1, text="   ", font="15",
                    bg='#C96666',
                    fg='#C96666', borderless=1, width=25,
                    highlightbackground='#C96666')
colour_red.place(x=95, y=125)
# Green background, black text
colour_green = Button(root_1, text="   ", font="15",
                      bg='#B0D8B5', fg='#B0D8B5',
                      borderless=1,
                      width=25)
colour_green.place(x=125, y=125)
# Blue background, black text
colour_blue = Button(root_1, text="   ", font="15",
                     bg='#A7C8D4', fg='#A7C8D4',
                     borderless=1,
                     width=25)
colour_blue.place(x=155, y=125)

# Title name and colour - Email
email_label = tk.Label(root_1, text="Email",
                       font=title_label_font)
email_label.place(x=30, y=190)

# Email entry
email_entry_var = tk.StringVar()
email_entry = Entry(root_1, textvariable=email_entry_var,
                    width=32)
email_entry.place(x=35, y=235)

# Button which changes the set email
done = Button(root_1, text="Change", bg='#ffffff',
              fg='#000000', borderless=1)
done.place(x=32, y=285)

# Help
# Title name and colour - Help
assistance_label = tk.Label(root_1, text="Help",
                            font=title_label_font)
assistance_label.place(x=30, y=350)

# Button which opens the help window
done_1 = Button(root_1, text="Assistance", bg='#ffffff',
                fg='#000000', borderless=1)
done_1.place(x=32, y=395)

root_1.mainloop()
