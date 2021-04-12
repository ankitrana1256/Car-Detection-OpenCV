
import cv2


def drawCircle(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        print('({}, {})'.format(x, y))

        imgCopy = img.copy()
        cv2.circle(imgCopy, (x, y), 10, (255, 0, 0), -1)

        cv2.imshow('image', imgCopy)


img = cv2.imread('Resources/1.png')
image1 = cv2.line(img, (223,208), (487,208), (0,0,255), 2)
image2 = cv2.line(img, (100,302), (590,302), (0,0,255), 2)
cv2.imshow('window_name', img)

cv2.setMouseCallback('image', drawCircle)

cv2.waitKey(0)
cv2.destroyAllWindows()