import cv2
import joblib
from cvpipe import process_frame
import mediapipe as mp
import pandas as pd
import math
from dataset import add_padding, process_dataset
import json


class AI_Tester:
    def __init__(self, model):
        self.model_path = model
        self.model = joblib.load(model)
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
        self.mp_drawing = mp.solutions.drawing_utils
        
        with open("max_sequence_len.json", "r") as f:
            self.max_sequence_len = json.load(f)["max_sequence_len"]

        with open("column_names.json", "r") as f:
            self.column_names = json.load(f)

    def calculate_distance(self, start, end):
        print(f"Attempting to find distance between {start} and {end}")
        return math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)

    def analyze(self, video_path):
        print(f"Analyzing {video_path}...")
        width = 480
        height = 320
        start_time = 0
        end_time = 0
        start_shoulder_position = None
        end_shoulder_position = None
        aggregated_features = []
        cap = cv2.VideoCapture(video_path)

        # path_components = self.model_path.split("_")
        # padding_num = int(path_components[0][5:]) + 1
        


        while cap.isOpened():
            success, frame = cap.read()

            if not success:
                break
            
            timestamp = cap.get(cv2.CAP_PROP_POS_MSEC)
            frame_features, shoulder_position, frame = process_frame(frame, width, height, self.pose, self.mp_pose, self.mp_drawing)
            
            if shoulder_position is not None:
                if start_shoulder_position is None:
                    start_shoulder_position = shoulder_position
                    start_time = timestamp
                    print("shoulder", start_shoulder_position)
                end_shoulder_position = shoulder_position
                end_time = timestamp

            aggregated_features.extend(frame_features)
                    

            cv2.imshow("Test Video", frame)

            key = cv2.waitKey(1)

            if key == ord('q'):
                break

                # TODO Check if person started (get timestamp along with related conversions as needed)

        # Calculate displacement (distance travelled)
        # if start_shoulder_position and end_shoulder_position:
        displacement = self.calculate_distance(start_shoulder_position, end_shoulder_position)
        # Calculate velocity
        elapsed_time = (end_time - start_time) / 1000
        # print("Elapsed time:", elapsed_time, "seconds")
        velocity = displacement / elapsed_time if elapsed_time > 0 else 0
        # print(YELLOW + "Avg. Velocity (pixels/s):" + RESET, velocity)
        
        # Do additional data processing/preparation to send data to model
        all_angles = [angle for group in aggregated_features for angle in group]
        
        features = all_angles + [0] * (self.max_sequence_len - 1 - len(all_angles))
        features.append(velocity)
        # print(features)
        # features = process_dataset([[features]])
        features = pd.DataFrame([features], columns=self.column_names)
        print(features)
        prediction = self.model.predict(features)
        
        cap.release()
        cv2.destroyAllWindows()

        # Return the results
        return prediction
