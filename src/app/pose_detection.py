import cv2
import mediapipe as mp
from .calculate_cases import is_right_hand_active, is_left_hand_active, is_walking

def pose_detection():
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose
    cap = cv2.VideoCapture(0)
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()
            
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            results = pose.process(image)
        
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            
            try:
                landmarks = results.pose_landmarks.landmark

                # if is_right_hand_active(landmarks[16], landmarks[23]):
                #     print("PRAWA AKTYWNA")

                if is_left_hand_active(landmarks[15], landmarks[24]):
                    print("LEWA ATYWNA")

                # if is_walking:
                #     print("IDZIESZ")

            except:
                pass
            
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)               
            
            cv2.imshow('Webcam Player Controler', image)

            key = cv2.waitKey(10)
            if key == 27: 
                break

    cap.release()
    cv2.destroyAllWindows()


# pose_detection()