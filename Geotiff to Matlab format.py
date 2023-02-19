# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 23:21:44 2023

@author: gaurh
"""


#conversion code

from osgeo import gdal
from osgeo.gdal_array import DatasetReadAsArray
import scipy.io as sio

Data = gdal.Open('2013_IEEE_GRSS_DF_Contest_CASI.tif')
Data = DatasetReadAsArray(Data)
sio.savemat('Conversion.mat', {'Data': Data})
