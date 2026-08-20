import cv2
import numpy as np

# Read image
image = cv2.imread("sample.jpg")

if image is None:
    print("Error: Image not found")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convert to float32
gray = np.float32(gray)

# Harris Corner Detection
corners = cv2.cornerHarris(
    gray,
    blockSize=2,
    ksize=3,
    k=0.04
)

# Mark corners
image[corners > 0.01 * corners.max()] = [0, 0, 255]

cv2.imshow("Harris Corners", image)

cv2.waitKey(0)
cv2.destroyAllWindows()