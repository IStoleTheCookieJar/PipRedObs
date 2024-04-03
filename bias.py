import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from astropy.io import fits
import astropy.units as u
import pandas as pd
import glob
import sys
import os

if(len(sys.argv)<2):
    sys.exit("Not enough arguements, try 'py bias.py ~datadirectory~'")

#Mac users should just be able to copy absolute path
#Windows should change absolute paths to directories from C:\User\...\ to /Users/.../
#In Kalvyn's case: /Users/Kalvyn/Desktop/Obs2/APO_Data/

pathname = sys.argv[1]
biasfiles = glob.glob(pathname +"bias*")
if(len(biasfiles) == 0):
    sys.exit("No bias files found in chosen directory")
usefiles = glob.glob(pathname+"*galspec*")
if(len(usefiles) == 0):
    sys.exit("No galspec files found in chosen directory")

bias0 = fits.open(biasfiles[0])
size = np.shape(bias0[0].data)
# print(size)
bias_image_array = np.zeros((len(biasfiles),size[0],size[1]))

for i in range(len(biasfiles)):
  bias = fits.open(biasfiles[i])
  bias_image = bias[0].data
  bias_image_array[i] = bias_image

bias_image_array = np.mean(bias_image_array,axis=0)
###Creating Fits file
hdu = fits.PrimaryHDU(bias_image_array)
hdu.writeto("FullBias.fits")