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

    go_back = ctk.CTkButton(master=controlls, text="Go back", fg_color="transparent",
                            command=close_controlls_cb)
    go_back.place(relx=0.04, rely=0.04, anchor="nw")

    header_label = ctk.CTkLabel(master=controlls, text="Controls",
                                font=ctk.CTkFont(size=24, weight="bold"))
    header_label.place(relx=0.1, rely=0.1, anchor="n")

    restore_settings = ctk.CTkButton(master=controlls, text="Restore default", fg_color="transparent",
                            border_width=2)
    restore_settings.place(relx=0.04, rely=0.96, anchor="sw")

    save = ctk.CTkButton(master=controlls, text="Save")
    save.place(relx=0.96, rely=0.96, anchor="se")

    root.mainloop()
