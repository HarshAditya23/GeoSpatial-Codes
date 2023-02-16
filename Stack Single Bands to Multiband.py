# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 16:16:30 2023

@author: HarshAditya23
"""

import glob
import rasterio
from natsort import natsorted 

file_list = natsorted((glob.glob(r'C:\Users\mrg21-021411956\Desktop\input\*.tif')))
#print(file_list)

# Read metadata of first file
with rasterio.open(file_list[0]) as src0:
    meta = src0.meta

# Update meta to reflect the number of layers
meta.update(count = len(file_list))

# Read each layer and write it to stack
with rasterio.open('stack.tif', 'w', **meta) as dst:
    for id, layer in enumerate(file_list, start=1):
        with rasterio.open(layer) as src1:
            dst.write_band(id, src1.read(1))
            