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
biasfiles = glob.glob(pathname +"bias*")
if(len(biasfiles) == 0):
    sys.exit("No bias files found in chosen directory")
usefiles = glob.glob(pathname+"*galspec*")
if(len(usefiles) == 0):
    sys.exit("No galspec files found in chosen directory")
flatfiles = glob.glob(pathname+"flat*")
if(len(flatfiles) == 0):
    sys.exit("No flat files found in chosen direcotry")

####Opening vias files#######
bias0 = fits.open(biasfiles[0])
size = np.shape(bias0[0].data)
# print(size)
bias_image_array = np.zeros((len(biasfiles),size[0],size[1]))

#######Reading bias files and averaging###########
for i in range(len(biasfiles)):
    bias = fits.open(biasfiles[i])
    bias_image = bias[0].data
    bias_image = bias_image.astype(float)
    bias_image_array[i] = bias_image

bias_image_final = np.median(bias_image_array,axis=0)

#######Subtracting from all use files and creating new ones##########
for i in range(len(usefiles)):
    if(usefiles[i][-6:] == "b.fits"):
        print(usefiles[i])
        current = fits.open(usefiles[i])
        current_image = current[0].data
        reduced = current_image-bias_image_final
        temp = fits.HDUList([fits.PrimaryHDU(reduced)])
        temp.writeto(usefiles[i][:-5]+".B.fits", overwrite=True)

########Subtracting from all flat files and creating new ones#########
for i in range(len(flatfiles)):
    if(flatfiles[i][-6:] == "b.fits"):
        print(flatfiles[i])
        current = fits.open(flatfiles[i])
        current_image = current[0].data
        reduced = current_image-bias_image_final
        temp = fits.HDUList([fits.PrimaryHDU(reduced)])
        temp.writeto(flatfiles[i][:-5]+".B.fits", overwrite=True)

###Creating Fits file##############
hdu = fits.PrimaryHDU(bias_image_final)
hdu.writeto("FullBias.fits",overwrite=True)