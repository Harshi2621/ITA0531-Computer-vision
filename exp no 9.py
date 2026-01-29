import cv2

# Read the input image
image = cv2.imread(r"C:\Users\amuth.AMUTHAVALLI\OneDrive\Desktop\cv.jpg")

if image is None:
    print("Image not found")
else:
    # Resize image to smaller size
    small_image = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

    # Resize image to bigger size
    big_image = cv2.resize(image, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Smaller Image", small_image)
    cv2.imshow("Bigger Image", big_image)

    # Save output images
    cv2.imwrite("small_image.jpg", small_image)
    cv2.imwrite("big_image.jpg", big_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
