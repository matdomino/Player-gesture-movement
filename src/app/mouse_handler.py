from pynput.mouse import Controller, Button
from .input_operations import single_mb_press
from .calculate_cases import index_finger_up, peace_sign, three_fingers_up, four_fingers_up, open_palm

def move_mouse(coords, old_coords, controller, sensitivity):
    if old_coords != None:
        diff = (old_coords[0] - coords[0], old_coords[1] - coords[1])

        new_x = diff[0]
        new_y = diff[1]
        if abs(new_x) > 0.005 or abs(new_y) > 0.005:
            new_x = int(new_x * 100 * sensitivity)
            new_y = int(new_y * 100 * sensitivity * -1)

            controller.move(new_x, new_y)

def emulate_mouse(right_hand, old_landmarks): # pozniej to w watku przechowywac
    mouse_controller = Controller()

    if open_palm(right_hand):
        move_mouse((right_hand.landmark[0].x, right_hand.landmark[0].y), old_landmarks, mouse_controller, 50)

        return (right_hand.landmark[0].x, right_hand.landmark[0].y)

    if index_finger_up(right_hand): # POJEDYNCZO LEWY
        single_mb_press(Button.left, mouse_controller, False)
        return (right_hand.landmark[0].x, right_hand.landmark[0].y)

    if peace_sign(right_hand): # TRZYMANIE LEWEGO PRZYCISKU MYSZKI
        move_mouse((right_hand.landmark[0].x, right_hand.landmark[0].y), old_landmarks, mouse_controller, 50)

        return (right_hand.landmark[0].x, right_hand.landmark[0].y)

    if three_fingers_up(right_hand): # POJEDYNCZO PRAWY
        single_mb_press(Button.right, mouse_controller, False)
        return (right_hand.landmark[0].x, right_hand.landmark[0].y)

    if four_fingers_up(right_hand): # PRZYTRZYMANIE PRAWY
        move_mouse((right_hand.landmark[0].x, right_hand.landmark[0].y), old_landmarks, mouse_controller, 50)

        return (right_hand.landmark[0].x, right_hand.landmark[0].y)
