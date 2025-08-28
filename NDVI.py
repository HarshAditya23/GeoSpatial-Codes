# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 17:17:49 2025

@author: BR-WS3
"""

import os
import rasterio
import matplotlib.pyplot as plt
from glob import glob

def calculate_ndvi(nir_band, red_band):
    """
    Calculate NDVI from NIR and Red bands.
    NDVI = (NIR - Red) / (NIR + Red)
    """
    return (nir_band - red_band) / (nir_band + red_band)

def process_rasters(input_dir, output_dir):
    # Get all TIFF files in the input directory
    raster_files = glob(os.path.join(input_dir, '*.tif'))
    
    for raster_file in raster_files:
        with rasterio.open(raster_file) as src:
            # Read the bands: Assuming bands 3 (Red) and 4 (NIR)
            red_band = src.read(4)  # Band 3 (Red)
            nir_band = src.read(5)  # Band 4 (NIR)
            
            # Calculate NDVI
            ndvi = calculate_ndvi(nir_band, red_band)
            
            # Define the output file path
            output_file = os.path.join(output_dir, os.path.basename(raster_file).replace('.tif', '_VI.tif'))
            
            # Write the NDVI output to a new raster file
            with rasterio.open(output_file, 'w', driver='GTiff',
                               count=1, dtype='float32', crs=src.crs, transform=src.transform,
                               width=src.width, height=src.height) as dst:
                dst.write(ndvi, 1)
        
        print(f"Processed NDVI for {raster_file}")

# Example usage
input_directory = r""  # Directory where your TIFF files are stored
output_directory = r""  # Directory where NDVI rasters will be saved

process_rasters(input_directory, output_directory)
