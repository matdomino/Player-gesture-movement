import customtkinter as ctk
from .controlls import controlls_menu, ControllsGUI
from .menu import menu

class GUI:
    def __init__(self):
        self.exit_option = None

    def start_program(self, root):
        self.exit_option = "start"
        root.destroy()

    def open_menu(self, controlls, gui, root):
        controlls.destroy()
        menu(gui, root)

    def open_controlls(self, main, gui, root):
        main.destroy()
        controlls_gui = ControllsGUI()
        controlls_menu(controlls_gui, gui, root)

def menu_window():
    gui = GUI()
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    root = ctk.CTk()
    root.geometry("600x400")

    menu(gui, root)

    root.mainloop()

    return gui.exit_option
