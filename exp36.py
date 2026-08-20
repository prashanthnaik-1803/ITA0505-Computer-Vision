import cv2

image = cv2.imread("image1.jpg")

if image is None:
    print("Image not found!")
    exit()

# Convert BGR to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Example: detect green background
lower = (35, 40, 40)
upper = (85, 255, 255)

# Create mask
mask = cv2.inRange(
    hsv,
    lower,
    upper
)

# Remove background
result = cv2.bitwise_and(
    image,
    image,
    mask=mask
)

cv2.imshow("Original", image)
cv2.imshow("Background Mask", mask)
cv2.imshow("Background Color", result)

cv2.waitKey(0)
cv2.destroyAllWindows()