import queue
from collections import deque
from .calculate_cases import calculate_gesture, calculate_joint_angle
from .input_operations import hold_key, release_key, single_key_press

def left_hand_single_action(gesture, last_hand_gesture, keyboard_config):
    if gesture == last_hand_gesture:
        return

    match gesture:
        case "four_fingers_up":
            single_key_press(keyboard_config['l-four-up'])
        case "index_finger_up":
            single_key_press(keyboard_config['l-index-up'])
        case "peace_sign":
            single_key_press(keyboard_config['l-peace'])
        case "three_fingers_up":
            single_key_press(keyboard_config['l-three-up'])
        case _:
            return

def walk(body_landmarks, walking_history_queue, walking_queue_length, keyboard_config):
    if (calculate_joint_angle(body_landmarks[26], body_landmarks[24], body_landmarks[12]) < 140 or
        calculate_joint_angle(body_landmarks[25], body_landmarks[23], body_landmarks[11]) < 140):

        walking_history_queue.extend([1] * walking_queue_length)
        hold_key(keyboard_config['Walk'])

    try:
        walking_history_queue.popleft()

    except IndexError:
        release_key(keyboard_config['Walk'])


def run_keyboard_emulation(keyboard_landmarks_queue, keyboard_config, camera_fps, exit_event):
    last_hand_gesture = None
    walking_queue_length = int(camera_fps/4)
    walking_history_queue = deque(maxlen=walking_queue_length) # kolejka na 1/4 sekundy w zaleznosci od fps kamery

    while not exit_event.is_set():
        try:
            left_hand, body = keyboard_landmarks_queue.get(timeout=1)

            # Lewa reka pojedyncze gesty 
            hand_gesture = calculate_gesture(left_hand)
            left_hand_single_action(hand_gesture, last_hand_gesture, keyboard_config)

            # Otwarta dlon?? - moze przytrzymanie shift?
            ...

            # Pochylenie lewo-prawo - chodzenie w boki
            ...

            # Chodzenie do przodu
            walk(body, walking_history_queue, walking_queue_length, keyboard_config)

            # Skok - tutaj po prostu zrobic funkcje ktora sprawdzi czy nogi sa naraz pochylone odpowiednio
            ...

            last_hand_gesture = hand_gesture

        except queue.Empty:
            pass
