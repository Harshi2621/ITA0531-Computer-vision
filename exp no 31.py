import cv2

img = cv2.imread('input.jpg', 0)

# Apply threshold
_, segmented = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)

cv2.imshow('Original Image', img)
cv2.imshow('Segmented Image', segmented)
cv2.waitKey(0)
cv2.destroyAllWindows()
