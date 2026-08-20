import cv2
import numpy as np

# Create white image
image = np.ones(
    (500, 500, 3),
    dtype=np.uint8
) * 255

# Draw circle
cv2.circle(
    image,
    (250, 250),
    100,
    (255, 0, 0),
    3
)

cv2.imshow("Circle", image)

cv2.waitKey(0)
cv2.destroyAllWindows()