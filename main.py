from src.menu.menu_window import menu_window

def main():
    option = menu_window()

    if option == "start":
        print("start")
    else:
        return

if __name__ == "__main__":
    main()
