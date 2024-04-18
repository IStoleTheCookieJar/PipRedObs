import numpy as np
from astropy.io import fits
import glob
import sys

x_lower=0
x_upper=2048
y_lower=0
y_upper=145

if(len(sys.argv)<2):
    sys.exit("Not enough arguements, try 'py dark.py ~datadirectory~'")
if(len(sys.argv) == 5):
    x_lower = sys.argv[2]
    x_upper = sys.argv[3]
    y_lower = sys.argv[4]
    y_upper = sys.argv[5]
elif(len(sys.argv) != 2):
    sys.exit("Incorrect nmber of arguements, either just enter directory, or directory proceeded by 4 numbers, (x_lower,x_upper,y_lower,y_upper)")
    

#####File finding############
pathname = sys.argv[1]
usefiles = glob.glob(pathname+"*galspec*.B.fits")
if(len(usefiles) == 0):
    sys.exit("No galspec files found in chosen directory")
flatfiles = glob.glob(pathname+"flat*.B.fits")
if(len(flatfiles) == 0):
    sys.exit("No flat files found in chosen direcotry")
stdfiles = glob.glob(pathname+"std*.B.fits")
if(len(stdfiles) == 0):
    sys.exit("No std files found in chosen directory")

#######Subtracting darks from all use files and creating new ones##########
for i in range(len(usefiles)):
    if(usefiles[i][-7:] == ".B.fits"):
        print(usefiles[i])
        current = fits.open(usefiles[i])
        current_image = current[0].data
        dark = current_image[x_lower:x_upper,y_lower:y_upper]
        dark = np.median(dark)
        current_image = current_image-dark
        temp = fits.HDUList([fits.PrimaryHDU(current_image)])
        temp.writeto(usefiles[i][:-5]+".D.fits", overwrite=True)

########Subtracting from all flat files and creating new ones#########
for i in range(len(flatfiles)):
    if(flatfiles[i][-7:] == ".B.fits"):
        print(flatfiles[i])
        current = fits.open(flatfiles[i])
        current_image = current[0].data
        dark = current_image[x_lower:x_upper,y_lower:y_upper]
        dark = np.median(dark)
        current_image = current_image-dark
        temp = fits.HDUList([fits.PrimaryHDU(current_image)])
        temp.writeto(flatfiles[i][:-5]+".D.fits", overwrite=True)

########Subtracting from all std files and creating new ones#########
for i in range(len(stdfiles)):
    if(stdfiles[i][-7:] == ".B.fits"):
        print(stdfiles[i])
        current = fits.open(stdfiles[i])
        current_image = current[0].data
        dark = current_image[x_lower:x_upper,y_lower:y_upper]
        dark = np.median(dark)
        current_image = current_image-dark
        temp = fits.HDUList([fits.PrimaryHDU(current_image)])
        temp.writeto(stdfiles[i][:-5]+".D.fits", overwrite=True)
