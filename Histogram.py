# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 15:33:54 2024

@author: gaurh
"""

import rasterio
import numpy as np
import matplotlib.pyplot as plt

tiff_file = '220725_ortho_NDRE.tif'
with rasterio.open(tiff_file) as dataset:
    ndvi_band = dataset.read(1)

no_data_value = dataset.nodata
ndvi_band = np.ma.masked_equal(ndvi_band, no_data_value)

plt.figure(figsize=(10, 6))
plt.hist(ndvi_band.compressed(), bins=50, color='salmon', edgecolor='black')
plt.title('Survey 3 Distribution of NDRE Values')
plt.xlabel('NDRE Index Value')
plt.ylabel('Frequency')
plt.grid(True, linewidth=0.2)
plt.show()
