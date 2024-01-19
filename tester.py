import cv2
import joblib
from cvpipe import process_frame
import mediapipe as mp

class AI_Tester:
    def __init__(self, model):
        self.model = joblib.load(model)
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
        self.mp_drawing = mp.solutions.drawing_utils

    def analyze(self, video_path):
        print(f"Analyzing {video_path}...")

        cap = cv2.VideoCapture(video_path)

        while cap.isOpened():
            ret, frame = cap.read()

            if not ret:
                print(f"ERROR: Failed to retrieve a frame from {video_path}!")
                break

            # Prepare the frame
            frame_features, _, frame = process_frame(frame, 480, 320, self.pose, self.mp_pose, self.mp_drawing)

            # Give the frame to the model
            prediction = self.model.predict([frame_features])

            # Interpret model output
            print(f"PREDICTION: {prediction}")

            cv2.imshow('Frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

        # Return the results
        return prediction
