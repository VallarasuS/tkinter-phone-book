from tkinter import *
from tkinter import Tk, ttk

# create instance of a window, root window to start with
root = Tk()
root.title("Phone Book")  # sets title to "Phone Book"
root.geometry("800x500")  # sets window width x height to 800 x 500


# -------------------------------------------------------------------
#                       LABEL / ENTRY / BUTTON
# -------------------------------------------------------------------


def on_add_button_clicked():
    print(name.get())
    print(phone.get())


# -------------------------------------------------------------------

name_label = ttk.Label(root, text="Name: ")
name_label.pack(padx=3, pady=3)

name = ttk.Entry(root, text="")
name.pack(padx=3, pady=3)

phone_label = ttk.Label(root, text="Phone: ")
phone_label.pack(padx=3, pady=3)

phone = ttk.Entry(root, text="")
phone.pack(padx=3, pady=3)

# Pass function as reference. NOTE NO '()'
button = ttk.Button(root, text="Add", command=on_add_button_clicked)
button.pack(pady=10)

# call the main loop, displays window and runs the loop till closed.
root.mainloop()
