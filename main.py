from ai_engine import AIEngine
import ai_engine

import cv2
img_grayscale = cv2.imread("IMG_9865.png", 0)
cv2.imshow("window", img_grayscale)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("IMG-9865.png", img_grayscale)





if __name__ == "__main__":
    pass


