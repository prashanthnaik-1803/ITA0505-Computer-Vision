import cv2

# Load image
image = cv2.imread("image1.jpg")

if image is None:
    print("Image not found!")
    exit()

# Load face and eye classifiers
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_eye.xml"
)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for x, y, w, h in faces:

    # Draw face rectangle
    cv2.rectangle(
        image,
        (x, y),
        (x + w, y + h),
        (255, 0, 0),
        2
    )

    face_gray = gray[y:y+h, x:x+w]
    face_color = image[y:y+h, x:x+w]

    # Detect eyes
    eyes = eye_cascade.detectMultiScale(face_gray)

    for ex, ey, ew, eh in eyes:

        cv2.rectangle(
            face_color,
            (ex, ey),
            (ex + ew, ey + eh),
            (0, 255, 0),
            2
        )

cv2.imshow("Eye Detection", image)

cv2.waitKey(0)
cv2.destroyAllWindows()