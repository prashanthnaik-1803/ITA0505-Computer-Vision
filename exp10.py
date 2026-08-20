import cv2

# Read image
image = cv2.imread("sample.jpg")

if image is None:
    print("Error: Image not found")
    exit()

# Get original dimensions
height, width = image.shape[:2]

# Resize to bigger size
bigger = cv2.resize(
    image,
    (width * 2, height * 2),
    interpolation=cv2.INTER_LINEAR
)

# Resize to smaller size
smaller = cv2.resize(
    image,
    (width // 2, height // 2),
    interpolation=cv2.INTER_AREA
)

# Display
cv2.imshow("Original Image", image)
cv2.imshow("Bigger Image", bigger)
cv2.imshow("Smaller Image", smaller)

cv2.waitKey(0)
cv2.destroyAllWindows()