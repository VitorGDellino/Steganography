import numpy as np
import imageio
import math
import binascii

def char_to_bin(txt):
    bin_txt = []
    for eachline in txt:
        for eachchar in eachline:
            bin_txt.append(bin(ord(eachchar))[2:].zfill(8))

    return bin_txt

def lsb(image):
    None

image_name = str(input()).rstrip()
txt_name = str(input()).rstrip()

image = imageio.imread("./images/"+image_name)
txt = open("./txt/"+txt_name, 'r')

print("----Text in binary----")
bin_txt = char_to_bin(txt)
print(bin_txt)
print("----Colorful image----")
print(image)
