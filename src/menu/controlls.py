import customtkinter as ctk
from .config_handler import save_config, restore_to_default, read_config

def controlls_menu(menu_gui, root):
    new_config = menu_gui.config
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    controlls = ctk.CTkFrame(master=root)
    controlls.pack(pady=0, padx=0, fil="both", expand=True)

    def close_controlls_cb():
        menu_gui.open_menu(controlls, menu_gui, root)

    def restore_controls():
        restore_to_default()
        menu_gui.config = read_config()

    def save_current_config():
        # new_config["walk"] = "test"
        save_config(new_config)
        menu_gui.config = read_config()

    go_back = ctk.CTkButton(master=controlls, text="← Go back", fg_color="transparent",
                            border_width=2, command=close_controlls_cb)
    go_back.place(relx=0.04, rely=0.04, anchor="nw")

    header_label = ctk.CTkLabel(master=controlls, text="Controls",
                                font=ctk.CTkFont(size=24, weight="bold"))
    header_label.place(relx=0.04, rely=0.15, anchor="nw")

    # TODO - lista ustawien

    for key, val in new_config.items():
        print(key, val)

    restore_settings = ctk.CTkButton(master=controlls, text="Restore default", fg_color="transparent",
                            border_width=2, command=restore_controls)
    restore_settings.place(relx=0.04, rely=0.96, anchor="sw")

    save = ctk.CTkButton(master=controlls, text="Save", command=save_current_config)
    save.place(relx=0.96, rely=0.96, anchor="se")

    root.mainloop()
