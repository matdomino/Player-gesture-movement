from pynput.mouse import Controller

def emulate_mouse(landmarks):
    mouse = Controller()

    try:
        if len(landmarks) > 1:
            right_hand = landmarks[0]
            left_hand = landmarks[1]

            if right_hand.landmark[0].x > left_hand.landmark[0].x:
                right_hand, left_hand = left_hand, right_hand

        else:
            raise ValueError("Brak wykrytych dłoni")

    except:
        pass