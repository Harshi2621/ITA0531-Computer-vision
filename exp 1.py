import cv2

# Read the image
image = cv2.imread(r"C:\Users\amuth.AMUTHAVALLI\OneDrive\Desktop\cv.jpg")

# Display original image
cv2.imshow("Original Image", image)

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display grayscale image
cv2.imshow("Grayscale Image", gray_image)

# Wait for key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
