# from ai_engine import AIEngine
from cvpipe import process_video
from dataset import process_and_save_dataset, add_distance_column

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

# specify input
video_list = ["videos/andrea1.mp4", "videos/zeke2.mp4"]
file_path = "swimming.csv"

sequences = []
for video in video_list:
    results = process_video(video_path=video)
    sequences.append(results)


process_and_save_dataset(sequences=sequences, file_path=file_path)

# TODO: add distance column manually
# e.g. 4 videos would mean 4 distances like [5.5, 5.0, 6.1, 6.5]
add_distance_column(file_path, [])
"""carson 405
andrea 445
sean 420
hamilton 451
paige 412
zeke 600
vince 445
zeke 645
trevor 623
david 500
daniel 669"""
# How far away from the subject, plug into math formula
