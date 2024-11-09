import queue
from .calculate_cases import calculate_gesture

def clear_queue(queue, amount):
    for _ in range(amount):
        if not queue.empty():
            queue.get()

def add_to_pointer_queue(move_vector, action, roughness_ratio, segments_queue):
    new_x = move_vector[0]
    new_y = move_vector[1]
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
            segments_queue.put((x_segment, y_segment, action))

            new_x_abs -= x_segment_abs
            new_y_abs -= y_segment_abs
            continue

        if new_x_abs >= x_segment_abs and new_y_abs <= y_segment_abs:
            if new_y_abs > 0:
                segments_queue.put((x_segment, new_y, action))
            else:
                segments_queue.put((x_segment, 0, action))

            new_x_abs -= x_segment_abs
            new_y_abs = 0
            continue

        if new_x_abs <= x_segment_abs and new_y_abs >= y_segment_abs:
            if new_x_abs > 0:
                segments_queue.put((new_x, y_segment, action))
            else:
                segments_queue.put((0, y_segment, action))

            new_y_abs -= y_segment_abs
            new_x_abs = 0
            continue

def calculate_pointer_move(coords, old_coords, sensitivity):
    if old_coords[0] is None:
        return ((coords[0], coords[1]), (None, None))

    diff = (old_coords[0] - coords[0], old_coords[1] - coords[1])
    move_x = diff[0]
    move_y = diff[1]

    if abs(move_x) > 0.005 or abs(move_y) > 0.005:
        move_x = int(move_x * 100 * sensitivity)
        move_y = int(move_y * 100 * sensitivity * -1)

        return ((coords[0], coords[1]), (move_x, move_y))

    return ((coords[0], coords[1]), (None, None))

mouse_actions = {
    None: None,
    "open_palm": None,
    "four_fingers_up": "r_hold",
    "index_finger_up": "l_single",
    "peace_sign": "l_hold",
    "three_fingers_up": "r_single"
}

def emulate_mouse(segments_queue, right_hand, old_landmarks, roughness_ratio, sensitivity):
    gesture = calculate_gesture(right_hand)
    action = mouse_actions[gesture]

    current_pos, move_vector = calculate_pointer_move((right_hand.landmark[0].x, right_hand.landmark[0].y),
                                            old_landmarks, sensitivity)

    if action in ["index_finger_up", "three_fingers_up"]:
        segments_queue.put((None, None, action))

    if current_pos[0] is not None and move_vector[0] is not None:
        add_to_pointer_queue(move_vector, action, roughness_ratio, segments_queue)

    if gesture is None:
        return (None, None)

    return current_pos

def run_mouse_emulation(mouse_landmarks_queue, segments_queue, mouse_config, exit_event):
    old_landmarks = (None, None)
    roughness_ratio = 0
    loop_iterator = 0

    frame_rate = mouse_config.get('pointer-refresh-rate')
    queue_limit = frame_rate * 2

    while not exit_event.is_set():
        try:
            landmarks = mouse_landmarks_queue.get(timeout=1)

            old_landmarks = emulate_mouse(segments_queue, landmarks,
                        old_landmarks, roughness_ratio,
                        mouse_config.get('mouse-sensitivity'))

            if loop_iterator % 100 == 0:
                loop_iterator = 0
                if segments_queue.qsize() > queue_limit:
                    clear_queue(segments_queue, queue_limit)

                    if roughness_ratio < 9:
                        roughness_ratio += 1
                else:
                    if roughness_ratio > 0:
                        roughness_ratio -= 1

        except queue.Empty:
            pass
