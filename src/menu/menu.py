import customtkinter as ctk

def menu(gui, root):
    def start_program_cb():
        gui.start_program(root)

    def open_controlls_cb():
        gui.open_controlls(main, gui, root)

    main = ctk.CTkFrame(master=root)
    main.pack(pady=0, padx=0, fil="both", expand=True)

    header_label = ctk.CTkLabel(master=main, text="Webcam player controller",
                                font=ctk.CTkFont(size=24, weight="bold"))
    header_label.place(relx=0.5, rely=0.25, anchor="n")

    start = ctk.CTkButton(master=main, text="Start program", command=start_program_cb)
    start.place(relx=0.5, rely=0.45, anchor="center")

    settings = ctk.CTkButton(master=main, text="Settings", fg_color="transparent",
                            border_width=2, command=open_controlls_cb)
    settings.place(relx=0.5, rely=0.55, anchor="center")

    author = ctk.CTkLabel(master=main, text="Mateusz Domino 2024",
                                font=ctk.CTkFont(size=12, weight="bold"))
    author.place(relx=0.98, rely=1, anchor="se")
