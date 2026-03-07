from tkinter import *
from tkinter import Tk, ttk

from TK00_app_window import create_root_window


def create_widgets(root, name_var, phone_var, button_clicked):

    # label - display text
    name_label = ttk.Label(root, text="Name: ")
    name_label.pack(padx=3, pady=3, anchor="w")

    # entry - input text
    name = ttk.Entry(root, text="", textvariable=name_var)
    name.pack(padx=3, pady=3, anchor="w")

    phone_label = ttk.Label(root, text="Phone: ")
    phone_label.pack(padx=3, pady=3, anchor="w")

    phone = ttk.Entry(root, text="", textvariable=phone_var)
    phone.pack(padx=3, pady=3, anchor="w")

    # button
    text = ttk.Button(root, text="Add", command=button_clicked)
    text.pack(padx=3, pady=3, anchor="e")


# -------------------------------------------------------------------
#                       Button Event / Command
# -------------------------------------------------------------------


def on_add_button_clicked():
    print(name_var.get())
    print(phone_var.get())


# -------------------------------------------------------------------


if __name__ == "__main__":

    root = create_root_window()

    name_var = StringVar()
    phone_var = StringVar()
    create_widgets(root, name_var, phone_var, on_add_button_clicked)
    root.mainloop()
