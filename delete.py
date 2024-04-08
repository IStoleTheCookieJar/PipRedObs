import numpy as np
from astropy.io import fits
from scipy.ndimage import rotate
import glob
import sys
import os

##This .py is defined to delete all edited and reduced fits files to make starting over easier

if(len(sys.argv)<2):
    sys.exit("Not enough arguements, try 'py delete.py ~datadirectory~'")

#####File finding############
pathname = sys.argv[1]
fitsfiles = glob.glob(pathname+"*.fits*")
if(len(fitsfiles) == 0):
    sys.exit("No fits files found in chosen directory")

#######Deleting all fits files that aren't b.fits##########
for i in range(len(fitsfiles)):
    if(fitsfiles[i][-6:] != "b.fits" and fitsfiles[i][-6:] != "t.fits"):
        # t.fits is to avoid deleting the std_raw_extract.fits, please don't put .t.fits as an ending
        os.remove(fitsfiles[i])
        print("Removed: ",fitsfiles[i])

print("Done!")