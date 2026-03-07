from tkinter import *
from tkinter import Tk, ttk

from TK00_app_window import create_root_window
from TK02_app_button_command import create_widgets

# -------------------------------------------------------------------
#                       FRAME / GRID LAYOUT
# -------------------------------------------------------------------

# ----------------------------
# row 0, col 0 | row 0, col 1
# ----------------------------
# row 1, col 0 | row 0, col 1
# ----------------------------


def create_grid_frame(root):

    # configure root to take equal weight (fill available space)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # layout frame
    layout = ttk.Frame(root, padding=3)
    layout.grid(row=0, column=0, sticky="nsew")

    # two columns of equal weight (fill available space)
    layout.columnconfigure(0, weight=1)
    layout.columnconfigure(1, weight=1)
    layout.rowconfigure(0, weight=1)

    # -------------------------------------------------------------------
    # column 0 - List of Contacts
    # -------------------------------------------------------------------
    left_frame = ttk.LabelFrame(layout, padding=5, text="Contact List")
    left_frame.grid(row=0, column=0, sticky="nsew", padx=3, pady=3)

    # -------------------------------------------------------------------
    # Column 1 - Add Contact
    # -------------------------------------------------------------------
    right_frame = ttk.LabelFrame(layout, padding=5, text="Add Contact")
    right_frame.grid(row=0, column=1, sticky="nw", padx=3, pady=3)
    right_frame.rowconfigure(0, weight=1)
    right_frame.columnconfigure(0, weight=1)

    return (layout, left_frame, right_frame)


def on_add_button_clicked():
    print(name_var.get())
    print(phone_var.get())


if __name__ == "__main__":

    root = create_root_window()
    layout, left_frame, right_frame = create_grid_frame(root)

    name_var = StringVar()
    phone_var = StringVar()
    create_widgets(right_frame, name_var, phone_var, on_add_button_clicked)
    root.mainloop()
