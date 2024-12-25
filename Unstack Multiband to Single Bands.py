# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 16:16:30 2023

@author: HarshAditya23
"""

import os
import rasterio

src = rasterio.open(r'C:\Users\gaurh\Desktop\rgb.tif')
for band in range(1, src.count + 1):
    single_band = src.read(band)

    # get the output name
    out_name = os.path.basename(r'C:\Users\gaurh\Desktop\liss3')
    file, ext = os.path.splitext(out_name)
    name = file + "_" + "B" + str(band) + ".tif"
    out_img = os.path.join(r'C:\Users\gaurh\Desktop\input', name)
    print(out_img + " done")

    # Copy the metadata
    out_meta = src.meta.copy()
    out_meta.update({"count": 1})

    # save the clipped raster to disk
    with rasterio.open(out_img, "w", **out_meta) as dest:
        dest.write(single_band, 1)
