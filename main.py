from src.menu.menu_window import menu_window
from src.app.pose_detection import pose_detection

def main():
    option = menu_window()

    if option == "start":
        pose_detection()
    else:
        return

if __name__ == "__main__":
    #main()

    pose_detection()
