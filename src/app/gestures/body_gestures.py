def is_left_hand_active(left_wrist, left_hip, nose) -> bool:
    """
    Checks if the left hand is active (it is higher than left hip and to the left of the nose).

        Parameters:
            - left_wrist, left_hip, nose (NormalizedLandmark): coords (x, y, z).

        Returns:
            - (bool): the active status of the left hand.
    """

    if left_wrist.x > nose.x and left_wrist.y < left_hip.y:
        return True

    return False

def is_leaning(right_hip, left_hip, nose) -> str | bool:
    """
    Checks if the person is leaning to the right or left.

        Parameters:
            - right_hip, left_hip, nose (NormalizedLandmark): coords (x, y, z).

        Returns:
            - (str | bool): status - right, left or False.
    """
    if nose.x < right_hip.x:
        return "right"
    if nose.x > left_hip.x:
        return "left"
    return False
