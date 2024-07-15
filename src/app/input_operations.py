from pyautogui import keyUp, keyDown

def hold_key(key):
    keyDown(key)

def release_key(key):
    keyUp(key)

def single_key_press(key, is_pressed):
    if not is_pressed:
        keyDown(key)
        keyUp(key)

def hold_mb(mb, mouse_controller, isPressed):
    if not isPressed:
        mouse_controller.press(mb)

def release_mb(mb, mouse_controller):
    mouse_controller.release(mb)

def single_mb_press(mb, mouse_controller, status):
    if not status:
        mouse_controller.click(mb, 1)
