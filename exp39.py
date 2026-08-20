import cv2

# Open video
cap = cv2.VideoCapture("vehicles.mp4")

if not cap.isOpened():
    print("Cannot open video!")
    exit()

frames = []

# Read all frames
while True:

    ret, frame = cap.read()

    if not ret:
        break

    frames.append(frame)

cap.release()

print("Total frames:", len(frames))

# Play in reverse
for frame in reversed(frames):

    cv2.imshow(
        "Reverse Slow Motion",
        frame
    )

    # Larger value = slower video
    if cv2.waitKey(100) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()