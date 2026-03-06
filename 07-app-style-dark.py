from tkinter import *
from tkinter import Tk, ttk
import tkinter.font as tkfont


def create_window():
    # create instance of a window, root window to start with
    root = Tk()
    root.title("Phone Book")  # sets title to "Phone Book"
    root.geometry("800x500")  # sets window width x height to 800 x 500

    # configure root window to have single column
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    return root


def quit():
    root.quit()


def build_menu(parent):
    menu = Menu(parent)
    parent.config(menu=menu)

    file = Menu(menu, tearoff=0)
    menu.add_cascade(label="File", menu=file)

    file.add_command(label="Import")
    file.add_command(label="Export")
    file.add_command(label="Quit", command=quit)

    edit = Menu(menu, tearoff=0)
    menu.add_cascade(label="Edit", menu=edit)

    about = Menu(menu, tearoff=0)
    menu.add_cascade(label="About", menu=about)


def create_form_widget(parent):
    name_label = ttk.Label(parent, text="Name: ", style="Dark.TLabel")
    name_label.pack(anchor="nw", padx=3, pady=3)

    name = ttk.Entry(parent, text="", textvariable=nameVar)
    name.pack(anchor="se", padx=3, pady=3)

    phone_label = ttk.Label(parent, text="Phone: ", style="Dark.TLabel")
    phone_label.pack(anchor="w", padx=3, pady=3)

    phone = ttk.Entry(parent, text="", textvariable=phoneVar)
    phone.pack(anchor="se", padx=3, pady=3)

    text = ttk.Button(parent, text="Add", command=addContact, style="Bright.TButton")
    text.pack(anchor="se", pady=10)


def createContact(parent, name, phone):
    container = ttk.Frame(parent, style="InLineDark.TFrame")
    container.pack(fill="x", side="top")

    container.columnconfigure(0, weight=1)
    container.columnconfigure(1, weight=1)

    item = ttk.Label(container, text=phone, style="Dark.TLabel")
    item.grid(row=0, column=1, sticky="e")

    item = ttk.Label(container, text=name, style="Dark.TLabel")
    item.grid(row=0, column=0, sticky="w")

    ttk.Separator(parent, orient="horizontal").pack(fill="x", pady=5, padx=1)


def create_root_layout():
    # layout frame
    layout = ttk.Frame(root, padding=3, style="Dark.TFrame")
    layout.grid(row=0, column=0, sticky="nsew")

    # two columns of equal weight
    layout.columnconfigure(0, weight=1)
    layout.columnconfigure(1, weight=1)
    layout.rowconfigure(0, weight=1)
    return layout


def addContact():
    createContact(list_frame, nameVar.get(), phoneVar.get())


root = create_window()
build_menu(root)
layout = create_root_layout()

# column 0 - List of Contacts
list_frame = ttk.LabelFrame(
    layout, padding=5, text="Contact List", style="Dark.TLabelframe"
)
list_frame.grid(row=0, column=0, sticky="nsew", padx=3, pady=3)

# Column 1 - Add Contact
formFrame = ttk.LabelFrame(
    layout, padding=5, text="Add Contact", style="Dark.TLabelframe"
)
formFrame.grid(row=0, column=1, sticky="nw", padx=3, pady=3)
formFrame.rowconfigure(0, weight=1)
formFrame.columnconfigure(0, weight=1)


nameVar = StringVar()
phoneVar = StringVar()

# -------------------------------------------------------------------
#                       STYLES
# -------------------------------------------------------------------

style = ttk.Style()
style.configure("Dark.TFrame", background="#000000")
style.configure("Bright.TButton", background="#FFD45A", foreground="#FF0000")

style.configure("Dark.TLabelframe", background="#16181c", bordercolor="#00ff9d")
style.configure("Dark.TLabelframe.Label", background="#16181c", foreground="#e7e9ea")
style.configure("InLineDark.TFrame", background="#16181c")


style.configure("Dark.TLabel", background="#16181c", foreground="#e7e9ea")

# -------------------------------------------------------------------

create_form_widget(formFrame)

# call the main loop, displays window and runs the loop till closed.
root.mainloop()
