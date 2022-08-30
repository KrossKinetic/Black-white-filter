# Imageio library simplifies reading images, like removing headers
# imageio returns a numpy array
import imageio.v3 as iio
# PIL allows me to quickly remove alpha values
from PIL import Image
# numpy arrays are in general faster than python lists, good for reading 4k images
import numpy
from math import sqrt

def save(img):
    x = img
    namefnew = input("Enter new name of the file: ")
    while True:
        print("Choose extension to store file as: ")
        print("1.JPG (Alpha data will be lost, smaller file size)")
        print("2.PNG (Alpha data will be retained, larger file size)")
        temp1 = input("Choose 1 or 2 ?: ")
        if temp1 == "1":
            img = Image.fromarray(img).convert("RGB")
            img = numpy.array(img)
            newext = ".jpg"
            break
        elif temp1 == "2":
            newext = ".png"
            break
        print("That is not an option. Please try again.")
    newname = namefnew + newext
    iio.imwrite(newname,img)

def bw(img):
    for i in img:
        for j in i:
            avgColor = (int(j[0]) + int(j[1]) + int(j[2]))/3 
            j[0] = avgColor
            j[1] = avgColor
            j[2] = avgColor

nameold = str(input("Enter name of the file with the file extension: "))
temp1 = iio.imread(nameold)
img = temp1.copy()
height = img.shape[0]
width = img.shape[1]
type = img.shape[2]
print()
bw(img)
save(img)