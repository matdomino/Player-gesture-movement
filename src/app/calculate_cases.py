def calculate_joint_angle(outer_joint_1, searched_joint, outer_joint2):
    ...

# Prawa reka aktywna jak prawy nadgarstek jest powyzej bioder i po prawej stronie lewego biodra
def is_right_hand_active(right_wrist, left_hip):
    if right_wrist.x < left_hip.x:
        if right_wrist.y < left_hip.y:
            return True

    return False

# Lewa reka aktywna jak lewy nadgarstek jest powyzej bioder i jest po lewej stronie prawego biodra 
def is_left_hand_active(left_wrist, right_hip):
    if left_wrist.x > right_hip.x:
        if left_wrist.y < right_hip.y:
            return True

    return False

def is_walking():
    return False

# TODO Wymyslec jeszcze moze jak zrobic bieganie? jakies katy moze mniejsze miedzy stawami nog???
# MOZE KAT W BIODRZE??????

