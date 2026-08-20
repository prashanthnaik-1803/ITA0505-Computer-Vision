import cv2
import numpy as np

image = cv2.imread("sample.jpg")

if image is None:
    print("Error: Image not found")
    exit()

height, width = image.shape[:2]

# Source points
src_points = np.float32([
    [0, 0],
    [width - 1, 0],
    [width - 1, height - 1],
    [0, height - 1]
])

# Destination points
dst_points = np.float32([
    [50, 50],
    [width - 50, 0],
    [width - 1, height - 50],
    [0, height - 1]
])

# Calculate perspective matrix
matrix = cv2.getPerspectiveTransform(
    src_points,
    dst_points
)

# Apply transformation
result = cv2.warpPerspective(
    image,
    matrix,
    (width, height)
)

cv2.imshow("Original Image", image)
cv2.imshow("Perspective Transformation", result)

cv2.waitKey(0)
cv2.destroyAllWindows()