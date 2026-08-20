import cv2

# Read image
image = cv2.imread("sample.jpg")

if image is None:
    print("Error: Image not found")
    exit()

# Select ROI
roi = image[50:200, 50:200]

# Copy ROI
copied_roi = roi.copy()

# Paste ROI at another location
image[250:400, 250:400] = copied_roi

# Display
cv2.imshow("Original / Pasted Image", image)
cv2.imshow("Cropped ROI", roi)

cv2.waitKey(0)
cv2.destroyAllWindows()