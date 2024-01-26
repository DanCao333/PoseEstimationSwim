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

if command == "0":
    # specify input
    video_list = ["videos/carson1.mp4", "videos/andrea1.mp4", "videos/sean1.mp4", "videos/andrew1.mp4", "videos/paige1.mp4", "videos/zeke2.mp4", "videos/vince2.mp4", "videos/trevor1.mp4"] 
    
    # video_list = ["videos/andrea1.mp4"]
    file_path = "csv/swimming.csv"

    sequences = []
    for video in video_list:
        results = process_video(video_path=video)
        sequences.append(results)

    process_and_save_dataset(sequences=sequences, file_path=file_path)

elif command == "1":
    # pass
    file_path = "csv/swimming.csv"
    # e.g. 4 videos would mean 4 distances like [5.5, 5.0, 6.1, 6.5]0
    add_distance_column(file_path, [405, 445, 420, 451, 412, 600, 461, 623])
    
    # How far away from the subject, plug into math formula
elif command == "2":
    print(f"Attempting to analyze {MODEL_PATH}")
    tester = AI_Tester(MODEL_PATH)
    prediction = tester.analyze("videos/vince1.mp4")
    print(f"PREDICTION (SCORE): {prediction}")
elif command == "3":
    print(f"Attempting to train")
    data_path = "csv/swimming.csv"
    model_name = "model_v1.pkl"
    train_model(dataset_path=data_path, model_name=model_name)
elif command == "4":
    video_list = ["videos/carson1.mp4", "videos/vince1.mp4", "videos/sean1.mp4", "videos/andrew1.mp4", "videos/paige1.mp4", "videos/zeke2.mp4", "videos/vince2.mp4", "videos/trevor1.mp4"] 
    file_path = "csv/swimming.csv"
    sequences = []
    for video in video_list:
        results = process_video(video_path=video)
        sequences.append(results)
    process_and_save_dataset(sequences=sequences, file_path=file_path)
    add_distance_column(file_path, [405, 445, 420, 451, 412, 600, 461, 623])
    print(f"Attempting to train")
    model_name = "model_v1.pkl"
    train_model(dataset_path=file_path, model_name=model_name)
    print(f"Attempting to analyze {model_name}")
    tester = AI_Tester(model_name)
    prediction = tester.analyze("videos/andrea1.mp4")
    print(f"PREDICTION (SCORE): {prediction}")




