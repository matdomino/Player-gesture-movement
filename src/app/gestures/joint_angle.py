import numpy as np

def calculate_joint_angle(outer_joint_1, searched_joint, outer_joint_2) -> np.float64:
    """
    Calculates angle between two bones.

        Parameters:
            - outer_joint_1, searched_joint, outer_joint_2 (numpy.ndarray): coords (x, y, z)
            of the first outer joint.

        Returns:
            - angle (numpy.float64): angle between two bones (in degrees).
    """

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
