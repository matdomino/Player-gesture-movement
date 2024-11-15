import queue
from .calculate_cases import calculate_gesture

def run_keyboard_emulation(keyboard_landmarks_queue, keyboard_config, camera_fps, exit_event):


    while not exit_event.is_set():
        last_action = None
        try:
            left_hand, body = keyboard_landmarks_queue.get(timeout=1)

            

            print(calculate_gesture(left_hand))

        except queue.Empty:
            pass
