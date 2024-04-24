import customtkinter as ctk

class GUI:
    def __init__(self):
        self.exit_option = None

    def start_program(self, root):
        self.exit_option = "start"
        root.destroy()

def menu():
    gui = GUI()
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    root = ctk.CTk()
    root.geometry("600x400")

    def start_program_cb():
        gui.start_program(root)

    frame = ctk.CTkFrame(master=root)
    frame.pack(pady=0, padx=0, fil="both", expand=True)

    start = ctk.CTkButton(master=frame, text="Start program", command=start_program_cb)
    start.pack(pady=0, padx=0)

    root.mainloop()

    return gui.exit_option
