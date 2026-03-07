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


def create_contact_item(root, name, phone):
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


if __name__ == "__main__":

    root = create_root_window()
    root, left, right = create_grid_frame(root)

    # -------------------------------------------------------------------
    #                       VARIABLE
    # -------------------------------------------------------------------
    name_var = StringVar()
    phone_var = StringVar()

    # -------------------------------------------------------------------

    def on_add_button_clicked():
        create_contact_item(left, name_var.get(), phone_var.get())

    create_widgets(right, name_var, phone_var, on_add_button_clicked)
    root.mainloop()
