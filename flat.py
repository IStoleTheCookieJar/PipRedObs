#This code should work, but eventually gives us some big(ish) negative values in the calibrated one
#I think because of negative values from the bias calibration
#Should we zero out any negative values from the bias calibration?

import numpy as np
from astropy.io import fits
import glob
import sys

if(len(sys.argv)<2):
    sys.exit("Not enough arguements, try 'py bias.py ~datadirectory~'")

#Mac users should just be able to copy absolute path
#Windows should change absolute paths to directories from C:\User\...\ to /Users/.../
#In Kalvyn's case: /Users/Kalvyn/Desktop/Obs2/APO_Data/

#####File finding############
pathname = sys.argv[1]
usefiles = glob.glob(pathname+"*galspec*")
if(len(usefiles) == 0):
    sys.exit("No galspec files found in chosen directory")
flatfiles = glob.glob(pathname+"flat*.B*")
if(len(flatfiles) == 0):
    sys.exit("No flat files found in chosen direcotry")

####Opening flat files#######
flat0 = fits.open(flatfiles[0])
size = np.shape(flat0[0].data)
# print(size)
flat_image_array = np.zeros((len(flatfiles),size[0],size[1]))

#######Reading flat files and averaging###########
for i in range(len(flatfiles)):
    flat = fits.open(flatfiles[i])
    flat_image = flat[0].data
    flat_image = flat_image.astype(float)
    flat_image_array[i] = flat_image

flat_image_final = np.median(flat_image_array,axis=0)
Iff = flat_image_final/np.median(flat_image_final)
big = (Iff >= 0.01)
small = (Iff < 0.01)
Iff = Iff*big + small

#######Subtracting from all use files and creating new ones##########
for i in range(len(usefiles)):
    if(usefiles[i][-6:] == "B.fits"):
        print(usefiles[i])
        current = fits.open(usefiles[i])
        current_image = current[0].data
        reduced = current_image/Iff
        temp = fits.HDUList([fits.PrimaryHDU(reduced)])
        temp.writeto(usefiles[i][:-5]+".F.fits", overwrite=True)


###Creating Fits file##############
hdu = fits.PrimaryHDU(Iff)
hdu.writeto("FullFlat.fits",overwrite=True)
