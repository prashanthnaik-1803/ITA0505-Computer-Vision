import cv2
import numpy as np

# Create white image
image = np.ones(
    (500, 500, 3),
    dtype=np.uint8
) * 255

# Draw rectangle
cv2.rectangle(
    image,
    (100, 100),
    (400, 300),
    (0, 0, 255),
    3
)

cv2.imshow("Rectangle", image)

cv2.waitKey(0)
cv2.destroyAllWindows()