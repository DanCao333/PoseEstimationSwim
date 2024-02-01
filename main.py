# from ai_engine import AIEngine
from cvpipe import process_video
from dataset import process_and_save_dataset, add_distance_column
from tester import AI_Tester
from trainer import train_model
"""
main.py Objective:
-specify the input media
-process input to get landmarks
-create a dataset for the ML model based on input
"""

# import cv2
# img_grayscale = cv2.imread("IMG_9865.png", 0)
# cv2.imshow("window", img_grayscale)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.imwrite("IMG-9865.png", img_grayscale)

command = input("Which operation would you like to do? (0:DATASET, 1:EDIT, 2:ANALYSIS, 3: TRAIN, 4: UNIVERSAL): ").strip()

MODEL_PATH = "model_v1.pkl"
DATA_PATH = "csv/swimming.csv"

# MASTER_DATA = {
#     "videos/carson1.mp4": 405,

# }


# for entry in MASTER_DATA.items():
#     print(entry)
#     VIDEO_LIST.append(entry.key)
#     DISTANCE_COLUMN.append(entry.values)

VIDEO_LIST = ["videos/carson1.mp4", "videos/vince1.mp4", "videos/sean1.mp4", "videos/andrew1.mp4", "videos/paige1.mp4", "videos/zeke2.mp4", "videos/vince2.mp4", "videos/trevor1.mp4"]
DISTANCE_COLUMN = [405, 445, 420, 451, 412, 600, 461, 623]

if command == "0":
    sequences = []

    for video in VIDEO_LIST:
        results = process_video(video_path=video)
        sequences.append(results)

    process_and_save_dataset(sequences=sequences, file_path=DATA_PATH)

elif command == "1":
    # Add true distance values
    add_distance_column(DATA_PATH, DISTANCE_COLUMN)
    
    # How far away from the subject, plug into math formula
    
elif command == "2":
    print(f"Attempting to analyze {MODEL_PATH}")
    tester = AI_Tester(MODEL_PATH)
    prediction = tester.analyze("videos/david2.mp4")
    print(f"PREDICTION (SCORE): {prediction}")
    
elif command == "3":
    print(f"Attempting to train")
    data_path = "csv/swimming.csv"
    train_model(dataset_path=data_path, model_name=MODEL_PATH)
    
elif command == "4":
    sequences = []
    for video in VIDEO_LIST:
        results = process_video(video_path=video)
        sequences.append(results)
    process_and_save_dataset(sequences=sequences, file_path=DATA_PATH)
    add_distance_column(DATA_PATH, DISTANCE_COLUMN)
    print(f"Attempting to train")
    train_model(dataset_path=DATA_PATH, model_name=MODEL_PATH)
    print(f"Attempting to analyze {MODEL_PATH}")
    tester = AI_Tester(MODEL_PATH)
    prediction = tester.analyze("videos/trevor2.mp4")
    print(f"PREDICTION (SCORE): {prediction} inches")




