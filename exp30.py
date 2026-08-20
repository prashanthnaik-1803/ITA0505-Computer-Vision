import cv2

image = cv2.imread("image1.jpg")

if image is None:
    print("Image not found!")
    exit()

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

smile_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_smile.xml"
)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for x, y, w, h in faces:

    face_gray = gray[y:y+h, x:x+w]
    face_color = image[y:y+h, x:x+w]

    smiles = smile_cascade.detectMultiScale(
        face_gray,
        scaleFactor=1.8,
        minNeighbors=20
    )

    for sx, sy, sw, sh in smiles:

        cv2.rectangle(
            face_color,
            (sx, sy),
            (sx + sw, sy + sh),
            (0, 255, 0),
            2
        )

cv2.imshow("Smile Detection", image)

cv2.waitKey(0)
cv2.destroyAllWindows()