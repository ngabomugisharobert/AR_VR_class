# -*- coding: utf-8 -*-,
"""
Created on Fri Oct 29 20:50:57 2021

@author: King
"""


from matplotlib import pyplot as plt
from PIL import Image
import numpy as np
import scipy
from scipy import linalg, matrix
from scipy.interpolate import  griddata



original_img = Image.open("PC_test_1.jpg")

new_img = Image.new('RGB', (800,800))

img = original_img.load()
img2 = new_img.load()

points_original = np.array([[229,240],[360,240],[597,615],[48,618]])

Points_new = np.array([[0,800],[800,800],[800,0],[0,0]])

A = np.array([
        [points_original[0][0], points_original[0][1], 1 , 0, 0, 0, -Points_new[0][0]*points_original[0][0], -Points_new[0][0]*points_original[0][1]],
        [0,0,0,points_original[0][0], points_original[0][1],1 , -Points_new[0][1]*points_original[0][0], -Points_new[0][1]*points_original[0][1]],
        
        [points_original[1][0], points_original[1][1], 1 , 0, 0, 0, -Points_new[1][0]*points_original[1][0], -Points_new[0][0]*points_original[1][1]],
        [0,0,0,points_original[1][0], points_original[1][1],1 , -Points_new[1][1]*points_original[1][0], -Points_new[0][1]*points_original[1][1]],
        
        [points_original[2][0], points_original[2][1], 1 , 0, 0, 0, -Points_new[2][0]*points_original[2][0], -Points_new[2][0]*points_original[2][1]],
        [0,0,0,points_original[2][0], points_original[2][1],1 , -Points_new[2][1]*points_original[2][0], -Points_new[0][1]*points_original[2][1]],
        
        [points_original[3][0], points_original[3][1], 1 , 0, 0, 0, -Points_new[3][0]*points_original[3][0], -Points_new[3][0]*points_original[3][1]],
        [0,0,0,points_original[3][0], points_original[3][1],1 , -Points_new[3][1]*points_original[3][0], -Points_new[3][1]*points_original[3][1]]
    ])

B = np.array([[Points_new[0][0]], [Points_new[0][1]], [Points_new[1][0]], [Points_new[1][1]], [Points_new[2][0]], [Points_new[2][1]], [Points_new[3][0]], [Points_new[3][1]]])

h = np.dot(np.linalg.inv(A),B)

H = np.append(h,1).reshape(3,3)

for i in range(800):
    for j in range(800):
        result = np.dot(np.linalg.inv(H), np.array([i, j, 1]))
        a = np.round(result[0]/result[2])
        b = np.round(result[1]/result[2])
        if original_img.size[0] > a and original_img.size[1] > b:
            img2[i,j] =img[a,b]
        
new_img.save("output.png",format="png")