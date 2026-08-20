import cv2

# Read image
image = cv2.imread("sample.jpg")

if image is None:
    print("Error: Image not found")
    exit()

# Copy original image
watermarked = image.copy()

# Watermark text
text = "MY WATERMARK"

# Position
position = (50, 50)

# Font
font = cv2.FONT_HERSHEY_SIMPLEX

# Add watermark
cv2.putText(
    watermarked,
    text,
    position,
    font,
    1,
    (255, 255, 255),
    2,
    cv2.LINE_AA
)

# Display
cv2.imshow("Original Image", image)
cv2.imshow("Watermarked Image", watermarked)

cv2.waitKey(0)
cv2.destroyAllWindows()