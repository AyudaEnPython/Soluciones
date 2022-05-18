"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from PIL import Image
from matplotlib import pyplot as plt

img = Image.open('assets/logo.png')
img.thumbnail((64, 64), Image.ANTIALIAS)
plt.imshow(img, interpolation="bicubic")
plt.axis("off")
plt.show()