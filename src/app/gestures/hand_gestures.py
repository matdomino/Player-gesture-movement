from .joint_angle import calculate_joint_angle

def open_palm(thumb_angle, index_angle, middle_angle, ring_angle, pinky_angle) -> bool:
    """
    Checks if the gesture is "open_palm".

        Parameters:
            - thumb_angle (numpy.float64): Angle of the thumb.
            - index_angle (numpy.float64): Angle of the index finger.
            - middle_angle (numpy.float64): Angle of the middle finger.
            - ring_angle (numpy.float64): Angle of the ring finger.
            - pinky_andle (numpy.float64): Angle of the pinky finger.

        Returns:
            - bool: True or False.
    """

    if thumb_angle > 160 and index_angle > 160 and middle_angle > 160 and ring_angle > 160 and pinky_angle > 160:
        return True

    return False

def index_finger_up(index_angle, middle_angle, ring_angle, pinky_angle) -> bool:
    """
    Checks if the gesture is "index_finger_up".

        Parameters:
            - index_angle (numpy.float64): Angle of the index finger.
            - middle_angle (numpy.float64): Angle of the middle finger.
            - ring_angle (numpy.float64): Angle of the ring finger.
            - pinky_andle (numpy.float64): Angle of the pinky finger.

        Returns:
            - bool: True or False.
    """

    if index_angle > 160 and middle_angle < 120 and ring_angle < 120 and pinky_angle < 120:
        return True

    return False

def peace_sign(index_angle, middle_angle, ring_angle, pinky_angle) -> bool:
    """
    Checks if the gesture is "peace_sign".

        Parameters:
            - index_angle (numpy.float64): Angle of the index finger.
            - middle_angle (numpy.float64): Angle of the middle finger.
            - ring_angle (numpy.float64): Angle of the ring finger.
            - pinky_andle (numpy.float64): Angle of the pinky finger.

        Returns:
            - bool: True or False.
    """

    if index_angle > 160 and middle_angle > 160 and ring_angle < 120 and pinky_angle < 120:
        return True

    return False

def three_fingers_up(index_angle, middle_angle, ring_angle, pinky_angle) -> bool:
    """
    Checks if the gesture is "three_fingers_up".

        Parameters:
            - index_angle (numpy.float64): Angle of the index finger.
            - middle_angle (numpy.float64): Angle of the middle finger.
            - ring_angle (numpy.float64): Angle of the ring finger.
            - pinky_andle (numpy.float64): Angle of the pinky finger.

        Returns:
            - bool: True or False.
    """

    if index_angle > 160 and middle_angle > 160 and ring_angle > 160 and pinky_angle < 120:
        return True

    return False

def four_fingers_up(index_angle, middle_angle, ring_angle, pinky_angle) -> bool:
    """
    Checks if the gesture is "four_fingers_up".

        Parameters:
            - index_angle (numpy.float64): Angle of the index finger.
            - middle_angle (numpy.float64): Angle of the middle finger.
            - ring_angle (numpy.float64): Angle of the ring finger.
            - pinky_andle (numpy.float64): Angle of the pinky finger.

        Returns:
            - bool: True or False.
    """

    if index_angle > 160 and middle_angle > 160 and ring_angle > 160 and pinky_angle > 160:
        return True

    return False

def calculate_gesture(hand) -> str | None:
    """
    Determines the current hand gesture.

    Parameters:
    - hand (NormalizedLandmarkList): coords (x, y, z) of the hand landmarks.

    Returns:
    str | None: The determined gesture (string) or None if the gesture is not recognized.
    """

    wrist = hand.landmark[0]
    thumb_angle = calculate_joint_angle(wrist, hand.landmark[2], hand.landmark[4])
    index_angle = calculate_joint_angle(wrist, hand.landmark[5], hand.landmark[8])
    middle_angle = calculate_joint_angle(wrist, hand.landmark[9], hand.landmark[12])
    ring_angle = calculate_joint_angle(wrist, hand.landmark[13], hand.landmark[16])
    pinky_angle = calculate_joint_angle(wrist, hand.landmark[17], hand.landmark[20])

    if open_palm(thumb_angle, index_angle, middle_angle, ring_angle, pinky_angle):
        return "open_palm"

    if four_fingers_up(index_angle, middle_angle, ring_angle, pinky_angle):
        return "four_fingers_up"

    if index_finger_up(index_angle, middle_angle, ring_angle, pinky_angle):
        return "index_finger_up"

    if peace_sign(index_angle, middle_angle, ring_angle, pinky_angle):
        return "peace_sign"

    if three_fingers_up(index_angle, middle_angle, ring_angle, pinky_angle):
        return "three_fingers_up"

    return None
