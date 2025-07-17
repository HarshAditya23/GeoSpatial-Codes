# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 19:38:36 2025

@author: gaurh
"""

import numpy as np
import rasterio

def convert_micasense_to_uint8(input_raster_path, output_raster_path, no_data_value=-10000.0):
    """
    Converts a 5-band MicaSense RedEdge-MX Float32 raster to uint8.
    
    Args:
        input_raster_path (str): Path to the input Float32 raster.
        output_raster_path (str): Path to save the output uint8 raster.
        no_data_value (float): Value representing NoData in the input raster (default is -999.0).
    """
    # Open the input raster
    with rasterio.open(input_raster_path) as src:
        # Read all bands as a 3D numpy array (bands, rows, cols)
        data = src.read()
        
        # Get the metadata (such as nodata value, crs, etc.)
        profile = src.profile

        # Get the NoData value if it's not provided
        if no_data_value is None:
            no_data_value = src.nodata

        # Prepare a mask for NoData values (across all bands)
        if no_data_value is not None:
            mask = data == no_data_value
            data = np.ma.masked_equal(data, no_data_value)  # Mask NoData values

        # Create an empty array for the normalized uint8 data
        normalized_data = np.zeros_like(data, dtype=np.uint8)

        # Process each band individually
        for band_idx in range(data.shape[0]):
            band = data[band_idx]

            # Find min and max values in this band (ignoring NoData values)
            min_val = np.min(band)
            max_val = np.max(band)

            if max_val != min_val:
                # Normalize the data to fit in the uint8 range (0-255)
                normalized_band = ((band - min_val) / (max_val - min_val) * 255).astype(np.uint8)
            else:
                # If all values in the band are the same, set to 255 (or another value)
                normalized_band = np.full_like(band, 255, dtype=np.uint8)  # Uniform value band

            # Re-apply the NoData mask (map to 0 or another value in the uint8 range)
            if no_data_value is not None:
                normalized_band[mask[band_idx]] = 0  # Map NoData to 0

            # Store the processed band in the output array
            normalized_data[band_idx] = normalized_band

        # Update the metadata for the output raster
        profile.update(dtype=rasterio.uint8, count=normalized_data.shape[0], nodata=0)

        # Write the normalized multi-band output raster
        with rasterio.open(output_raster_path, 'w', **profile) as dest:
            dest.write(normalized_data)

    print(f"Raster converted and saved to {output_raster_path}")

input_tiff = ""
output_tiff = ""
convert_micasense_to_uint8(input_tiff, output_tiff)