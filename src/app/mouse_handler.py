from pyautogui import moveRel

def move_mouse(coords, old_coords, sensitivity):
    if old_coords != None:
        diff = (old_coords[0] - coords[0], old_coords[1] - coords[1])

        new_x = diff[0]
        new_y = diff[1]
        if abs(new_x) > 0.005 or abs(new_y) > 0.005:
            new_x = int(new_x * 100 * sensitivity)
            new_y = int(new_y * 100 * sensitivity * -1)

            moveRel(new_x, new_y)


def emulate_mouse(landmarks, old_landmarks): # pozniej to w watku przechowywac

    try:
        if len(landmarks) > 1:
            right_hand = landmarks[0]
            left_hand = landmarks[1]

            if right_hand.landmark[0].x > left_hand.landmark[0].x:
                right_hand, left_hand = left_hand, right_hand

            move_mouse((right_hand.landmark[0].x, right_hand.landmark[0].y), old_landmarks, 50)


        else:
            raise ValueError("Brak wykrytych dłoni")

        return (right_hand.landmark[0].x, right_hand.landmark[0].y)

    except:
        pass