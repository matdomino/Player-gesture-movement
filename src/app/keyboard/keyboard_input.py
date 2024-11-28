def hold_key(key, keyboard_controller):
    """
    Emulates a key press until it's released.

        Parameters:
            - key(enum Key): The key to press.
            - keyboard_controller(Controller): Keyboard controler (Pynput).

        Returns:
            - None
    """

    keyboard_controller.press(key)

def release_key(key, keyboard_controller):
    """
    Releases the previously pressed key.

        Parameters:
            - key(enum Key): The key to release.
            - keyboard_controller(Controller): Keyboard controller (Pynput).

        Returns:
            - None
    """

    keyboard_controller.release(key)

def single_key_press(key, keyboard_controller):
    """
    Simulates pressing and releasing a key once.

        Parameters:
            - key(enum Key): The key to press and release.
            - keyboard_controller(Controller): Keyboard controller (Pynput).

        Returns:
            - None
    """

    keyboard_controller.press(key)
    keyboard_controller.release(key)
