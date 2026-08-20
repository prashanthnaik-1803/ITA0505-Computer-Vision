import cv2

image = cv2.imread("sample.jpg")

if image is None:
    print("Error: Image not found")
    exit()

# Rotate 270 degrees clockwise
rotated = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow("Original Image", image)
cv2.imshow("270 Degree Clockwise", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()