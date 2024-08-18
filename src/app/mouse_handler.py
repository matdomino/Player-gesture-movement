from pynput.mouse import Controller, Button
import queue
from .input_operations import single_mb_press, hold_mb, release_mb
from .calculate_cases import index_finger_up, peace_sign, three_fingers_up, four_fingers_up, open_palm

def clear_queue(queue, amount):
    for _ in range(amount):
        if not queue.empty():
            queue.get()

def segment_pointer_move(new_x, new_y, roughness_ratio, segments_queue):
    x_segment = 0
    y_segment = 0

    if new_x >= 0:
        x_segment = new_x // (10 - roughness_ratio) if new_x >= (10 - roughness_ratio) else 1
    else:
        x_segment = new_x // (10 - roughness_ratio) if (new_x * -1) >= (10 - roughness_ratio) else -1

    if new_y >= 0:
        y_segment = new_y // (10 - roughness_ratio) if new_y >= (10 - roughness_ratio) else 1
    else:
        y_segment = new_y // (10 - roughness_ratio) if (new_y * -1) >= (10 - roughness_ratio) else -1

    for _ in range(10 - roughness_ratio):
        new_x_abs = abs(new_x)
        new_y_abs = abs(new_y)
        x_segment_abs = abs(x_segment)
        y_segment_abs = abs(y_segment)

        if new_x_abs >= x_segment_abs and new_y_abs >= y_segment:
            segments_queue.put((x_segment, y_segment))

            new_x_abs -= x_segment_abs
            new_y_abs -= y_segment_abs
            continue

        if new_x_abs >= x_segment_abs and new_y_abs <= y_segment_abs:
            if new_y_abs > 0:
                segments_queue.put((x_segment, new_y))
            else:
                segments_queue.put((x_segment, 0))

            new_x_abs -= x_segment_abs
            new_y_abs = 0
            continue

        if new_x_abs <= x_segment_abs and new_y_abs >= y_segment_abs:
            if new_x_abs > 0:
                segments_queue.put((new_x, y_segment))
            else:
                segments_queue.put((0, y_segment))

            new_y_abs -= y_segment_abs
            new_x_abs = 0
            continue

    return roughness_ratio

def calculate_pointer_move(coords, old_coords, segments_queue, sensitivity):
    if old_coords != None:
        diff = (old_coords[0] - coords[0], old_coords[1] - coords[1])
        new_x = diff[0]
        new_y = diff[1]

        if abs(new_x) > 0.005 or abs(new_y) > 0.005:
            new_x = int(new_x * 100 * sensitivity)
            new_y = int(new_y * 100 * sensitivity * -1)

            frame_rate = 240
            queue_limit = frame_rate * 2
            roughness_ratio = 0

            roughness_ratio = segment_pointer_move(new_x, new_y, roughness_ratio, segments_queue)

            if segments_queue.qsize() > queue_limit:
                clear_queue(segments_queue, frame_rate)
                roughness_ratio += 1
            else:
                if roughness_ratio > 0:
                    roughness_ratio -= 1

def release_last(last_option, mouse_controller):
    if last_option == "peace_sign":
        release_mb(Button.left, mouse_controller)
        return

    if last_option == "four_fingers_up":
        release_mb(Button.right, mouse_controller)
        return

def emulate_mouse(right_hand, old_landmarks, mouse_controller, last_mouse_option, segments_queue):
    if open_palm(right_hand): # RUSZANIE KURSOREM
        release_last(last_mouse_option, mouse_controller)

        calculate_pointer_move((right_hand.landmark[0].x, right_hand.landmark[0].y), old_landmarks, segments_queue, 50)

        return (right_hand.landmark[0].x, right_hand.landmark[0].y), None

    if four_fingers_up(right_hand): # TRZYMANIE PRAWEGO PRZCISKU MYSZKI
        if last_mouse_option == "peace_sign":
            release_mb(Button.left, mouse_controller)

        calculate_pointer_move((right_hand.landmark[0].x, right_hand.landmark[0].y), old_landmarks, segments_queue, 50)
        hold_mb(Button.right, mouse_controller, last_mouse_option=="four_fingers_up")

        return (right_hand.landmark[0].x, right_hand.landmark[0].y), "four_fingers_up"

    if index_finger_up(right_hand): # POJEDYNCZO LEWY
        release_last(last_mouse_option, mouse_controller)
        single_mb_press(Button.left, mouse_controller, last_mouse_option == "index_finger_up")
        return (right_hand.landmark[0].x, right_hand.landmark[0].y), "index_finger_up"

    if peace_sign(right_hand): # TRZYMANIE LEWEGO PRZYCISKU MYSZKI
        if last_mouse_option == "four_fingers_up":
            release_mb(Button.right, mouse_controller)

        calculate_pointer_move((right_hand.landmark[0].x, right_hand.landmark[0].y), old_landmarks, segments_queue, 50)
        hold_mb(Button.left, mouse_controller, last_mouse_option=="peace_sign")

        return (right_hand.landmark[0].x, right_hand.landmark[0].y), "peace_sign"

    if three_fingers_up(right_hand): # POJEDYNCZO PRAWY
        release_last(last_mouse_option, mouse_controller)
        single_mb_press(Button.right, mouse_controller, last_mouse_option == "three_fingers_up")
        return (right_hand.landmark[0].x, right_hand.landmark[0].y), "three_fingers_up"

    return None, last_mouse_option

def run_mouse_emulation(mouse_landmarks_queue, segments_queue, exit_event):
    mouse_controller = Controller()
    old_landmarks = None
    last_mouse_option = None

    while not exit_event.is_set():
        try:
            landmarks = mouse_landmarks_queue.get(timeout=1)
            landmarks_tmp, last_mouse_option = emulate_mouse(landmarks, old_landmarks, mouse_controller, last_mouse_option, segments_queue)

            if landmarks_tmp is not None:
                old_landmarks = landmarks_tmp

        except queue.Empty:
            pass

    release_mb(Button.left, mouse_controller)
    release_mb(Button.right, mouse_controller)
