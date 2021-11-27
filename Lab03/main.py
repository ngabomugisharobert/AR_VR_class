
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 18:27:38 2021

@author: King
"""


import sys
import warnings
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import block_reduce

warnings.filterwarnings("ignore")


pilim = Image.open("Rwanda_SRTM30meters.tif")
img = np.asarray(pilim,np.uint16)
print (f"image shape is {img.shape}")
R = img.shape[0]
C = img.shape[1]
min_el = img.min()
max_val = img.max()
datf = img.astype(np.float)
print(f"minimum elevation is " + str( np.amin( datf ) ) )
print(f"maximum value is " + str( np.amin( datf ) ) )


max_vals = np.where(img == max_val)

for idx in range(len(max_vals[0])):
    img[max_vals[0][idx]][max_vals[1][idx]] = 0

max_el = img.max()
max_el

#rescale to 0.255
img_rescaled = img * ( 255/max_el)

img_rescaled_uint8 = img_rescaled.astype('uint8')
plt.imshow(img_rescaled_uint8)
plt.show()

#result = Image.fromarray(img_rescaled_uint8)
#result.save('rwanda.jpeg')


img_rescaled_subsampled = block_reduce(img_rescaled_uint8, block_size=(10,10), func=np.max)
plt.imshow(img_rescaled_subsampled)



