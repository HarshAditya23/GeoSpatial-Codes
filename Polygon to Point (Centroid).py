# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 12:36:26 2023

@author:  gaurh
"""

#Library Import
import geopandas as gpd

# GeoDataFrame creation
polygon = gpd.read_file(r"C:\Users\gaurh\Desktop\NEW\Field3_D1.shp")

# Change the geometry
points = polygon.copy()
points.geometry = points['geometry'].centroid

# Set Shapefile CRS
points.crs = polygon.crs

#Save the Shapefile
points.to_file(r'C:\Users\gaurh\Desktop\point_centroid_3.shp')
