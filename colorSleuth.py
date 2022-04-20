"""
This python script analyzes an image and returns a list of hex codes of all the unique colors in the image.

Steps:
Step 1: load the image (using PIL)

Step 2: store the image in a 3 dimensional numpy array (height, width, color_channel)

Step 3: check for duplicate hex codes

Step 4: print the list of unique hex codes

"""

import numpy as np
from PIL import Image

# The input image file path.
input_image_path = 'samples/image_6.jpg'

# Loading the input image using PIL
input_image = Image.open(input_image_path)

"""
Image Validation Stage:
The input image mode must be RGB.
"""

# Validating image mode.
if input_image.mode != "RGB":
    print("Error: Input image mode is not RGB.")
    exit(1)

# Convert the image loaded using PIL into a numpy array and store its height, width, and number of channels.
image_array = np.asarray(input_image)
image_height, image_width, image_channels = image_array.shape

# Reshape the 3 dimensional array into a 2 dimensional array.
image_array = image_array.reshape((1, image_height * image_width, 3))

# List to keep track of hex codes.
unique_hex_codes = []

# Computing the hex code for each cell.
print("\nHex codes: \n")
for column in image_array[0]:
    hex_code = "#"

    # Concatenating the hex values of each channel.
    for channel in (0, 1, 2):
        # Splicing the result of the hex() method with [2:] to remove the leading "0x".
        # Then converting to uppercase.
        # Prepending a "0" if the hex value is a single digit (i.e. its decimal value is < 16).
        hex_code += ("0" if (column[channel] < 16) else "") + hex(column[channel])[2:].upper()

    if hex_code not in unique_hex_codes:
        # Store the hex code.
        unique_hex_codes.append(hex_code)
        # Directly print the hex code to the terminal.
        print(hex_code)
print("\nCompleted Task!")
