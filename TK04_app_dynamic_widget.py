from tkinter import *
from tkinter import Tk, ttk

from TK00_app_window import create_root_window
from TK02_app_button_command import create_widgets
from TK03_app_grid_frame import create_grid_frame

# -------------------------------------------------------------------
#                       WIDGET
# -------------------------------------------------------------------

# -----------------------
#   Name     |  Phone
# -----------------------


def createContact(root, name, phone):
    contact_container = ttk.Frame(root)
    contact_container.pack(fill="x", side="top")

    # column 0, column 1 for name & phone
    contact_container.columnconfigure(0, weight=1)
    contact_container.columnconfigure(1, weight=1)

    # name
    item = ttk.Label(contact_container, text=name)
    item.grid(row=0, column=0, sticky="w")

    # phone
    item = ttk.Label(contact_container, text=phone)
    item.grid(row=0, column=1, sticky="e")

    # Separator - Horizontal Line
    ttk.Separator(root, orient="horizontal").pack(fill="x", pady=5, padx=1)


# todo: create a string var, pass ref
def addContact(root):
    createContact(root, name.get(), phone.get())


if __name__ == "__main__":

    root = create_root_window()
    root, left_frame, right_frame = create_grid_frame(root)
    create_widgets(right_frame)
    addContact(left_frame)
    root.mainloop()
