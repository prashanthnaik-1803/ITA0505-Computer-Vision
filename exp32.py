import cv2
import numpy as np

# User-defined size
width = int(input("Enter image width: "))
height = int(input("Enter image height: "))

# Create white image
image = np.ones(
    (height, width, 3),
    dtype=np.uint8
) * 255

# Box size
box = 100

# Black box - top left
cv2.rectangle(
    image,
    (10, 10),
    (10 + box, 10 + box),
    (0, 0, 0),
    -1
)

# Blue box - top right
cv2.rectangle(
    image,
    (width - box - 10, 10),
    (width - 10, 10 + box),
    (255, 0, 0),
    -1
)

# Green box - bottom left
cv2.rectangle(
    image,
    (10, height - box - 10),
    (10 + box, height - 10),
    (0, 255, 0),
    -1
)

# Red box - bottom right
cv2.rectangle(
    image,
    (width - box - 10, height - box - 10),
    (width - 10, height - 10),
    (0, 0, 255),
    -1
)

cv2.imshow("Four Colored Boxes", image)

cv2.waitKey(0)
cv2.destroyAllWindows()