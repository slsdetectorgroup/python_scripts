#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reading a single image TIFF file where the data starts directly after the
header. Requires knowledge about the geometry and data type.
"""
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
plt.ion()

#If the script is called without arguments
if len(sys.argv) == 1:
    os.chdir('/path/to/file')
    fname = 'my_file_name.tiff'

#If we call the script with a file name    
elif len(sys.argv) == 2:
    fname = sys.argv[1]
    
#Size and data type
nx = 400
ny = 400
dt = np.float32

#Read
with open(fname) as f:
    f.seek(8) #skip header
    image = np.fromfile(f, dtype = dt, count = nx*ny).reshape((nx,ny), order = 'C')

#Plot 
plt.figure()
plt.imshow(image, interpolation = 'nearest', origin = 'lower')
plt.colorbar()

#set limits of the color scale between 0 and 
plt.clim(0,image.flat[np.argsort(image.flat)[-int(image.size/100)]])