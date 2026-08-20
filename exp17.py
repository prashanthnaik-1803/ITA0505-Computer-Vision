import cv2

# Read image
image = cv2.imread("sample.jpg")

if image is None:
    print("Error: Image not found")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Sobel X
sobel_x = cv2.Sobel(
    gray,
    cv2.CV_64F,
    1,
    0,
    ksize=3
)

# Sobel Y
sobel_y = cv2.Sobel(
    gray,
    cv2.CV_64F,
    0,
    1,
    ksize=3
)

# Convert to absolute values
sobel_x = cv2.convertScaleAbs(sobel_x)
sobel_y = cv2.convertScaleAbs(sobel_y)

# Combine X and Y
sobel = cv2.addWeighted(
    sobel_x,
    0.5,
    sobel_y,
    0.5,
    0
)

cv2.imshow("Original Image", image)
cv2.imshow("Sobel X", sobel_x)
cv2.imshow("Sobel Y", sobel_y)
cv2.imshow("Sobel Edge Detection", sobel)

cv2.waitKey(0)
cv2.destroyAllWindows()