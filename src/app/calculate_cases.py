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
    angle = np.arccos(dot_product)

    return np.degrees(angle)


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

