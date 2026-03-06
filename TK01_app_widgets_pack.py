from tkinter import *
from tkinter import Tk, ttk

from TK00_app_window import create_root_window


# -------------------------------------------------------------------
#                       LABEL / ENTRY / BUTTON
# -------------------------------------------------------------------


def create_widgets(root):

    # label - display text
    name_label = ttk.Label(root, text="Name: ")
    name_label.pack(padx=3, pady=3)

    # entry - input text
    name = ttk.Entry(root, text="")
    name.pack(padx=3, pady=3)

    phone_label = ttk.Label(root, text="Phone: ")
    phone_label.pack(padx=3, pady=3)

    phone = ttk.Entry(root, text="")
    phone.pack(padx=3, pady=3)

    # button
    text = ttk.Button(root, text="Add")
    text.pack(pady=10)


# -------------------------------------------------------------------

if __name__ == "__main__":
    root = create_root_window()
    create_widgets(root)
    root.mainloop()
