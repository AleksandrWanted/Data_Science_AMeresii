import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

img = np.loadtxt(fname='img.csv', delimiter=",")

rotated = ndimage.rotate(img, 30, reshape=0)
plt.imsave(fname='new_img1.png', arr=rotated)
# plt.imshow(img)

sob = ndimage.sobel(img)
plt.imsave(fname='new_img2.png', arr=sob)

lx, ly = img.shape
crop = img[lx // 4: - lx // 4,
       ly // 4: - ly // 4]

plt.imsave(fname='new_img3.png', arr=crop)

blur = ndimage.gaussian_filter(img, sigma=30)
plt.imsave(fname='new_img4.png', arr=blur)
