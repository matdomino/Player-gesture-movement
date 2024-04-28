import customtkinter as ctk

class ControllsGUI:
    def __init__(self):
        self.walk = "w"
        self.jump = " "

    def close_settings(self, root):
        root.destroy()


def controlls_menu(controlls_gui, menu_gui, root):
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    controlls = ctk.CTkFrame(master=root)
    controlls.pack(pady=0, padx=0, fil="both", expand=True)

    def close_controlls_cb():
        menu_gui.open_menu(controlls, menu_gui, root)

    header_label = ctk.CTkLabel(master=controlls, text="Controls",
                                font=ctk.CTkFont(size=24, weight="bold"))
    header_label.place(relx=0.5, rely=0.25, anchor="n")

    settings = ctk.CTkButton(master=controlls, text="Go back to menu", fg_color="transparent",
                            border_width=2, command=close_controlls_cb)
    settings.place(relx=0.5, rely=0.55, anchor="center")

    root.mainloop()
