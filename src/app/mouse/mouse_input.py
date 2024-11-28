def hold_mb(mb, mouse_controller) -> None:
    """
    Emulates a mouse button press and holds it until released.

        Parameters:
            - mb(enum Button): The mouse button to press.
            - mouse_controller(Controller): Mouse controler (Pynput).

        Returns:
            - None
    """

    mouse_controller.press(mb)

def release_mb(mb, mouse_controller) -> None:
    """
    Releases the previously pressed mouse button.

        Parameters:
            - mb(enum Button): The mouse button to release.
            - mouse_controller(Controller): Mouse controler (Pynput).

        Returns:
            - None
    """

    mouse_controller.release(mb)

def single_mb_press(mb, mouse_controller, status) -> None:
    """
    Simulates a single mouse button press.

        Parameters:
            - mb(enum Button): The mouse button to press.
            - mouse_controller(Controller): Mouse controler (Pynput).

        Returns:
            - None
    """

    if not status:
        mouse_controller.click(mb, 1)
