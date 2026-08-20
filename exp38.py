import cv2

image = cv2.imread("image1.jpg")

if image is None:
    print("Image not found!")
    exit()

# Load face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

# Convert to grayscale
gray = cv2.cvtColor(
    image,
    cv2.COLOR_BGR2GRAY
)

# Detect faces
faces = face_cascade.detectMultiScale(
    gray,
    1.3,
    5
)

# Count faces
count = len(faces)

print("Number of faces:", count)

# Draw rectangles
for x, y, w, h in faces:

    cv2.rectangle(
        image,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        4
    )

cv2.imshow("Face Count", image)

cv2.waitKey(0)
cv2.destroyAllWindows()