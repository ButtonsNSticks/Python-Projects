#! python3
# resizeAndAdLogo.py - Resizes all images in the current working directory to fit
# in a 300 x 3400 square, adds a catlogo.png to the lower right corner.

import os
from PIL import Image

square_fit_size = 300
logo_filename = "catlogo.png"

logo_image = Image.open(logo_filename)  # Open the logo
logo_width, logo_height = logo_image.size  # Get the logo image & height and assign to variables.

os.makedirs("with_logo", exist_ok=True)  # Make a folder for the updated images to go into.


# Loop over all files in the CWD

for filename in os.listdir("."):  # Loop over every file in current directory (NOT sub-folders!)

    if not (filename.endswith(".png") or filename.endswith(".jpg")) or filename == logo_filename:
        continue  # If the file being looked at is NOT a PNG or JPG image or is the logo image then SKIP it.

    image = Image.open(filename)  # Otherwise, open up the image.
    width, height = image.size  # Store the width and height

# Todo: Check if image needs to be resized.

if width > square_fit_size and height > square_fit_size:  # We only want to resize if image is larger than 300 x x300

    # Calculate the new width & height to resize to
    if width > height:
        height = int((square_fit_size/width) * height)
        width = square_fit_size

    else:
        width = int((square_fit_size/height) * width)
        height = square_fit_size

# Resize the image
    print("Resizing {}...".format(filename))
    image = image.resize((width, height))

# Add the logo

print("Adding the logo to {}".format(filename))

image.paste(logo_image, (width - logo_width, height - logo_height), logo_image)

# We want to put the logo in the BOTTOM RIGHT corner of the image.
# As the logo position is based on the (x,y) co-ords of the top left pixel, we need to place the logo
# at position x = width of image - logo_width & y = height - logo height.

# Also: the paste argument will NOT paste the transparent pixels in the logo UNLESS you specify the last
# "mask" argument, that's why we have logo_image twice.

# Save the changes

image.save(os.path.join("with_logo", filename))



