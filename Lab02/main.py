# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 11:11:40 2021

@author: King
"""

"""
The concept of the assignment is to generate night stars all around you using the concept of a round earth.. so the Perkins wants you to convert a flat surface into a sphere.
from the previous assignment, the start_data excel sheet 
has 4 columns, but the last 3 columns represent decimeter, radius and magnitude(you can confirm with your TA).

in plotting these starts you need 3 main variables, which are:1. longitude 
2. latitude 
3. intensity 

longitude = 360 -(rad*15)
latitude = -dec 
the intensity is within a range of -1.44 to 5 and we want to convert them to pixels according to the assignment.
so from the assignment -1.44 maps to 255pixels and 5 maps to 20 pixels.
from the interpolation the new intensity(I) = mag*m +c, where the m is gradient and c is constant you get from interpolating the mappings above.

ra = right ascension (hours); convert to longitude via 15*ra (will be 0 to 360)
 dec = declination (degrees) = “latitude” (-90 to 90)
mag = magnitude (the brightness of the star)
"""

from matplotlib import pyplot as plt
import pandas as pd
from PIL import Image
import numpy as np
import scipy
from scipy import linalg, matrix
from scipy.interpolate import  griddata
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
latitude =-dec

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

final = Image.fromarray(img.astype(np.uint8))
final.show()
