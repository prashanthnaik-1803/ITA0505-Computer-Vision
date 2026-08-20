import cv2

# Open the video file
cap = cv2.VideoCapture("video.mp4")

# Check if video is opened successfully
if not cap.isOpened():
    print("Error: Cannot open video")
    exit()

print("Video opened successfully")

# Read video frame by frame
while True:
    ret, frame = cap.read()

    # Stop when video ends
    if not ret:
        break

    # Display video
    cv2.imshow("Video", frame)

    # Press Q to stop
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Release video
cap.release()

# Close windows
cv2.destroyAllWindows()