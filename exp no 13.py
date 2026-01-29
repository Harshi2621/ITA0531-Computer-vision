import cv2
import numpy as np

# Read the input image
image = cv2.imread(r"C:\Users\amuth.AMUTHAVALLI\OneDrive\Desktop\cv.jpg")

if image is None:
    print("Image not found")
else:
    rows, cols = image.shape[:2]

    # Select 3 points from the original image
    src_points = np.float32([
        [50, 50],
        [200, 50],
        [50, 200]
    ])

    # Select corresponding points in the output image
    dst_points = np.float32([
        [70, 100],
        [220, 50],
        [100, 250]
    ])

    # Get affine transformation matrix
    affine_matrix = cv2.getAffineTransform(src_points, dst_points)

    # Apply affine transformation
    affine_image = cv2.warpAffine(image, affine_matrix, (cols, rows))

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Affine Transformed Image", affine_image)

    # Save output image
    cv2.imwrite("affine_image.jpg", affine_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
