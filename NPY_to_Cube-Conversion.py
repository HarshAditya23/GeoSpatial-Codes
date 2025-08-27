# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 16:54:03 2024

@author: gaurh
"""
import numpy as np

def npy_to_bsq(npy_file, bsq_file):
    # Load the .npy file
    hyperspectral_data = np.load(npy_file)
    
    # Print the dimensions of the loaded data
    print(f"Loaded data dimensions: {hyperspectral_data.shape}")
    
    # Transpose the hyperspectral data to switch rows and columns
    hyperspectral_data = np.transpose(hyperspectral_data, (1, 0, 2))
    
    # Print the new dimensions after transposing
    print(f"Transposed data dimensions: {hyperspectral_data.shape}")

    # Ensure the data is in the format (rows, cols, bands)
    #if hyperspectral_data.ndim != 3:
    #    raise ValueError("Expected a 3D array (rows, cols, bands)")

    # Open a binary file for writing the BSQ data
    with open(bsq_file, 'wb') as f:
        for band in range(hyperspectral_data.shape[2]):
            # Write each band sequentially
            hyperspectral_data[:, :, band].astype(np.float32).tofile(f)

def write_bsq_header(bsq_file, hdr_file, rows, cols, bands):
    header = f"""ENVI
samples = {cols}
lines   = {rows}
bands   = {bands}
header offset = 0
file type = ENVI Standard
data type = 4
interleave = bsq
byte order = 0
"""
    with open(hdr_file, 'w') as f:
        f.write(header)

# Example usage
npy_file = 'urban_gt_reshaped.npy'
bsq_file = 'urban_gt2.bsq'
hdr_file = 'urban_gt2.hdr'

# Convert npy to bsq
npy_to_bsq(npy_file, bsq_file)

# Load the hyperspectral data to get its dimensions
hyperspectral_data = np.load(npy_file)
hyperspectral_data = np.transpose(hyperspectral_data, (1, 0, 2))
rows, cols, bands = hyperspectral_data.shape

# Write the BSQ header file
write_bsq_header(bsq_file, hdr_file, rows, cols, bands)
