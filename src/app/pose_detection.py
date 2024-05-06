import cv2
import mediapipe as mp
from pynput.mouse import Controller
from .config_handler import read_config
from .calculate_cases import calculate_joint_angle, is_right_hand_active, is_left_hand_active, is_walking, is_leaning_right, is_leaning_left, index_finger_up, peace_sign, three_fingers_up, four_fingers_up
from .input_operations import hold_key, release_key, single_key_press, move_mouse, hold_mb, single_mb_press

def pose_detection():
    binds_config = read_config()

    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose
    mp_hands = mp.solutions.hands
    cap = cv2.VideoCapture(0)

    mouse = Controller()
    left_hand = None
    right_hand = None
    # CURSOR STATES
    old_x = 0
    old_y = 0

    #SINGLE USE STATES
    is_jumping = False
    l_index = False
    l_peace = False
    l_three = False
    l_four = False

    r_index = False
    r_peace = False
    r_three = False
    r_four = False

    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose, mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5, max_num_hands=2) as hands:
        while cap.isOpened():
            ret, frame = cap.read()

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            results = pose.process(image)
            results_hands = hands.process(image)

            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            try:
                landmarks = results.pose_landmarks.landmark
                landmarks_hands = results_hands.multi_hand_landmarks

                # Sprawdzenie czy sa 2 dlonie i przypisanie prawej i lewej
                if len(landmarks_hands) > 1:
                    first_hand = landmarks_hands[0]
                    second_hand = landmarks_hands[1]

                    if first_hand.landmark[0].x < landmarks[0].x and second_hand.landmark[0].x > landmarks[0].x:
                        right_hand = first_hand
                        left_hand = second_hand

                    elif first_hand.landmark[0].x > landmarks[0].x and second_hand.landmark[0].x < landmarks[0].x:
                        right_hand = second_hand
                        left_hand = first_hand
                    else:
                        raise ValueError("Błąd - dwie dłonie po jednej stronie")

                else:
                    raise ValueError("Brak wykrytych dłoni")

                if is_right_hand_active(landmarks[16], landmarks[24], landmarks[0]):
                    move_mouse(mouse, landmarks[16].x, landmarks[16].y, old_x, old_y, 3)

                    old_x = landmarks[16].x
                    old_y = landmarks[16].y

                    # Gesty
                    # Myszki
                    # Jednokrotne przycisniecie lewego
                    if (index_finger_up(right_hand)):
                        single_mb_press("left", r_index)
                        r_index = True
                    else:
                        r_index = False
                    # Przytrzymanie lewego
                    if (peace_sign(right_hand)):
                        hold_mb("left", r_peace)
                        r_peace = False
                    else:
                        r_peace = True
                    # Jednokrotnie prawego:
                    if (three_fingers_up(right_hand)):
                        single_key_press("right", r_three)
                        r_three = True
                    else:
                        r_three = False
                    # Przytrzymanie prawego:
                    if (four_fingers_up(right_hand)):
                        hold_mb("right", r_four)
                        r_four = False
                    else:
                        r_four = True

                if is_left_hand_active(landmarks[15], landmarks[23], landmarks[0]):

                    # Klawiatura
                    if (index_finger_up(left_hand)):
                        single_key_press(binds_config["l-index-up"], l_index)
                        l_index = True
                    else:
                        l_index = False

                    if (peace_sign(left_hand)):
                        single_key_press(binds_config["l-peace"], l_peace)
                        l_peace = True
                    else:
                        l_peace = False

                    if (three_fingers_up(left_hand)):
                        single_key_press(binds_config["l-three-up"], l_three)
                        l_three = True
                    else:
                        l_three = False

                    if (four_fingers_up(left_hand)):
                        single_key_press(binds_config["l-four-up"], l_four)
                        l_four = True
                    else:
                        l_four = False

                # CHODZENIE
                if (calculate_joint_angle(landmarks[12], landmarks[24], landmarks[26]) < 120
                    or calculate_joint_angle(landmarks[11], landmarks[23], landmarks[25]) < 120):

                    hold_key(binds_config["Walk"])
                else:
                    release_key(binds_config["Walk"])

                # SKAKANIE
                if (calculate_joint_angle(landmarks[12], landmarks[24], landmarks[26]) < 90
                    or calculate_joint_angle(landmarks[11], landmarks[23], landmarks[25]) < 90):

                    if not is_jumping:
                        single_key_press(binds_config["Jump"], is_jumping)
                        is_jumping = True
                else:
                    is_jumping = False

                # SKLON PRAWO
                if is_leaning_right(landmarks[0], landmarks[24]):
                    hold_key(binds_config["Go right"])
                else:
                    release_key(binds_config["Go right"])

                # SKLON LEWO
                if is_leaning_left(landmarks[0], landmarks[23]):
                    hold_key(binds_config["Go left"])
                else:
                    release_key(binds_config["Go left"])

                right_hand = None
                left_hand = None
            except:
                pass

            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
            if results_hands.multi_hand_landmarks:
                for hand in results_hands.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS)

            cv2.imshow('Webcam Player Controler', image)

            key = cv2.waitKey(10)
            if key == 27:
                break

    cap.release()
    cv2.destroyAllWindows()
