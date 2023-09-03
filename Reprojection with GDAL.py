# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 09:55:18 2022

@author: gaurh
"""

import os
from osgeo import gdal

input_folder = r''
output_folder = r''

for filename in os.listdir(input_folder):
    
    if filename.endswith('.tif'):
        input_path = os.path.join(input_folder, filename)
        ds = gdal.Open(input_path)
        output_filename = f"Reprojected_{os.path.splitext(filename)[0]}.tif"
        output_path = os.path.join(output_folder, output_filename)
        dsReprj = gdal.Warp(output_path, ds, dstSRS = "EPSG:4326")
        print(f"Reprojected and saved for {filename}")
        
print("Batch processing complete.")