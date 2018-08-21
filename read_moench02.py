#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sample script to read Moench02 data from a raw file

@author: Erik Frojdh
"""
import numpy as np
import matplotlib.pyplot as plt
plt.ion()

n_rows = 160
n_cols = 160    
sc_width = 40       #Width of the super column
n_samples = 6410    #Number of samples 160*160/4 + 10 
n_sc = 4            #Number of supercolumns
#slices to access the super column
supercolumns = [np.s_[:, i*sc_width:(i+1)*sc_width] for i in range(n_sc)] 
data_slice = slice(0,n_samples-10, None)
#index if the adc used to read out pixel data in the corresponding super column
adc_index = [10,8,23,20]


def read_frame(file_handle, block_size = 32):
    """
    Read one frame, works with a file handle or a file name
    block_size = 32 - analog data only
    block_size = 36 - analog and digital data
    """
    block = np.fromfile(file_handle, count = n_samples*block_size, 
                        dtype = np.uint16).reshape(n_samples, block_size)
    image = np.zeros((n_rows, n_cols))
    for iadc, sc in zip(adc_index, supercolumns):
        image[sc] = block[data_slice, iadc].reshape(n_rows, sc_width)

    return image
    

fname = '/path/to/file.raw'

#Read the first frame using file name
image = read_frame(fname)
fig, ax = plt.subplots(1,1)
im = ax.imshow(image, origin = 'lower', interpolation = 'nearest')
ax.grid(False)


