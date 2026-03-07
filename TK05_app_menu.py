from tkinter import *
from tkinter import Tk, ttk

from TK00_app_window import create_root_window
from TK02_app_button_command import create_widgets
from TK03_app_grid_frame import create_grid_frame
from TK04_app_dynamic_widget import create_contact_item

# -------------------------------------------------------------------
#                       MENU
# -------------------------------------------------------------------


def create_menu(root):

    def quit():
        root.quit()

    # Create and attach Menubar to window
    menu = Menu(root)
    root.config(menu=menu)

    # Create top level File Menu
    file = Menu(menu, tearoff=0)
    menu.add_cascade(label="File", menu=file)

    edit = Menu(menu, tearoff=0)
    menu.add_cascade(label="Edit", menu=edit)

    about = Menu(menu, tearoff=0)
    menu.add_cascade(label="About", menu=about)

    # Create commands under File
    file.add_command(label="Import")
    file.add_command(label="Export")
    file.add_separator()
    file.add_command(label="Quit", command=quit)


# -------------------------------------------------------------------


if __name__ == "__main__":

    root = create_root_window()
    layout, left, right = create_grid_frame(root)
    create_menu(root)

    name_var = StringVar()
    phone_var = StringVar()

    def on_add_button_clicked():
        create_contact_item(left, name_var.get(), phone_var.get())

    create_widgets(right, name_var, phone_var, on_add_button_clicked)
    root.mainloop()
