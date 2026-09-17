import cv2

watch_cascade = cv2.CascadeClassifier(
    "watch_cascade.xml"
)

image = cv2.imread("watch.jpg")

gray = cv2.cvtColor(
    image,
    cv2.COLOR_BGR2GRAY
)

watches = watch_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

for (x, y, w, h) in watches:
    cv2.rectangle(
        image,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        2
    )

cv2.imshow(
    "Detected Watch",
    image
)

cv2.waitKey(0)
cv2.destroyAllWindows()
