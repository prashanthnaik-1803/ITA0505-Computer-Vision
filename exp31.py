import cv2

image = cv2.imread("image1.jpg")

if image is None:
    print("Image not found!")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Threshold value
threshold_value = 127

_, segmented = cv2.threshold(
    gray,
    threshold_value,
    255,
    cv2.THRESH_BINARY
)

cv2.imshow("Original Image", image)
cv2.imshow("Segmented Image", segmented)

cv2.waitKey(0)
cv2.destroyAllWindows()