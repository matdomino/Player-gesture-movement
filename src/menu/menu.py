import customtkinter as ctk

class GUI:
    def __init__(self):
        self.exit_option = None

    def start_program(self, root):
        self.exit_option = "start"
        root.destroy()

    def open_settings(self):
        print("test")

def menu():
    gui = GUI()
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    root = ctk.CTk()
    root.geometry("600x400")

    def start_program_cb():
        gui.start_program(root)

    def open_settings_cb():
        gui.open_settings()

    main = ctk.CTkFrame(master=root)
    main.pack(pady=0, padx=0, fil="both", expand=True)

    header_label = ctk.CTkLabel(master=main, text="Webcam player controller",
                                font=ctk.CTkFont(size=24, weight="bold"))
    header_label.place(relx=0.5, rely=0.25, anchor="n")

    start = ctk.CTkButton(master=main, text="Start program", command=start_program_cb)
    start.place(relx=0.5, rely=0.45, anchor="center")

    settings = ctk.CTkButton(master=main, text="Settings", command=open_settings_cb)
    settings.place(relx=0.5, rely=0.55, anchor="center")

    author = ctk.CTkLabel(master=main, text="Mateusz Domino 2024",
                                font=ctk.CTkFont(size=12, weight="bold"))
    author.place(relx=0.98, rely=1, anchor="se")

    root.mainloop()

    return gui.exit_option
