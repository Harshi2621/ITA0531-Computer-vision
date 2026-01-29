import cv2
import numpy as np

# Read the input image
image = cv2.imread(r"C:\Users\amuth.AMUTHAVALLI\OneDrive\Desktop\cv.jpg")

if image is None:
    print("Image not found")
else:
    # Split into Blue, Green, Red channels
    b, g, r = cv2.split(image)

    # Calculate histograms
    hist_b = cv2.calcHist([b], [0], None, [256], [0, 256])
    hist_g = cv2.calcHist([g], [0], None, [256], [0, 256])
    hist_r = cv2.calcHist([r], [0], None, [256], [0, 256])

    # Print histogram analysis
    print("Histogram Analysis Based on Color Levels")
    print("Blue Channel Pixels :", int(np.sum(hist_b)))
    print("Green Channel Pixels:", int(np.sum(hist_g)))
    print("Red Channel Pixels  :", int(np.sum(hist_r)))
