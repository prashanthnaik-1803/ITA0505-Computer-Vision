import cv2
import numpy as np

# Read the image
image = cv2.imread("sample.jpg")

# Check if image is loaded
if image is None:
    print("Error: Image not found")
    exit()

# Create a kernel
kernel = np.ones((5, 5), np.uint8)

# Apply erosion
eroded_image = cv2.erode(image, kernel, iterations=1)

# Display original image
cv2.imshow("Original Image", image)

# Display eroded image
cv2.imshow("Eroded Image", eroded_image)

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()