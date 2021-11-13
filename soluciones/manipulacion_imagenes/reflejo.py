"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from PIL import Image
from PIL import ImageOps
from matplotlib import pyplot as plt

im = Image.open("assets/logo.png")
img = ImageOps.mirror(im)

for j, i in enumerate((im, img)):
    plt.subplot(1, 2, j+1)
    plt.imshow(i)
    plt.axis('off')
plt.subplots_adjust(wspace=0)
plt.show()