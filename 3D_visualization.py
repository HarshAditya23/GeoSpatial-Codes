# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 16:16:30 2023

@author: HarshAditya23
"""

from osgeo import gdal
from tvtk.api import tvtk
from mayavi import mlab

data = gdal.Open('dsm.tif')
layer_1 = data.ReadAsArray()
layer_2 = tvtk.JPEGReader()
layer_2.file_name="terrain.jpg"

texture = tvtk.Texture(input_connection=layer_2.output_port, interpolate=0)

mlab.figure(size=(640, 800), bgcolor=(0.16, 0.28, 0.46))

surf = mlab.surf(layer_1, color=(1,1,1), warp_scale=0.2) 
surf.actor.enable_texture = True
surf.actor.tcoord_generator_mode = 'plane'
surf.actor.actor.texture = texture

mlab.show()