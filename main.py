from ai_engine import AIEngine
from cvpipe import process_video

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
video_list = ["videos/sample_video.mp4"]
for video in video_list:
    results = process_video(video_path=video)
    # TODO implement dataset formatting
    
# TODO format and save final dataset



# if __name__ == "__main__":
#     pass


