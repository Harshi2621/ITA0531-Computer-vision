import cv2

# Read the image
image = cv2.imread(r"C:\Users\amuth.AMUTHAVALLI\OneDrive\Desktop\cv.jpg")

# Check if image is loaded
if image is None:
    print("Image not found")
else:
    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Histogram Equalization
    equalized_image = cv2.equalizeHist(gray_image)

    # Display original grayscale image
    cv2.imshow("Original Grayscale Image", gray_image)

    # Display histogram equalized image
    cv2.imshow("Histogram Equalized Image", equalized_image)

    # Save output images
    cv2.imwrite("original_gray.jpg", gray_image)
    cv2.imwrite("equalized_image.jpg", equalized_image)

    # Wait for key press
    cv2.waitKey(0)
    cv2.destroyAllWindows()
