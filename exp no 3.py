import cv2

# Read the image
image = cv2.imread(r"C:\Users\amuth.AMUTHAVALLI\OneDrive\Desktop\cv.jpg")

# Check if image is loaded
if image is None:
    print("Image not found")
else:
    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection
    edges = cv2.Canny(gray_image, 100, 200)

    # Display original image
    cv2.imshow("Original Image", image)

    # Display outline image
    cv2.imshow("Canny Edge Detection", edges)

    # Save the output image
    cv2.imwrite("canny_edges.jpg", edges)

    # Wait for key press
    cv2.waitKey(0)
    cv2.destroyAllWindows()
