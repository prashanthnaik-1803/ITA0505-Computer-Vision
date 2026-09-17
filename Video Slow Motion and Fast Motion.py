import cv2

cap = cv2.VideoCapture("video.mp4")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Video", frame)

    key = cv2.waitKey(100) & 0xFF

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
