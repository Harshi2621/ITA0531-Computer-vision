import cv2
import numpy as np

h = int(input("Enter height: "))
w = int(input("Enter width: "))

img = np.ones((h, w, 3), dtype=np.uint8) * 255

cv2.rectangle(img, (100,100), (300,250), (0,0,255), 3)

cv2.imshow("Rectangle", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
