import cv2
import mediapipe as mp
from pynput.mouse import Controller
from .config_handler import read_config
from .calculate_cases import calculate_joint_angle, is_right_hand_active, is_left_hand_active, is_walking, is_leaning_right, is_leaning_left
from .input_operations import hold_key, release_key, single_key_press, move_mouse

def pose_detection():
    binds_config = read_config()

    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose
    mp_hands = mp.solutions.hands
    cap = cv2.VideoCapture(0)

    mouse = Controller()

    # CURSOR STATES
    old_x = 0
    old_y = 0

    #SINGLE USE STATES
    is_jumping = False

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

                # if len(landmarks_hands) > 1:
                #     one_hand = landmarks_hands[0]
                #     second_hand = landmarks_hands[1]

                #     print("PRAWA")
                #     print(one_hand)


                # inicjalizatory do kursora
                # is_left_mb_pressed = False
                # is_right_mb_pressed = False



                # ZROBIC ZE PRZECHYLENIE W LEWO LUB W PRAWO TO POJSCIE W TA STRONE

                if is_right_hand_active(landmarks[16], landmarks[24], landmarks[0]):
                    move_mouse(mouse, landmarks[16].x, landmarks[16].y, old_x, old_y, 3)

                    old_x = landmarks[16].x
                    old_y = landmarks[16].y

                # if is_left_hand_active(landmarks[15], landmarks[23], landmarks[0]):

                    # TU DODAC FUNKCJE KLAWISZOWE

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


pose_detection()