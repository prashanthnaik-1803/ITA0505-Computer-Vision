import cv2

# Full path of input video
input_video = ("video.mp4")

# Open input video
cap = cv2.VideoCapture(input_video)

if not cap.isOpened():
    print("Cannot open video!")
    exit()

# Get original FPS
fps = cap.get(cv2.CAP_PROP_FPS)

if fps <= 0:
    fps = 30

# Store frames
frames = []

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frames.append(frame)

cap.release()

# Check frames
if len(frames) == 0:
    print("No frames found!")
    exit()

print("Total frames:", len(frames))
print("FPS:", fps)

# Get video size
height, width, _ = frames[0].shape

# Output file
output_video = "reverse_video.avi"
# Create AVI video using MJPG codec
fourcc = cv2.VideoWriter_fourcc(*"MJPG")

out = cv2.VideoWriter(
    output_video,
    fourcc,
    fps,
    (width, height)
)

# Check output video
if not out.isOpened():
    print("Cannot create output video!")
    exit()

# Write frames in reverse
for frame in reversed(frames):
    out.write(frame)

# Release
out.release()

print("Reverse video created successfully!")
print("Saved at:")
print(output_video)