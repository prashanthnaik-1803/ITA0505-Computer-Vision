import cv2
import numpy as np

# Read image
image = cv2.imread("sample.jpg")

if image is None:
    print("Error: Image not found")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create kernel
kernel = np.ones((5, 5), np.uint8)

# Apply Black Hat
black_hat = cv2.morphologyEx(
    gray,
    cv2.MORPH_BLACKHAT,
    kernel
)

# Display images
cv2.imshow("Original Image", gray)
cv2.imshow("Black Hat Operation", black_hat)

cv2.waitKey(0)
cv2.destroyAllWindows()