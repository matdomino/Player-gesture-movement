import customtkinter as ctk
from .controlls import controlls_menu
from .menu import menu
from .config_handler import read_config

class GUI:
    def __init__(self, config):
        self.exit_option = None
        self.config = config

    def start_program(self, root):
        self.exit_option = "start"
        root.destroy()

    def open_menu(self, controlls, gui, root):
        controlls.destroy()
        menu(gui, root)

    def open_controlls(self, main, gui, root):
        main.destroy()
        controlls_menu(gui, root)

def menu_window():
    config = read_config()
    gui = GUI(config)
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    root = ctk.CTk()
    root.geometry("600x400")

    menu(gui, root)

    root.mainloop()

    return gui.exit_option
