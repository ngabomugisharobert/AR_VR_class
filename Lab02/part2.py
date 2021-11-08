# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 11:11:40 2021

@author: King
"""


from matplotlib import pyplot as plt
import pandas as pd
from PIL import Image
import numpy as np
import scipy
import scipy.signal
from scipy import linalg, matrix
from scipy.interpolate import  griddata
import seaborn as sns
import math

stars_data = pd.read_csv("star_data_lots.csv")

new_img = Image.new('RGB', (800,800))

img = np.zeros((800,800),np.uint8)

ra = stars_data['ra']
dec = stars_data['dec']
mag = stars_data['mag']

c = 202.45
m = -36.49

longitude = 360 -(ra * 15)
latitude = -dec

long_const = 0
long_mag = 2.22

lat_const = 400
lat_mag = 4.44

lat = np.round(latitude*lat_mag + lat_const)
long = np.round(longitude*long_mag + long_const)

intensity = np.round(mag*m +c)

a = stars_data.shape[0]

for i in range(stars_data.shape[0]):
    img[int(lat[i]),int(long[i])] = int(intensity[i])
    
#img2 = Image.fromarray(img)
#img.save('my.png')

#convk = np.asarray([(0.0,0.5,0.0), (0.5,1.0,0.5), (0.0,0.5,0.0)], np.float32)
#imdat = signal.convolved2d(imdat, convk)

final = Image.fromarray(img.astype(np.uint8))
final.show()
final.save("final.png",format="png")