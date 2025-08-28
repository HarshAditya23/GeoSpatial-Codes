# -*- coding: utf-8 -*-
"""
Created on Wed Aug 20 11:49:26 2025

@author: BR-WS3
"""
import os
import spectral
import numpy as np
from osgeo import gdal

# Input & output directories
input_dir = ""
output_dir = ""

# Number of bands in each cube
num_bands = 15

# Create band-wise folders
for b in range(1, num_bands + 1):
    os.makedirs(os.path.join(output_dir, f"Band{b}"), exist_ok=True)

# Process each ENVI file
for file in os.listdir(input_dir):
    if file.endswith(".hdr"):   # only open hdr, it links to img
        filepath = os.path.join(input_dir, file)
        base_name = os.path.splitext(file)[0]

        # Open with spectral (handles BIP automatically)
        cube = spectral.envi.open(filepath)

        # Extract bands one by one
        for b in range(num_bands):
            band_array = cube.read_band(b)  # 0-indexed numpy array

            # Normalize to 8-bit (0–255) for JPEG
            arr_min, arr_max = band_array.min(), band_array.max()
            if arr_max > arr_min:  # avoid divide by zero
                scaled = ((band_array - arr_min) / (arr_max - arr_min) * 255).astype(np.uint8)
            else:
                scaled = (band_array * 0).astype(np.uint8)

            # Output path
            out_path = os.path.join(output_dir, f"Band{b+1}", f"{base_name}_B{b+1}.jpg")

            # --- FIX: Use MEM + CreateCopy instead of Create ---
            mem_driver = gdal.GetDriverByName("MEM")
            rows, cols = scaled.shape
            mem_ds = mem_driver.Create("", cols, rows, 1, gdal.GDT_Byte)
            mem_ds.GetRasterBand(1).WriteArray(scaled)

            jpeg_driver = gdal.GetDriverByName("JPEG")
            out_ds = jpeg_driver.CreateCopy(out_path, mem_ds, options=["QUALITY=100"])

            mem_ds = None
            out_ds = None

print("✅ All ENVI cubes processed! Each band saved as JPEG (quality=100).")

