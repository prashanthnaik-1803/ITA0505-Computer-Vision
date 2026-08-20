import cv2

# Load vehicle cascade
vehicle_cascade = cv2.CascadeClassifier("cars.xml")

# Open video
cap = cv2.VideoCapture("vehicles.mp4")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect vehicles
    vehicles = vehicle_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=3
    )

    # Draw rectangle
    for (x, y, w, h) in vehicles:
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            "Vehicle",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

    cv2.imshow("Vehicle Detection", frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()