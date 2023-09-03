# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 12:36:26 2023

@author:  gaurh
"""

#Library Import
import geopandas as gpd

# GeoDataFrame creation
polygon = gpd.read_file(r"C:\Users\gaurh\Desktop\Rabi_2021-2022_rectified (1)\reproj_Rabi_2021-2022.shp")

# Change the geometry
points = polygon.copy()
points.geometry = points['geometry'].centroid

# Set Shapefile CRS
points.crs = polygon.crs

#Save the Shapefile
points.to_file('point_centroid.shp')
