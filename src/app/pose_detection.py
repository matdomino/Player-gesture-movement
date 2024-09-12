import cv2
import mediapipe as mp
import threading
import queue
from .config_handler import read_config
from .mouse_handler import run_mouse_emulation
from .pointer_handler import pointer_movement_handler

mouse_landmarks_queue = queue.Queue()
pointer_queue = queue.Queue()
exit_event = threading.Event()
segments_queue = queue.Queue()

def pose_detection():
    global mouse_landmarks_queue
    global exit_event
    global segments_queue

    binds_config = read_config()

    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose
    mp_hands = mp.solutions.hands
    cap = cv2.VideoCapture(0)

    t_mouse = threading.Thread(target=run_mouse_emulation, args=(mouse_landmarks_queue, segments_queue, binds_config.get('mouse'), exit_event))
    t_pointer = threading.Thread(target=pointer_movement_handler, args=(segments_queue, binds_config.get('mouse').get('pointer-refresh-rate'), exit_event))

    t_mouse.start()
    t_pointer.start()

    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose, mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5, max_num_hands=2) as hands:
        while cap.isOpened() and not exit_event.is_set():
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

                    # TUTAJ DAC DODAWANIE DO KOLEJKI WATKOW
                    mouse_landmarks_queue.put(right_hand)

                    # emulate_keyboard(landmarks_body, left_hand)

            except:
                pass

            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
            if results_hands.multi_hand_landmarks:
                for hand in results_hands.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS)

            cv2.imshow('Webcam Player Controler', image)

            cv2.waitKey(1)
            if cv2.getWindowProperty('Webcam Player Controler', cv2.WND_PROP_VISIBLE) < 1:
                exit_event.set()
                break

    cap.release()
    cv2.destroyAllWindows()
    t_mouse.join()
    t_pointer.join()