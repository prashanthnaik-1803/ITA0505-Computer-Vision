import cv2
import pytesseract

# Open video
cap = cv2.VideoCapture("vehicles.mp4")

if not cap.isOpened():
    print("Cannot open video!")
    exit()

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )

    # Extract text
    text = pytesseract.image_to_string(gray)

    if text.strip():
        print("Detected Text:")
        print(text)

    # Display video
    cv2.imshow(
        "Text Extraction",
        frame
    )

    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()