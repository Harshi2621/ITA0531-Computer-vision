import cv2

# Read the input image
image = cv2.imread(r"C:\Users\amuth.AMUTHAVALLI\OneDrive\Desktop\cv.jpg")

if image is None:
    print("Image not found")
else:
    # Rotate image by 180 degrees
    rotated_image = cv2.rotate(image, cv2.ROTATE_180)

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("180 Degree Rotated Image", rotated_image)

    # Save the rotated image
    cv2.imwrite("rotated_180.jpg", rotated_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
