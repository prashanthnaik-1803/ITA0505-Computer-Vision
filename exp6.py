import cv2
import numpy as np

# Read the image
image = cv2.imread("sample.jpg")

# Check whether image is loaded
if image is None:
    print("Error: Image not found")
    exit()

# Create kernel
kernel = np.ones((5, 5), np.uint8)

# Apply erosion
eroded_image = cv2.erode(image, kernel, iterations=1)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Eroded Image", eroded_image)

cv2.waitKey(0)
cv2.destroyAllWindows() 