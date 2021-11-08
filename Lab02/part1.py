# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 18:39:53 2021

@author: King
"""


from matplotlib import pyplot as plt
import pandas as pd
from PIL import Image
import numpy as np
import scipy
from scipy import linalg, matrix
from scipy.interpolate import  griddata
import seaborn as sns
import math

orginal_img = Image.open('part1.jpg')

width, height = orginal_img.size

output_img = Image.new("RGB", (1024,1024),(0,0,0))

out_width, out_height = output_img.size

d = width
z = d
N = 1024
delta = 180/N


max_phi = math.atan(height/(2*d)) * (180/math.pi)
max_teta = math.atan(width/(2*d)) * (180/math.pi)


phi = np.linspace(-90,90,N)
teta = np.linspace(-90,90,N)

output_imgPix = output_img.load()
orginal_imgPix = orginal_img.load()


for i in np.linspace(-90,90,N):
    t=i
    for j in np.linspace(-90,90,N):
        p=j
        if p < max_phi and t < max_teta:
            r = z / (math.cos(math.radians(p)) * math.cos(math.radians(t)))
            
            x = r * (math.cos(math.radians(p)) * math.sin(math.radians(t)))
            
            y = r * (math.sin(math.radians(p)))
            
            pics_x = np.round(x + (height/2))
            pics_y = np.round(y + (width/2))
            
            if height > pics_x and width > pics_y:
                if pics_x > 0 and pics_y > 0:
                    i=t/delta
                    j=p/delta
                    output_imgPix[j+(out_height/2), i+(out_width/2)] = orginal_imgPix[pics_y,pics_x]

            
output_img.show()
            





