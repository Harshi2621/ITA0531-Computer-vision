import cv2
import numpy as np

# Read the input image
image = cv2.imread(r"C:\Users\amuth.AMUTHAVALLI\OneDrive\Desktop\cv.jpg")

if image is None:
    print("Image not found")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Create a kernel (structuring element)
    kernel = np.ones((5, 5), np.uint8)

    # Apply erosion
    eroded_image = cv2.erode(gray, kernel, iterations=1)

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Eroded Image", eroded_image)

    # Save the output image
    cv2.imwrite("eroded_image.jpg", eroded_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
