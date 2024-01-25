import math
import cv2
import mediapipe as mp

# import [package_name] *[as alias]
# from [package_name] import [sub_item]
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
RESET = '\033[0m'

def model_creation():
    pass

def calculate_distance(start, end):
    print(f"Attempting to find distance between {start} and {end}")
    return math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)

def calculate_angle(a, b, c):
    angle_radians = math.atan2(c.x - b.x, c.y - b.y) - math.atan2(a.x - b.x, a.y - b.y)
    angle_degrees = math.degrees(angle_radians)
    return angle_degrees + 360 if angle_degrees < 0 else angle_degrees

def process_frame(frame, width, height, pose=None, mp_pose=None, mp_drawing=None):
    # Initialize mediapipe
    if not pose or not mp_pose or not mp_drawing:
        mp_pose = mp.solutions.pose
        pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
        mp_drawing = mp.solutions.drawing_utils
    
    # Initialize important variables here
    # width = 480
    # height = 320
    angle_sequence = []
    
    
    frame_resize = cv2.resize(frame, (width, height))
    rgb_frame = cv2.cvtColor(frame_resize, cv2.COLOR_BGR2RGB)
    
    # Give the frame to mediapipe
    results = pose.process(rgb_frame)
    landmarks = results.pose_landmarks

    shoulder_position = None
    if landmarks:
        # draw the landmarks onto frame:
        # mp_drawing.draw_landmarks(frame, landmarks, mp_pose.POSE_CONNECTIONS)

        # TODO specify left/right, athletes starting with diff starting foot
        # TODO what do we do with the landmarks?
        # To calculate left leg angles:
        hip_landmark = landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP]
        hip_position = (hip_landmark.x * width, hip_landmark.y * height) if hip_landmark.visibility > 0.5 else (0, 0)

        knee_landmark = landmarks.landmark[mp_pose.PoseLandmark.LEFT_KNEE]
        knee_position = (knee_landmark.x * width, knee_landmark.y * height) if knee_landmark.visibility > 0.5 else (0,0)

        ankle_landmark = landmarks.landmark[mp_pose.PoseLandmark.LEFT_ANKLE]
        ankle_position = (ankle_landmark.x * width, ankle_landmark.y * height) if ankle_landmark.visibility > 0.5 else (0,0)

        # To calculate right leg  angles:
        rhip_landmark = landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP]
        rhip_position = (rhip_landmark.x * width, rhip_landmark.y * height) if rhip_landmark.visibility > 0.5 else (0, 0)

        rknee_landmark = landmarks.landmark[mp_pose.PoseLandmark.LEFT_KNEE]
        rknee_position = (rknee_landmark.x * width, rknee_landmark.y * height) if rknee_landmark.visibility > 0.5 else (0,0)

        rankle_landmark = landmarks.landmark[mp_pose.PoseLandmark.LEFT_ANKLE]
        rankle_position = (rankle_landmark.x * width, rankle_landmark.y * height) if rankle_landmark.visibility > 0.5 else (0,0)
        
        # To calculate right arm angles
        rshoulder_landmark = landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER]
        rshoulder_position = (rshoulder_landmark.x * width, rshoulder_landmark.y * height) if rshoulder_landmark.visibility > 0.5 else (0, 0)

        relbow_landmark = landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW]
        relbow_position = (relbow_landmark.x * width, relbow_landmark.y * height) if relbow_landmark.visibility > 0.5 else (0, 0)

        rwrist_landmark = landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST]
        rwrist_position = (rwrist_landmark.x * width, rwrist_landmark.y * height) if rwrist_landmark.visibility > 0.5 else (0, 0)
        
        # To calculate left arm angles
        lshoulder_landmark = landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER]
        lshoulder_position = (lshoulder_landmark.x * width, lshoulder_landmark.y * height) if lshoulder_landmark.visibility > 0.5 else (0, 0)

        lelbow_landmark = landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW]
        lelbow_position = (lelbow_landmark.x * width, lelbow_landmark.y * height) if lelbow_landmark.visibility > 0.5 else (0, 0)

        lwrist_landmark = landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST]
        lwrist_position = (lwrist_landmark.x * width, lwrist_landmark.y * height) if lwrist_landmark.visibility > 0.5 else (0, 0)
        
        
        # To calculate body angle
        rhip_landmark = landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP]
        rhip_position = (rhip_landmark.x * width, rhip_landmark.y * height) if lwrist_landmark.visibility > 0.5 else (0, 0)
        mp_drawing.draw_landmarks(frame, landmarks, mp_pose.POSE_CONNECTIONS)

        # Shoulder position
        shoulder_position = rshoulder_position
        
        # TODO calculate angle of other elements
        angle_l_legs = calculate_angle(landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP],
                                        landmarks.landmark[mp_pose.PoseLandmark.LEFT_KNEE],
                                        landmarks.landmark[mp_pose.PoseLandmark.LEFT_ANKLE])
        # print(f"Angle of left legs: {angle_l_legs}")
        l_leg_text = math.trunc(angle_l_legs)

        angle_r_legs = calculate_angle(landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP],
                                        landmarks.landmark[mp_pose.PoseLandmark.LEFT_KNEE],
                                        landmarks.landmark[mp_pose.PoseLandmark.LEFT_ANKLE])
        # print(f"Angle of right legs: {angle_r_legs}")

        r_leg_text = math.trunc(angle_r_legs)
        angle_l_arms =  calculate_angle(landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER],
                                        landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW],
                                        landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST])
        # print(f"Angle of left arms: {angle_l_arms}")

        l_arm_text = math.trunc(angle_l_arms)
        angle_r_arms = calculate_angle(landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER],
                                        landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW],
                                        landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST])
        # print(f"Angle of right arms: {angle_r_arms}")
        angle_body = calculate_angle(landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER],
                                        landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP],
                                        landmarks.landmark[mp_pose.PoseLandmark.RIGHT_KNEE])
        avg_arm_text = math.trunc((angle_r_arms + angle_l_arms)/2)
        
        # Prints out angle on screen:
        cv2.putText(frame, str("Arm angle: ") + str(avg_arm_text) + str(" Right leg angle: ") + str(r_leg_text) + str(" Left leg angle: ") + str(l_leg_text), org=(50,50), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1.0, color=(0, 0, 204))
        # print([angle_l_legs, angle_r_legs, angle_l_arms, angle_r_arms])
        angle_sequence.append([angle_l_legs, angle_r_legs, angle_l_arms, angle_r_arms, angle_body])
        

    return angle_sequence, shoulder_position, frame

def process_video(video_path):
    
    cap = cv2.VideoCapture(video_path)

    # Initialize mediapipe
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
    mp_drawing = mp.solutions.drawing_utils

    # Initialize Video Writer
    # Can change code here to add a number every time
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter("output_video.mp4", fourcc, 30, (480, 320))
    
    # Initialize important variables here
    width = 480
    height = 320
    start_time = 0
    end_time = 0
    start_shoulder_position = None
    end_shoulder_position = None
    aggregated_features = []

    
    # Start looking at the video
    print("Starting video playback")
    while cap.isOpened():
        success, frame = cap.read()

        if not success:
            break
        
        timestamp = cap.get(cv2.CAP_PROP_POS_MSEC)
        frame_features, shoulder_position, frame = process_frame(frame, width, height, pose, mp_pose, mp_drawing)
        
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
        out.write(frame)

            # TODO Check if person started (get timestamp along with related conversions as needed)

    # Calculate displacement (distance travelled)
    # if start_shoulder_position and end_shoulder_position:
    displacement = calculate_distance(start_shoulder_position, end_shoulder_position)
    print("Displacement:", displacement)
    print("Start shoulder position:", start_shoulder_position)
    print("End shoulder position:", end_shoulder_position)
    # Calculate velocity
    elapsed_time = (end_time - start_time) / 1000
    print("Elapsed time:", elapsed_time, "seconds")
    velocity = displacement / elapsed_time if elapsed_time > 0 else 0
    print(YELLOW + "Avg. Velocity (pixels/s):" + RESET, velocity)
    
    # Do additional data processing/preparation to send data to model
    all_angles = [angle for group in aggregated_features for angle in group]
    
    features = all_angles
    features.append(velocity)

    cap.release()
    out.release()
    return features
