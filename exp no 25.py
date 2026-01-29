import cv2

img = cv2.imread(r"C:\Users\amuth.AMUTHAVALLI\OneDrive\Desktop\cv.jpg")
template = cv2.imread(r"C:\Users\amuth.AMUTHAVALLI\OneDrive\Desktop\watch.jpg")

if img is None or template is None:
    print("Error: Image or template not found")
else:
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_temp = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    w, h = gray_temp.shape[::-1]

    result = cv2.matchTemplate(gray_img, gray_temp, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val > 0.6:   # IMPORTANT threshold
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(img, top_left, bottom_right, (0,255,0), 2)

    cv2.imshow("Watch Detection", img)
    cv2.imwrite("watch_detected.jpg", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
