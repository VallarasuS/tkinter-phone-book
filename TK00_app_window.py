from tkinter import *
from tkinter import Tk

# -------------------------------------------------------------------
#                       WINDOW / SHELL / ROOT
# -------------------------------------------------------------------


def create_root_window():

    # create instance of a window, root window to start with
    root = Tk()
    root.title("Phone Book")  # sets title to "Phone Book"
    root.geometry("800x500")  # sets window width x height to 800 x 500

    return root


# prevent running when imported
if __name__ == "__main__":
    root = create_root_window()
    root.mainloop()  # call the main loop, displays window.

# -------------------------------------------------------------------
