# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 17:17:35 2023

@author: gaurh
"""

from osgeo import gdal

# Open the ENVI file
def convert_envi_to_tiff(envi_file, tiff_file):
    dataset = gdal.Open(envi_file)
    if dataset is None:
        print("Error: Could not open the ENVI file.")
        return

    # Create a new TIFF file
    driver = gdal.GetDriverByName("GTiff")
    tiff_dataset = driver.CreateCopy(tiff_file, dataset, 0)

    # Close the datasets
    dataset = None
    tiff_dataset = None
    print(f"Conversion complete. ENVI file '{envi_file}' converted to TIFF file '{tiff_file}'.")

input_envi_file = r"C:\Users\gaurh\Desktop\AVIRIS-NG (Jodhpur)\SID"
output_tiff_file = "output_file.tif"
convert_envi_to_tiff(input_envi_file, output_tiff_file)
