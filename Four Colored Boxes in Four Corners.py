import numpy as np
import cv2

def create_colored_corners(image_size):

    height, width = image_size

    image = np.ones(
        (height, width, 3),
        dtype=np.uint8
    ) * 255

    box_h = height // 10
    box_w = width // 10

    # Top-left: Black
    image[
        :box_h,
        :box_w
    ] = [0, 0, 0]

    # Top-right: Blue
    image[
        :box_h,
        -box_w:
    ] = [255, 0, 0]

    # Bottom-left: Green
    image[
        -box_h:,
        :box_w
    ] = [0, 255, 0]

    # Bottom-right: Red
    image[
        -box_h:,
        -box_w:
    ] = [0, 0, 255]

    cv2.imshow(
        "Colored Corners Image",
        image
    )

    cv2.waitKey(0)
    cv2.destroyAllWindows()


user_width = int(
    input("Enter image width: ")
)

user_height = int(
    input("Enter image height: ")
)

create_colored_corners(
    (user_height, user_width)
)
