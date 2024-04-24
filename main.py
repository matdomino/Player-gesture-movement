from src.menu import menu

def main():
    option = menu()

    if option == "start":
        print("start")
    else:
        return

if __name__ == "__main__":
    main()
