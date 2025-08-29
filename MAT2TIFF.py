# -*- coding: utf-8 -*-
"""
Created on Thu Aug 28 23:04:59 2025

@author: gaurh
"""

import numpy as np
import rasterio
# from rasterio.transform import from_origin
from scipy import io

def mat_to_tiff_conversion(mat_path, save_path):
    """
    Conversion of the outcome of Full-Resolution framework algorithms from *.mat to GeoTIFF.

    Parameters
    ----------
    mat_path : str
        Path to the .mat file containing hyperspectral/multispectral data (variable 'data').
    save_path : str
        Path to save the output GeoTIFF.
    """

    # Load data from .mat file
    ms = io.loadmat(mat_path)['data'].astype(np.float32)  # shape: (rows, cols, bands)
    rows, cols, bands = ms.shape

    # Define transform (dummy if no georeference available)
    # Update this if you have actual GeoTransform values
    # transform = from_origin(0, 0, 1, 1)  

    # Metadata profile
    profile = {
        'driver': 'GTiff',
        'dtype': 'float32',
        'count': bands,
        'height': rows,
        'width': cols,
        'crs': None,       # update with "EPSG:4326" or another CRS if known
        'transform': None
    }

    # Write using Rasterio
    with rasterio.open(save_path, 'w', **profile) as dst:
        for i in range(bands):
            dst.write(ms[:, :, i], i + 1)
            
if __name__ == "__main__":
    mat_to_tiff_conversion(r'C:/Users/gaurh/Documents/GitHub/GeoSpatial-Machine-Learning-Codes/Urban_HSI_Dataset/Urban_F210.mat', r'C:/Users/gaurh/Documents/GitHub/GeoSpatial-Machine-Learning-Codes/Urban_HSI_Dataset')
