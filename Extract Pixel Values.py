# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 16:14:42 2023

@author: gaurh
"""

import glob
import rasterio as rio
import geopandas as gpd

SHP= gpd.read_file(r'C:\Users\gaurh\codes_and_data\shapefile\Sugarcane.shp')
path = r'C:\Users\gaurh\codes_and_data\Sentinel-1\*.tif*'

for file in glob.glob(path):
    ndvi = rio.open(file)
    saveme = open(file.replace('tif', 'txt'), 'w')
    for point in SHP['geometry']:
        x = point.xy[0][0]
        y = point.xy[1][0]
        row, col = ndvi.index(x,y)
        print(point, file=saveme)
        print(row,col, file=saveme)
        print(ndvi.read(1)[row,col], file=saveme)
    saveme.close()