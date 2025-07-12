# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 17:08:57 2024

@author: gaurh
"""
import numpy as np
import matplotlib.pyplot as plt

# Load the .npy file
npy_file = ''
hyperspectral_data = np.load(npy_file)

# Print the dimensions of the loaded data
print(f"Loaded data dimensions: {hyperspectral_data.shape}")

# Transpose the hyperspectral data to switch rows and columns
hyperspectral_data = np.transpose(hyperspectral_data, (1, 0, 2))

# Print the new dimensions after transposing
print(f"Transposed data dimensions: {hyperspectral_data.shape}")

# Function to display a specific band
def display_band(data, band_index):
    plt.figure(figsize=(10, 8))
    plt.imshow(data[:, :, band_index], cmap='gray')
    plt.title(f'Band {band_index}')
    plt.colorbar()
    plt.show()

# Function to display a combination of three bands as an RGB image
def display_rgb(data, r_band, g_band, b_band):
    rgb_image = np.dstack((data[:, :, r_band], data[:, :, g_band], data[:, :, b_band]))
    plt.figure(figsize=(10, 8))
    plt.imshow(rgb_image / np.max(rgb_image))
    plt.title(f'RGB Composite (R: {r_band}, G: {g_band}, B: {b_band})')
    plt.show()

# Display specific bands
display_band(hyperspectral_data, 10)  # Display band 10
display_band(hyperspectral_data, 20)  # Display band 20

# Display an RGB composite using three selected bands
display_rgb(hyperspectral_data, 10, 20, 30)  # Display composite of bands 10, 20, 30


