import math
import cv2
import mediapipe as mp

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
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
    mp_drawing = mp.solutions.drawing_utils

    # Initialize Video Writer
    # Can change code here to add a number every time
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter("output_video.mp4", fourcc, 30, (640, 480))
    
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
        landmarks = results.pose_landmarks

        if landmarks:
            # draw the landmarks onto frame:
            mp_drawing.draw_landmarks(frame, landmarks, mp_pose.POSE_CONNECTIONS)

            # TODO specify left/right, athletes starting with diff starting foot
            # TODO what do we do with the landmarks?
            hip_landmark = landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP]
            hip_position = (hip_landmark.x * width, hip_landmark.y * height) if hip_landmark.visibility > 0.5 else (0, 0)

            knee_landmark = landmarks.landmark[mp_pose.PoseLandmark.LEFT_KNEE]
            knee_position = (knee_landmark.x * width, knee_landmark.y * height) if knee_landmark.visibility > 0.5 else (0,0)

            ankle_landmark = landmarks.landmark[mp_pose.PoseLandmark.LEFT_ANKLE]
            ankle_position = (ankle_landmark.x * width, ankle_landmark.y * height) if ankle_landmark.visibility > 0.5 else (0,0)
            
            # TODO calculate angle of other elements
            angle_legs = calculate_angle(landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP],
                                         landmarks.landmark[mp_pose.PoseLandmark.LEFT_KNEE],
                                         landmarks.landmark[mp_pose.PoseLandmark.LEFT_ANKLE])
            print(f"Angle of legs: {angle_legs}")

        cv2.imshow("Test Video", frame)

        key = cv2.waitKey(1)

        if key == ord('q'):
            break
        out.write(frame)

            # TODO Check if person started (get timestamp along with related conversions as needed)

        # Calculate displacement (distance travelled by hip)

        # Calculate velocity

    # Do additional data processing/preparation to send data to model

    cap.release()
    out.release()

    # TODO replace with packaged data results
    return None

        

