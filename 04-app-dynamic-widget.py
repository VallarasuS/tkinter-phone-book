from tkinter import *
from tkinter import Tk, ttk
import tkinter.font as tkfont

# create instance of a window, root window to start with
root = Tk()
root.title("Phone Book")  # sets title to "Phone Book"
root.geometry("800x500")  # sets window width x height to 800 x 500

# configure root window to have single column
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


# -------------------------------------------------------------------
#                       WIDGET
# -------------------------------------------------------------------


def createContact(name, phone):
    container = ttk.Frame(list_frame)
    container.pack(fill="x", side="top")

    container.columnconfigure(0, weight=1)
    container.columnconfigure(1, weight=1)

    item = ttk.Label(container, text=phone)
    item.grid(row=0, column=1, sticky="e")

    item = ttk.Label(container, text=name)
    item.grid(row=0, column=0, sticky="w")

    ttk.Separator(list_frame, orient="horizontal").pack(fill="x", pady=5, padx=1)


def addContact():
    createContact(name.get(), phone.get())


# -------------------------------------------------------------------

# layout frame
layout = ttk.Frame(root, padding=3)
layout.grid(row=0, column=0, sticky="nsew")

# two columns of equal weight
layout.columnconfigure(0, weight=1)
layout.columnconfigure(1, weight=1)
layout.rowconfigure(0, weight=1)


# column 0 - List of Contacts

list_frame = ttk.LabelFrame(layout, padding=5, text="Contact List")
list_frame.grid(row=0, column=0, sticky="nsew", padx=3, pady=3)

# Column 1 - Add Contact

formFrame = ttk.LabelFrame(layout, padding=5, text="Add Contact")
formFrame.grid(row=0, column=1, sticky="nw", padx=3, pady=3)
formFrame.rowconfigure(0, weight=1)
formFrame.columnconfigure(0, weight=1)

name_label = ttk.Label(formFrame, text="Name: ")
name_label.pack(anchor="nw", padx=3, pady=3)

name = ttk.Entry(formFrame, text="")
name.pack(anchor="se", padx=3, pady=3)

phone_label = ttk.Label(formFrame, text="Phone: ")
phone_label.pack(anchor="w", padx=3, pady=3)

phone = ttk.Entry(formFrame, text="")
phone.pack(anchor="se", padx=3, pady=3)

text = ttk.Button(formFrame, text="Add", command=addContact)
text.pack(anchor="se", pady=10)

# call the main loop, displays window and runs the loop till closed.
root.mainloop()
