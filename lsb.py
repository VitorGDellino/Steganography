import numpy as np
import imageio
import math
import matplotlib.pyplot as plt

# char_to_bin(txt)
# This function tranforms the ascii txt into binary txt
# Parameters:
#   txt -> txt in ascii
# Return:
#   bin_txt -> txt in binary
def char_to_bin(txt):
    bin_txt = []
    for eachline in txt:
        for eachchar in eachline:
            bin_txt.append(bin(ord(eachchar))[2:].zfill(8))

    return bin_txt

# change_pixel(image_pixel, char, start, end)
# This function changes the image pixel
# Parameters:
#   image -> original image pixel
#   char -> char in binary that is gonna be hided
#   start -> char start
#   end -> char end
# Return:
#   pixel -> adulterated pixel
def change_pixel(image_pixel, char, start, end):
    pixel = np.zeros(3, np.uint8)
    r = bin(image_pixel[0])[2:].zfill(8) # r channel in binary
    g = bin(image_pixel[1])[2:].zfill(8) # g channel in binary
    b = bin(image_pixel[2])[2:].zfill(8) # b channel in binary

    r = r[0:7] + char[start] # changing the last bit
    g = g[0:7] + char[start + 1] # changing the last bit
    if(end != 8):
        b = b[0:7] + char[end] # changing the last bit

    # creating the new pixel
    pixel[0] = int(r, 2)
    pixel[1] = int(g, 2)
    pixel[2] = int(b, 2)


    return pixel

# lsd(image, bin_txt, height, width, txt_size)
# This function perform the lsb
# Parameters:
#   image -> image(original) before steganography
#   bin_txt -> txt converted to binary
#   height -> image's height
#   width -> image's width
#   txt_size -> size of bin_txt
# Return:
#   steg_image
def lsb(image, bin_txt, height, width, txt_size):
    char = 0
    for i in range(height):
        for j in range(0, width-3, 3):
            if(char >= len(bin_txt)): # Testing if the entire txt was hided
                return image
            image[i, j] = change_pixel(image[i, j], bin_txt[char], 0, 3) # input the bits
            image[i, j+1] = change_pixel(image[i, j+1], bin_txt[char], 3, 6) # input the bits
            image[i, j+2] = change_pixel(image[i, j+2], bin_txt[char], 6, 8) # input the bits
            char = char + 1

    return image

# steganography(image, bin_txt, payload)
# This function just check if the txt fits within image
# Parameters:
#   image -> image(original) before steganography
#   bin_txt -> txt converted to binary
#   payload -> size of bin_txt (in bytes)
# Return:
#   steg_image if the txt fits
#   A message "txt is too big for the image"
def steganography(image, bin_txt, payload):
    (height, width) = image.shape[0:2]
    max_txt_size = (height*width*3)/8
    if(max_txt_size >= payload): # Testing if the txt fits within image
        return lsb(image, bin_txt, height, width,len(bin_txt))
    else:
        return "txt is too big for the image"

# Input image name and text name
image_name = str(input()).rstrip()
txt_name = str(input()).rstrip()

# Reading the image and text
image = imageio.imread("./images/"+image_name)
txt = open("./txt/"+txt_name, 'r')

# Transform the ascii txt into binary
bin_txt = char_to_bin(txt)

# Calculating txt size
payload = len(bin_txt)*8

# Closing file
txt.close()

# Performing steganography
steg_image = steganography(image, bin_txt, payload)

# Showing the original image and the steg image
plt.subplot(121)
plt.imshow(image)
plt.subplot(122)
plt.imshow(steg_image)
plt.show()

imageio.imwrite("./out/steg-" + image_name, steg_image)
