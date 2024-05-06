def calculate_joint_angle(outer_joint_1, searched_joint, outer_joint2):
    ...

# Prawa reka aktywna jak prawy nadgarstek jest powyzej bioder i po prawej stronie głowy
def is_right_hand_active(right_wrist, left_hip, nose):
    if right_wrist.x < nose.x:
        if right_wrist.y < left_hip.y:
            return True

    return False

# Lewa reka aktywna jak lewy nadgarstek jest powyzej bioder i jest po lewej stronie głowy
def is_left_hand_active(left_wrist, right_hip, nose):
    if left_wrist.x > nose.x:
        if left_wrist.y < right_hip.y:
            return True

    return False

def is_walking():
    return False

def is_leaning_right(nose, right_hip):
    if nose.x < right_hip.x:
        return True

    return False

def is_leaning_left(nose, left_hip):
    if nose.x > left_hip.x:
        return True

    return False



# TODO Wymyslec jeszcze moze jak zrobic bieganie? jakies katy moze mniejsze miedzy stawami nog???
# MOZE KAT W BIODRZE??????

