import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from astropy.io import fits
import astropy.units as u
import pandas as pd
import glob
import os
#i have no clue how much of this needs to be imported here, i've never made a pipeline before 

pathname = ""
biasfiles = glob.glob(pathname +"bias*")
usefiles = glob.glob(pathname+"*galspec*")

bias_image_array = np.zeros(len(biasfiles))
for i in range(len(biasfiles)):
  bias = fits.open(biasfiles[i])
  bias_image = bias[0].data
  bias_image_array[i] = bias_image
