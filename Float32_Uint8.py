# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 19:38:36 2025

@author: gaurh
"""

import rasterio
import numpy as np

def convert_to_8bit(input_path, output_path):
    with rasterio.open(input_path) as src:
        profile = src.profile.copy()
        profile.update(
            dtype=rasterio.uint8,
            count=src.count,
            compress='lzw'
        )

        with rasterio.open(output_path, 'w', **profile) as dst:
            for band in range(1, src.count + 1):
                data = src.read(band)
                min_val = np.nanmin(data)
                max_val = np.nanmax(data)

                # Prevent divide by zero
                if max_val - min_val == 0:
                    scaled = np.zeros(data.shape, dtype=np.uint8)
                else:
                    scaled = ((data - min_val) / (max_val - min_val) * 255).astype(np.uint8)

                dst.write(scaled, band)

    print(f"Converted: {input_path} → {output_path}")

# Example usage
if __name__ == "__main__":
    input_tiff = ""
    output_tiff = ""
    convert_to_8bit(input_tiff, output_tiff)