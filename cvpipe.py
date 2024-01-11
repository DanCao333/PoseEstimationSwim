import math
import cv2
import mediapipe

# import [package_name] *[as alias]
# from [package_name] import [sub_item]

def model_creation():
    pass

def calculate_distance(start, end):
    return math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)

def calculate_angle(a, b, c):
    angle_radians = math.atan2(c.x - b.x, c.y - b.y) - math.atan2(a.x - b.x, a.y - b.y)
    angle_degrees = math.degrees(angle_radians)
    return angle_degrees + 360 if angle_degrees < 0 else angle_degrees

def process_video(video_path):
    """This is test"""
    cap = cv2.VideoCapture(video_path)

    # Initialize mediapipe
    mp_pose = mediapipe.solutions.pose
    pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

    # Initialize important variables here
    width = 480
    height = 320
    hip_start = 0

    # Start looking at the video
    while cap.isOpened():
        success, frame = cap.read()

        if not success:
            break
        
        frame_resize = cv2.resize(frame, (width, height))
        rgb_frame = cv2.cvtColor(frame_resize, cv2.COLOR_BGR2RGB)
        
        # Give the frame to mediapipe
        results = pose.process(rgb_frame)
        landmarks = result.pose_landmarks

        if landmarks:
            # TODO specify left/right, athletes starting with diff starting foot
            # TODO what do we do with the landmarks?
            hip_landmark = landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP]
            hip_position = (hip_landmark.x * width, hip_landmark.y * height) if hip_landmark.visibility > 0.5 else (0, 0)

            knee_landmark = landmarks.landmark[mp_pose.PoseLandmark.LEFT_KNEE]
            knee_position = (knee_landmark.x * width, knee_landmark.y * height) if knee_landmark.visibility > 0.5 else (0,0)
            # TODO calculate angle of other elements
            angle_legs = calculate_angle(landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP],
                                         landmarks.landmark[mp_pose.PoseLandmark.LEFT_KNEE],
                                         landmarks.landmark[mp_pose.PoseLandmark.LEFT_ANKLE])
            print(f"Angle of legs: {angle_legs}")

            # TODO Check if person started (get timestamp along with related conversions as needed)

        # Calculate displacement (distance travelled by hip)

        # Calculate velocity

    # Do additional data processing/preparation to send data to model

    cap.release()

    # TODO replace with packaged data results
    return None

        

