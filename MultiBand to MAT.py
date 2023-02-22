# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 09:55:18 2022
@author: HarshAditya23
"""

#Conversion Multi-Band Tiff to MATLAB Format
import scipy.io as sio
from osgeo import gdal
from osgeo.gdal_array import DatasetReadAsArray

roi = gdal.Open(r"C:\Users\mrg21-021411956\Desktop\roi.tif")
roi = DatasetReadAsArray(houston).astype('uint32')

print(rio.shape)
rio = rio.transpose(1, 2, 0)

print(rio.shape)

sio.savemat('roi.mat', {'ROI': roi})

#Print MATLAB file keys
import scipy.io as sio
import numpy as np

m = sio.loadmat('roi.mat')

print(m.keys())
print(np.shape(m['ROI']))
print(m['ROI'])
