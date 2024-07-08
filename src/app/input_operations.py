from pyautogui import keyUp, keyDown, click, mouseDown, mouseUp

def hold_key(key):
    keyDown(key)

def release_key(key):
    keyUp(key)

def single_key_press(key, is_pressed):
    if not is_pressed:
        keyDown(key)
        keyUp(key)

def hold_mb(mb, release):
    if not release:
        mouseDown(button=mb)
    else:
        mouseUp(button=mb)

def single_mb_press(mb, status):
    if not status:
        click(button=mb)

def move_mouse(mouseobj, curr_x, curr_y, old_x, old_y, speed):
    x_difference = abs(curr_x - old_x)
    y_difference = abs(curr_y - old_y)

    if x_difference > 0.01:
        if curr_x < old_x:
            mouseobj.move(10 * speed, 0)
        elif curr_x > old_x:
            mouseobj.move(-10 * speed, 0)

    if y_difference > 0.01:
        if curr_y < old_y:
            mouseobj.move(0, -10 * speed)
        elif curr_y > old_y:
            mouseobj.move(0, 10 * speed)
