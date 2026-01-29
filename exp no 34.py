import cv2
import numpy as np

h = int(input("Enter height: "))
w = int(input("Enter width: "))

img = np.ones((h, w, 3), dtype=np.uint8) * 255

cv2.circle(img, (w//2, h//2), 80, (255,0,0), 4)

cv2.imshow("Circle", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
