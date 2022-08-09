import cv2
import numpy as np

def preprocess_image(img):
    """
    The function preprocess_image will first convert the colourful image into
    grayscale so that it is easy for us to extract text, then it resizes the
    image so that we can focus more on the divisions we create(it works as
    zooming an image) --> fx and fy are the dimensions for resize and interpolation
    refers to the additional gap created when resizing is being filled with the mid
    value of range 0 to 255 so that we don't see gap...

    Now we apply adaptive_threshold where 61 is block_size and 11 is constant c
    """

    gray = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)

    processed_image = cv2.adaptiveThreshold(
        resized,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        61,
        11
    )

    return processed_image