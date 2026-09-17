import cv2

image = cv2.imread("image.jpg")

watermark = "MY WATERMARK"

font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_thickness = 2
color = (0, 0, 255)

position = (50, 50)

watermarked_image = image.copy()

cv2.putText(
    watermarked_image,
    watermark,
    position,
    font,
    font_scale,
    color,
    font_thickness
)

cv2.imshow("Original Image", image)
cv2.imshow("Watermarked Image", watermarked_image)

cv2.imwrite(
    "watermarked_image.jpg",
    watermarked_image
)

cv2.waitKey(0)
cv2.destroyAllWindows()
