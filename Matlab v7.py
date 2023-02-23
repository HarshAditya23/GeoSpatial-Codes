# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 21:37:25 2023

@author: gaurh
"""

import scipy.io as sio #From v4 to v7.2 matlab files

mat = sio.loadmat('data.mat')
print(mat.keys())
print(type(mat))
print(len(mat))
x = mat.get('data')
print(x)

import h5py as h5 #From v7.3 matlab files

mat_v7 = h5.File('')
print(mat.keys())
print(type(mat_v7))
print(len(mat_v7))
y = mat_v7.get('')
print(y)
