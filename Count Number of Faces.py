import cv2

def count_faces(image_path):

    image = cv2.imread(
        image_path
    )

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades +
        "haarcascade_frontalface_default.xml"
    )

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    face_count = len(faces)

    print(
        "Number of faces detected:",
        face_count
    )

    for (x, y, w, h) in faces:

        cv2.rectangle(
            image,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

    cv2.imshow(
        "Face Detection",
        image
    )

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return face_count


count_faces(
    "face_image.jpg"
)
