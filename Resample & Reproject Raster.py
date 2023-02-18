# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 09:55:18 2022

@author: HarshAditya23
"""

from osgeo import gdal
import numpy as np

ds = gdal.Open("dem.tif")

# reproject
dsReprj = gdal.Warp("demReprj.tif", ds, dstSRS = "EPSG:4326")

# resample
dsRes = gdal.Warp("demRes.tif", ds, xRes = 150, yRes = 150, resampleAlg = "bilinear")
