from tkinter import *
from tkinter import Tk, ttk

from TK00_app_window import create_root_window
from TK02_app_button_command import create_widgets
from TK03_app_grid_frame import create_grid_frame
from TK04_app_dynamic_widget import create_contact_item
from TK05_app_menu import create_menu

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


if __name__ == "__main__":

    root = create_root_window()
    create_menu(root)

    root, left, right = create_grid_frame(root)

    name_var = StringVar()
    phone_var = StringVar()

    def on_add_button_clicked():
        create_contact_item(left, name_var.get(), phone_var.get())

    create_widgets(right, name_var, phone_var, on_add_button_clicked)
    root.mainloop()
