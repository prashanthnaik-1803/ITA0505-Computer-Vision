import cv2
import matplotlib.pyplot as plt

def analyze_histogram(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Check if the image is loaded
    if image is None:
        print("Error: Image not found!")
        return

    # Color channels
    color_channels = ('b', 'g', 'r')

    # Create a figure
    plt.figure(figsize=(10, 5))

    # Calculate and plot histogram for each color channel
    for i, color in enumerate(color_channels):
        histogram = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(histogram, color=color, label=color.upper() + " Channel")

    # Add title and labels
    plt.title("Color Histogram Analysis")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.xlim([0, 256])
    plt.legend()

    # Save histogram as an image
    plt.savefig("histogram.png")
    print("Histogram saved as histogram.png")

# Call the function
analyze_histogram("travel.jpg")