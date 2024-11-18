import numpy as np

def calculate_joint_angle(outer_joint_1, searched_joint, outer_joint_2):
    outer_joint_1 = np.array([outer_joint_1.x, outer_joint_1.y, outer_joint_1.z])
    searched_joint = np.array([searched_joint.x, searched_joint.y, searched_joint.z])
    outer_joint_2 = np.array([outer_joint_2.x, outer_joint_2.y, outer_joint_2.z])

    vector_1 = outer_joint_1 - searched_joint
    vector_2 = outer_joint_2 - searched_joint

    vector_1 /= np.linalg.norm(vector_1)
    vector_2 /= np.linalg.norm(vector_2)

    dot_product = np.dot(vector_1, vector_2)
    angle = np.arccos(np.clip(dot_product, -1.0, 1.0))

    return np.degrees(angle)

def is_right_hand_active(right_wrist, left_hip, nose):
    if right_wrist.x < nose.x and right_wrist.y < left_hip.y:
        return True

    return False

def is_left_hand_active(left_wrist, right_hip, nose):
    if left_wrist.x > nose.x and left_wrist.y < right_hip.y:
        return True

    return False

def is_leaning(right_hip, left_hip, nose):
    if nose.x < right_hip.x:
        return "right"
    if nose.x > left_hip.x:
        return "left"
    return False

def open_palm(wrist, thumb_mcp, thump_tip, index_mcp, index_tip, middle_mcp, middle_tip, ring_mcp, ring_tip, pinky_mcp, pinky_tip):
    if not calculate_joint_angle(wrist, thumb_mcp, thump_tip) > 160:
        return False
    if not calculate_joint_angle(wrist, index_mcp, index_tip) > 160:
        return False
    if not calculate_joint_angle(wrist, middle_mcp, middle_tip) > 160:
        return False
    if not calculate_joint_angle(wrist, ring_mcp, ring_tip) > 160:
        return False
    if not calculate_joint_angle(wrist, pinky_mcp, pinky_tip) > 160:
        return False

    return True

def index_finger_up(wrist, index_mcp, index_tip, middle_mcp, middle_tip, ring_mcp, ring_tip, pinky_mcp, pinky_tip):
    if not calculate_joint_angle(wrist, index_mcp, index_tip) > 160:
        return False
    if not calculate_joint_angle(wrist, middle_mcp, middle_tip) < 120:
        return False
    if not calculate_joint_angle(wrist, ring_mcp, ring_tip) < 120:
        return False
    if not calculate_joint_angle(wrist, pinky_mcp, pinky_tip) < 120:
        return False

    return True

def peace_sign(wrist, index_mcp, index_tip, middle_mcp, middle_tip, ring_mcp, ring_tip, pinky_mcp, pinky_tip):
    if not calculate_joint_angle(wrist, index_mcp, index_tip) > 160:
        return False
    if not calculate_joint_angle(wrist, middle_mcp, middle_tip) > 160:
        return False
    if not calculate_joint_angle(wrist, ring_mcp, ring_tip) < 120:
        return False
    if not calculate_joint_angle(wrist, pinky_mcp, pinky_tip) < 120:
        return False

    return True

def three_fingers_up(wrist, index_mcp, index_tip, middle_mcp, middle_tip, ring_mcp, ring_tip, pinky_mcp, pinky_tip):
    if not calculate_joint_angle(wrist, index_mcp, index_tip) > 160:
        return False
    if not calculate_joint_angle(wrist, middle_mcp, middle_tip) > 160:
        return False
    if not calculate_joint_angle(wrist, ring_mcp, ring_tip) > 160:
        return False
    if not calculate_joint_angle(wrist, pinky_mcp, pinky_tip) < 120:
        return False

    return True

def four_fingers_up(wrist, index_mcp, index_tip, middle_mcp, middle_tip, ring_mcp, ring_tip, pinky_mcp, pinky_tip):
    if not calculate_joint_angle(wrist, index_mcp, index_tip) > 160:
        return False
    if not calculate_joint_angle(wrist, middle_mcp, middle_tip) > 160:
        return False
    if not calculate_joint_angle(wrist, ring_mcp, ring_tip) > 160:
        return False
    if not calculate_joint_angle(wrist, pinky_mcp, pinky_tip) > 160:
        return False

    return True


def calculate_gesture(hand):
    wrist = hand.landmark[0]
    thumb_mcp = hand.landmark[2]
    thump_tip = hand.landmark[4]
    index_mcp = hand.landmark[5]
    index_tip = hand.landmark[8]
    middle_mcp = hand.landmark[9]
    middle_tip = hand.landmark[12]
    ring_mcp = hand.landmark[13]
    ring_tip = hand.landmark[16]
    pinky_mcp = hand.landmark[17]
    pinky_tip = hand.landmark[20]

    if open_palm(wrist, thumb_mcp, thump_tip, index_mcp, index_tip, middle_mcp,
                middle_tip, ring_mcp, ring_tip, pinky_mcp, pinky_tip):
        return "open_palm"

    if four_fingers_up(wrist, index_mcp, index_tip, middle_mcp, middle_tip,
                ring_mcp, ring_tip, pinky_mcp, pinky_tip):
        return "four_fingers_up"

    if index_finger_up(wrist, index_mcp, index_tip, middle_mcp, middle_tip,
                ring_mcp, ring_tip, pinky_mcp, pinky_tip):
        return "index_finger_up"

    if peace_sign(wrist, index_mcp, index_tip, middle_mcp, middle_tip,
                ring_mcp, ring_tip, pinky_mcp, pinky_tip):
        return "peace_sign"

    if three_fingers_up(wrist, index_mcp, index_tip, middle_mcp, middle_tip,
                ring_mcp, ring_tip, pinky_mcp, pinky_tip):
        return "three_fingers_up"

    return None
