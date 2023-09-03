# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 20:27:36 2023

@author: gaurh
"""

# Import the Libraries
import os
import glob
import rasterio
import numpy as np

# Function to calculate NDVI
def calculate_ndvi(red_band, nir_band):
    ndvi = (nir_band - red_band) / (nir_band + red_band)
    return ndvi

# Function to mask NoData values
def mask_nodata(array, nodata_value):
    return np.ma.masked_equal(array, nodata_value)

# Input the Data Folder
path = r'D:\sentinel-2\*.tif*'

for file in glob.glob(path):
   # Open the image using rasterio
    with rasterio.open(file) as src:
        red_band = src.read(3)
        nir_band = src.read(4)  

        # Get the NoData value from the metadata
        nodata_value = src.nodata

        # Mask NoData values
        red_band_masked = mask_nodata(red_band, nodata_value)
        nir_band_masked = mask_nodata(nir_band, nodata_value)

        # Calculate NDVI
        ndvi = calculate_ndvi(red_band_masked, nir_band_masked)

        # Create an output directory if it doesn't exist
        output_dir = r'D:\Spectral_Indice'
        os.makedirs(output_dir, exist_ok=True)

        # Save the NDVI result as a new GeoTIFF file
        output_path = os.path.join(output_dir, f'ndvi_{1}')
        profile = src.profile
        profile.update(driver='GTiff', dtype=rasterio.float32, count=1)
        with rasterio.open(output_path, 'w', **profile) as dst:
            dst.write(ndvi, 1)

print("NDVI calculation and saving completed.")
