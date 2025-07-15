# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 16:05:00 2023

@author: gaurh
"""

# Load packages to enable numpy file creation and visualization
import rasterio
from rasterio.plot import show
from matplotlib import pyplot as plt
import os
import numpy as np
import glob
from numpy import savez_compressed

# Specify folder path for data
path = '/*.tif'
out = '' # specify output folder

# Create a loop that opens GeoTiff and saves as numpy zipped files
for index, filename in enumerate(glob.glob(path)):
    # Get input Raster properties
    a = rasterio.open(filename)
    arr = a.read()
    arr.shape
    basename = os.path.splitext(os.path.basename(filename))[0]
    #Specify path to output folder to save numpy zipped files
    os.chdir(out)
    # Save numpy files
    savez_compressed(f'{basename}.npz',arr)

# Preview npz shape
import os
import numpy as np
out = ''
os.chdir(out)
# Multiband dataset - feature
file = "file1.npz"
images = np.load(region1)[arr_0]
images.shape

# Label layer
_label = "_label.npz"
label = np.load(region1_label)["arr_0"]
label.shape
