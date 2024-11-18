def hold_key(key, keyboard_controller):
    keyboard_controller.press(key)

def release_key(key, keyboard_controller):
    keyboard_controller.release(key)

def single_key_press(key, keyboard_controller):
    keyboard_controller.press(key)
    keyboard_controller.release(key)

def hold_mb(mb, mouse_controller):
    mouse_controller.press(mb)

def release_mb(mb, mouse_controller):
    mouse_controller.release(mb)

def single_mb_press(mb, mouse_controller, status):
    if not status:
        mouse_controller.click(mb, 1)
