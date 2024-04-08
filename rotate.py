import numpy as np
from astropy.io import fits
from scipy.ndimage import rotate
import glob
import sys

if(len(sys.argv)<2):
    sys.exit("Not enough arguements, try 'py bias.py ~datadirectory~'")


#####File finding############
pathname = sys.argv[1]
usefiles = glob.glob(pathname+"*galspec*")
if(len(usefiles) == 0):
    sys.exit("No galspec files found in chosen directory")
stdfiles = glob.glob(pathname+"std*")
if(len(stdfiles) == 0):
    sys.exit("No std files found in chosen direcotry")

# print(size)
rotate_val = -0.63  # Degres
xcrop = (600, 1650)
ycrop = (175, 850)

#######Rotating all use files and creating new ones##########
for i in range(len(usefiles)):
    if(usefiles[i][-6:] == "F.fits"):
        current = fits.open(usefiles[i])

        current[0].data = rotate(current[0].data, rotate_val, reshape=False)

        current[0].data = current[0].data[ycrop[0]:ycrop[1], xcrop[0]:xcrop[1]]

        current.writeto(usefiles[i].replace(".fits", ".R.fits"), overwrite=True)
        print("Saved {0}".format(usefiles[i].replace(".fits", ".R.fits")))


#######Rotating all std files and creating new ones##########
# for i in range(len(stdfiles)):
#     if(usefiles[i][-6:] == "F.fits"):
#         current = fits.open(usefiles[i])
#         current[0].data = rotate(current[0].data, rotate_val, reshape=False)
#         current[0].data = current[0].data[ycrop[0]:ycrop[1], xcrop[0]:xcrop[1]]
#         current.writeto(usefiles[i].replace(".fits", ".R.fits"), overwrite=True)
#         print("Saved {0}".format(usefiles[i].replace(".fits", ".R.fits")))
