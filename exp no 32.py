import cv2
import numpy as np

h = int(input("Enter height: "))
w = int(input("Enter width: "))

img = np.ones((h, w, 3), dtype=np.uint8) * 255

box_h = h // 10
box_w = w // 10

# Top-left: Black
img[0:box_h, 0:box_w] = (0,0,0)

# Top-right: Blue
img[0:box_h, w-box_w:w] = (255,0,0)

# Bottom-left: Green
img[h-box_h:h, 0:box_w] = (0,255,0)

# Bottom-right: Red
img[h-box_h:h, w-box_w:w] = (0,0,255)

cv2.imshow("Colored Boxes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
