import cv2

image = cv2.imread("image1.jpg")

if image is None:
    print("Image not found!")
    exit()

# Convert to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Select green color
lower = (35, 40, 40)
upper = (85, 255, 255)

# Detect foreground color
mask = cv2.inRange(
    hsv,
    lower,
    upper
)

# Extract foreground
foreground = cv2.bitwise_and(
    image,
    image,
    mask=mask
)

cv2.imshow("Original", image)
cv2.imshow("Foreground Mask", mask)
cv2.imshow("Foreground", foreground)

cv2.waitKey(0)
cv2.destroyAllWindows()