import cv2

# Read image
image = cv2.imread("simple.jpg")

if image is None:
    print("Image not found!")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create ORB detector
orb = cv2.ORB_create()

# Detect key points and descriptors
keypoints, descriptors = orb.detectAndCompute(gray, None)

# Draw key points
output = cv2.drawKeypoints(
    image,
    keypoints,
    None,
    color=(0, 255, 0),
    flags=0
)

print("Object Recognition Result")
print("Number of key points detected:", len(keypoints))

if len(keypoints) > 20:
    print("Watch object detected/recognized.")
else:
    print("Watch object could not be recognized clearly.")

cv2.imshow("Watch Recognition", output)

cv2.waitKey(0)
cv2.destroyAllWindows()