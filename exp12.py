import cv2

image = cv2.imread("sample.jpg")

if image is None:
    print("Error: Image not found")
    exit()

# Rotate 180 degrees
rotated = cv2.rotate(image, cv2.ROTATE_180)

cv2.imshow("Original Image", image)
cv2.imshow("180 Degree Rotation", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()