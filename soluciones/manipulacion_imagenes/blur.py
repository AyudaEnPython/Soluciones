from matplotlib import pyplot as plt
"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from PIL import Image

img = Image.open('assets/logo.png')
img.thumbnail((64, 64), Image.ANTIALIAS)
plt.imshow(img, interpolation="bicubic")
plt.axis("off")
plt.show()