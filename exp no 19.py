import cv2
import numpy as np

# Read the image in grayscale
image = cv2.imread(r"C:\Users\amuth.AMUTHAVALLI\OneDrive\Desktop\cv.jpg", cv2.IMREAD_GRAYSCALE)

# Check if image is loaded
if image is None:
    print("Error: Image not found or unable to read")
else:
    # Create structuring element (kernel)
    kernel = np.ones((5, 5), np.uint8)

    # Apply erosion
    eroded_image = cv2.erode(image, kernel, iterations=1)

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Eroded Image", eroded_image)

    # Save output
    cv2.imwrite("eroded_output.jpg", eroded_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
