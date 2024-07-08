import cv2
import mediapipe as mp
from .config_handler import read_config
from .calculate_cases import calculate_joint_angle, is_right_hand_active, is_left_hand_active, is_walking, is_leaning_right, is_leaning_left, index_finger_up, peace_sign, three_fingers_up, four_fingers_up
from .input_operations import hold_key, release_key, single_key_press, move_mouse, hold_mb, single_mb_press
from .mouse_handler import emulate_mouse

def pose_detection():
    binds_config = read_config()

    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose
    mp_hands = mp.solutions.hands
    cap = cv2.VideoCapture(0)


    # USUNAC POZNIEJ
    old_landmarks_hands = None

    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose, mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5, max_num_hands=2) as hands:
        while cap.isOpened():
            ret, frame = cap.read()

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            results = pose.process(image)
            results_hands = hands.process(image)

            image.flags.writeable = True
            # image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) // Tylko wizualnie kamera ma dobre kolory - pytanie czy to potrzebne

            try:
                landmarks_hands = results_hands.multi_hand_landmarks
                landmarks_body = results.pose_landmarks.landmark

                if len(landmarks_hands) > 1:
                    right_hand = landmarks_hands[0]
                    left_hand = landmarks_hands[1]

                    if right_hand.landmark[0].x > left_hand.landmark[0].x:
                        right_hand, left_hand = left_hand, right_hand

                    # ZMIENIC POZNIEJ ZEBY NIE ZWRACALO
                    landmarks_tmp = emulate_mouse(right_hand, old_landmarks_hands)

                    # emulate_keyboard(landmarks_body, left_hand)

                    if landmarks_tmp != None:
                        old_landmarks_hands = landmarks_tmp

            except:
                pass

            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
            if results_hands.multi_hand_landmarks:
                for hand in results_hands.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS)

            cv2.imshow('Webcam Player Controler', image)

            cv2.waitKey(1)
            if cv2.getWindowProperty('Webcam Player Controler', cv2.WND_PROP_VISIBLE) < 1:
                break

    cap.release()
    cv2.destroyAllWindows()