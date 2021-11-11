"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Documentación oficial de matplotlib:
https://matplotlib.org/stable/tutorials/introductory/images.html
"""
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('assets/logo.png')
R, G, B = img[:,:,0], img[:,:,1], img[:,:,2]
img_gray = 0.2989 * R + 0.5870 * G + 0.1140 * B

plt.imshow(img_gray, cmap='gray')
plt.show()