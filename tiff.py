#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reading TIFF in python
"""

import os
import numpy as np
import matplotlib.pyplot as plt
plt.ion()


os.chdir('/path/to/file')
fname = 'my_file_name.tiff'


#Size and data type
nx = 400
ny = 400
dt = np.float32

#Read
with open(fname) as f:
    f.seek(8)
    image = np.fromfile(f, dtype = dt, count = nx*ny).reshape((nx,ny))

#Plot 
    
plt.figure()
plt.imshow(image, interpolation = 'nearest', origin = 'lower')