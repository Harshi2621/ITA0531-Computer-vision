import cv2

# Read original image and watermark
image = cv2.imread(r"C:\Users\amuth.AMUTHAVALLI\OneDrive\Desktop\cv.jpg")
watermark = cv2.imread(r"C:\Users\amuth.AMUTHAVALLI\OneDrive\Desktop\download.jpg")

if image is None or watermark is None:
    print("Image or watermark not found")
else:
    # Resize watermark to fit image
    watermark = cv2.resize(watermark, (image.shape[1], image.shape[0]))

    # Blend images (watermarking)
    watermarked_image = cv2.addWeighted(image, 0.8, watermark, 0.2, 0)

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Watermarked Image", watermarked_image)

    # Save result
    cv2.imwrite("watermarked_image.jpg", watermarked_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
