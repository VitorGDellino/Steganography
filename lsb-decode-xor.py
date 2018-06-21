import numpy as np
import imageio
import math

def xor(a, b):
    return (a or b) and not (a and b)

# get_char(image_pixel, end):
# This function gets the last bit of all color channel in a pixel
# Parameters:
#   image_pixel -> a pixel
#   end -> just a flag to ignore the blue channel in last pixel
# Return:
#   bin_char -> string of bits
def get_char(image_pixel):
    r = bin(image_pixel[0])[2:].zfill(8) # r channel in binary
    g = bin(image_pixel[1])[2:].zfill(8) # g channel in binary
    b = bin(image_pixel[2])[2:].zfill(8) # b channel in binary

    bin_char = xor(int(r[7]), xor(int(g[7]), int(b[7])))

    return str(int(bin_char))


# lsb_decode(image):
# This function find the hidden message in an image
# Parameters:
#   image -> image after steganography
# Return:
#   message -> hidden message
def lsb_decode(image):
    (height, width) = image.shape[0:2]
    message = ""
    for i in range(height):
        for j in range(0, width-8, 8):
            bin = ""
            for k in range(8):
                bin += get_char(image[i, j+k]) # Getting the last bit, of all color channel
            char = chr(int(bin, 2))
            if(char == '|'): # Checking EOF
                return message
            message += char # Add the char into the image

    return message

# Input image name and text name for output
image_name = str(input()).rstrip()
txt_name = str(input()).rstrip()

# Reading the image
image = imageio.imread("./images/"+image_name)

# Creating a file with the found message
txt = open("./txt/"+txt_name+"-out", 'w')

# Finding the message
message = lsb_decode(image)

# Writing in the file
txt.write(message)

# Closing file
txt.close()
