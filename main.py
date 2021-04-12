import cv2
import numpy as np

matches = []


def get_centroid(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx, cy


cap = cv2.VideoCapture("Resources/cars.mp4")

if cap.isOpened():
    ret, frame1 = cap.read()
else:
    ret = False

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while ret:
    d = cv2.absdiff(frame1, frame2)
    roi = frame1[200:720, 0:1280]
    grey = cv2.cvtColor(d, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey, (5, 5), 0)
    ret, th = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(th, np.ones((3, 3)))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
    closing = cv2.morphologyEx(dilated, cv2.MORPH_CLOSE, kernel)
    contours, h = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for(i, c) in enumerate(contours):
        (x, y, w, h) = cv2.boundingRect(c)
        contours_valid = (w >= 40) and (h >= 40)

        if not contours_valid:
            continue

        cv2.rectangle(frame1, (x-10, y-10), (x+w+10, y+h+10), (255, 0, 0), 2)
        cv2.putText(frame1, "Vehicle", (x, y - 10), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (255, 0, 255), 2)
        centroid = get_centroid(x, y, w, h)
        matches.append(centroid)
        cv2.circle(frame1, centroid, 5, (0, 255, 0), -1)
        cx, cy = get_centroid(x, y, w, h)

    cv2.imshow("Difference", th)
    cv2.imshow("Original", frame1)

    if cv2.waitKey(20) == 27:
        break
    frame1 = frame2
    ret, frame2 = cap.read()
cv2.destroyAllWindows()
cap.release()
