import numpy as np
import cv2 as cv

img = cv.imread('img.jpg', 0)
print(img)

np.savetxt(delimiter=",", fname='img.csv', fmt='% 1.1i', X=img)
