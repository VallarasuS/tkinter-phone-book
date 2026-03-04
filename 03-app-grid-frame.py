from tkinter import *
from tkinter import Tk, ttk
import tkinter.font as tkfont

# create instance of a window, root window to start with
root = Tk()
root.title("Phone Book")  # sets title to "Phone Book"
root.geometry("800x500")  # sets window width x height to 800 x 500


def on_add_button_clicked():
    print(name.get())
    print(phone.get())


# configure root window to take equal weight (fill available space)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# -------------------------------------------------------------------
#                       FRAME / GRID LAYOUT
# -------------------------------------------------------------------

# ----------------------------
# row 0, col 0 | row 0, col 1
# ----------------------------
# row 1, col 0 | row 0, col 1
# ----------------------------

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
list_frame = ttk.LabelFrame(layout, padding=5, text="Contact List")
list_frame.grid(row=0, column=0, sticky="nsew", padx=3, pady=3)

# -------------------------------------------------------------------
# Column 1 - Add Contact
# -------------------------------------------------------------------
formFrame = ttk.LabelFrame(layout, padding=5, text="Add Contact")
formFrame.grid(row=0, column=1, sticky="nw", padx=3, pady=3)
formFrame.rowconfigure(0, weight=1)
formFrame.columnconfigure(0, weight=1)

# -------------------------------------------------------------------

name_label = ttk.Label(formFrame, text="Name: ")
name_label.pack(anchor="nw", padx=3, pady=3)

name = ttk.Entry(formFrame, text="")
name.pack(anchor="se", padx=3, pady=3)

phone_label = ttk.Label(formFrame, text="Phone: ")
phone_label.pack(anchor="w", padx=3, pady=3)

phone = ttk.Entry(formFrame, text="")
phone.pack(anchor="se", padx=3, pady=3)

text = ttk.Button(formFrame, text="Add", command=on_add_button_clicked)
text.pack(anchor="se", pady=10)

# call the main loop, displays window and runs the loop till closed.
root.mainloop()
