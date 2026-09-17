import cv2

image = cv2.imread("image.jpg")

# Crop a region of interest
roi = image[100:300, 100:300]

# Create a copy of the ROI
copied_roi = roi.copy()

# Create a copy of the original image
result = image.copy()

# Paste the copied ROI to another location
result[300:500, 300:500] = copied_roi

cv2.imshow("Original Image", image)
cv2.imshow("Cropped ROI", roi)
cv2.imshow("Copied and Pasted Image", result)

cv2.imwrite("cropped_roi.jpg", roi)
cv2.imwrite("roi_pasted.jpg", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
