import numpy as np
import imageio
import math
# get_char(image_pixel, end):
# This function gets the last bit of all color channel in a pixel
# Parameters:
#   image_pixel -> a pixel
#   end -> just a flag to ignore the blue channel in last pixel
# Return:
#   bin_char -> string of bits
def get_char(image_pixel, end):
    r = bin(image_pixel[0])[2:].zfill(8) # r channel in binary
    g = bin(image_pixel[1])[2:].zfill(8) # g channel in binary
    b = bin(image_pixel[2])[2:].zfill(8) # b channel in binary

    bin_char =""
    bin_char += r[7] # Getting the last bit
    bin_char += g[7] # Getting the last bit
    if(end != -1): # if is not the last pixel's blue channel
        bin_char += b[7] # Getting the last bit

    return bin_char


# lsb_decode(image):
# This function find the hidden message in an image
# Parameters:
#   image -> image after steganography
# Return:
#   message -> hidden message
def lsb_decode(image):
    (height, width) = image.shape[0:2]
    message = ""
    bin = ""
    char = 0
    for i in range(height):
        for j in range(0, width-3, 3):
            bin += get_char(image[i, j], 7) # Getting the last bit, of all color channel
            bin += get_char(image[i, j + 1], 7) # Getting the last bit, of all color channel
            bin += get_char(image[i, j + 2], -1) # Getting the last bit, of all color channel
            if(chr(int(bin, 2)) == '|'): # Checking EOF
                return message
            message += chr(int(bin, 2)) # Convert the binary string in char
            bin = ""
            char = char + 1

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
