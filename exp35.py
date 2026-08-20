import cv2
import numpy as np

# Create white image
image = np.ones(
    (500, 800, 3),
    dtype=np.uint8
) * 255

# Get text from user
text = input("Enter text: ")

# Display text
cv2.putText(
    image,
    text,
    (50, 250),
    cv2.FONT_HERSHEY_SIMPLEX,
    2,
    (0, 0, 255),
    3
)

cv2.imshow("Text on Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()