from tkinter import *
from tkinter import Tk, ttk

# create instance of a window, root window to start with
root = Tk()
root.title("Phone Book")  # sets title to "Phone Book"
root.geometry("800x500")  # sets window width x height to 800 x 500

# -------------------------------------------------------------------
#                       LABEL / ENTRY / BUTTON
# -------------------------------------------------------------------

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

# call the main loop, displays window and runs the loop till closed.
root.mainloop()
