import tkinter.messagebox as messagebox
import tkinter as tk
from tkmacosx import Button

root_1 = tk.Tk()
root_1.title('To-do List')
root_1.geometry('370x500+600+75')
root_1.resizable(False, False)


# Help message
def assistance():
    messagebox.showinfo("Done!",
                        "Help \n \n 1. Input a task by specifying a "
                        "title, date and time. To add a task, click the "
                        "+ button. \n \n 2. Once a task has been complete"
                        ", click the delete button; removing it from the "
                        "list \n \n 3. Clicking the settings button will "
                        "open up the preferences menu.")


# Button which opens the help window
done_1 = Button(root_1, text="Assistance", bg='#ffffff',
                fg='#000000', borderless=1, command=assistance)
done_1.place(x=32, y=395)

root_1.mainloop()
