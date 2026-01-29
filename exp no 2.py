import cv2

# Read the image
image = cv2.imread(r"C:\Users\amuth.AMUTHAVALLI\OneDrive\Desktop\cv.jpg")

# Check if image is loaded
if image is None:
    print("Image not found")
else:
    # Apply Gaussian Blur
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

    # Display original image
    cv2.imshow("Original Image", image)

    # Display blurred image
    cv2.imshow("Gaussian Blurred Image", blurred_image)

    # Save blurred image
    cv2.imwrite("gaussian_blur.jpg", blurred_image)

    # Wait for key press
    cv2.waitKey(0)
    cv2.destroyAllWindows()
