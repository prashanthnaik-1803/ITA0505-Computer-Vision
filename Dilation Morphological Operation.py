import cv2
import numpy as np

image = cv2.imread("image.jpg")

gray = cv2.cvtColor(
    image,
    cv2.COLOR_BGR2GRAY
)

kernel = np.ones(
    (5, 5),
    np.uint8
)

dilated_image = cv2.dilate(
    gray,
    kernel,
    iterations=1
)

cv2.imshow("Original Image", image)
cv2.imshow("Dilated Image", dilated_image)

cv2.imwrite(
    "dilated_image.jpg",
    dilated_image
)

cv2.waitKey(0)
cv2.destroyAllWindows()
