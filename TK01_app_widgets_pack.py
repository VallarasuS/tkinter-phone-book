from tkinter import *
from tkinter import Tk, ttk

from TK00_app_window import create_root_window


# -------------------------------------------------------------------
#                       LABEL / ENTRY / BUTTON
# -------------------------------------------------------------------


def create_widgets(root):

    # label - display text
    name_label = ttk.Label(root, text="Name: ")
    name_label.pack(padx=3, pady=3, anchor="w")

    # entry - input text
    name = ttk.Entry(root, text="")
    name.pack(padx=3, pady=3, anchor="w")

    phone_label = ttk.Label(root, text="Phone: ")
    phone_label.pack(padx=3, pady=3, anchor="w")

    phone = ttk.Entry(root, text="")
    phone.pack(padx=3, pady=3, anchor="w")

    # button
    text = ttk.Button(root, text="Add")
    text.pack(padx=10, pady=10, anchor="e")


# -------------------------------------------------------------------

if __name__ == "__main__":
    root = create_root_window()
    create_widgets(root)
    root.mainloop()
