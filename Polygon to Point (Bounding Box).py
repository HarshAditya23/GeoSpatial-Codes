# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 13:17:16 2023

@author: gaurh
"""

import geopandas as gpd
from shapely.geometry import Point

# Read the polygon shapefile
polygon_gdf = gpd.read_file(r'C:\Users\gaurh\Desktop\Rabi_2021-2022_rectified (1)\reproj_Rabi_2021-2022.shp')

# Create an empty list to store point geometries
point_geometries = []

# Iterate through polygons, splitting their exterior coordinates into points
for index, row in polygon_gdf.iterrows():
    polygon = row['geometry']
    exterior_coords = polygon.exterior.coords
    for coord in exterior_coords:
        point_geometries.append(Point(coord))

# Create a GeoDataFrame from the point geometries
point_gdf = gpd.GeoDataFrame(geometry=point_geometries, columns=['geometry'])

# Copy Polygon Shapefile CRS to Point Shapefile
point_gdf.crs = polygon_gdf.crs

# Write the new GeoDataFrame to a point shapefile
point_gdf.to_file('output_point_2.shp', driver='ESRI Shapefile')

print("Point shapefile created successfully.")

