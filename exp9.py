import cv2
import numpy as np

# Read image
image = cv2.imread("sample.jpg")

if image is None:
    print("Error: Image not found")
    exit()

# Create kernel
kernel = np.ones((5, 5), np.uint8)

# Apply dilation
dilated_image = cv2.dilate(image, kernel, iterations=1)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Dilated Image", dilated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()