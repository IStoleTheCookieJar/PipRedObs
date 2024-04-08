import numpy as np
from astropy.io import fits
from scipy.ndimage import rotate
import glob
import sys

if(len(sys.argv)<2):
    sys.exit("Not enough arguements, try 'py conglomerate.py ~datadirectory~'")

#Mac users should just be able to copy absolute path
#Windows should change absolute paths to directories from C:\User\...\ to /Users/.../
#In Kalvyn's case: /Users/Kalvyn/Desktop/Obs2/APO_Data/

#####File finding############
pathname = sys.argv[1]
usefiles = glob.glob(pathname+"*galspec*b.fits")
if(len(usefiles) == 0):
    sys.exit("No galspec files found in chosen directory")
stdfiles = glob.glob(pathname+"std*b.fits")
if(len(stdfiles) == 0):
    sys.exit("No std files found in chosen direcotry")

#######Conglomerating every 3 usefile##########
for i in range(0,len(usefiles),3):
    if(usefiles[i][-6:] == "b.fits"):
        second_bool = False
        third_bool = False
        second_data=0
        third_data=0
        first = fits.open(usefiles[i])
        first_data = first[0].data
        if(i+1 < len(usefiles)):
            second = fits.open(usefiles[i+1])
            second_data = second[0].data
            second_bool = True
        if(i+2 < len(usefiles)):
            third = fits.open(usefiles[i+2])
            third_data = third[0].data
            third_bool = True

        final = 0
        if(third_bool == True):
            final = np.array([first_data,second_data,third_data])
            final = np.median(final,axis=0)
        elif(second_bool == True):
            final = np.array([first_data,second_data])
            final = np.median(final,axis=0)
        else:
            final = first_data
        temp = fits.HDUList([fits.PrimaryHDU(final)])
        temp.writeto((usefiles[i].replace(".fits", ".C.fits")), overwrite=True)

        print("Saved {0}".format(usefiles[i].replace(".fits", ".C.fits")))


#######Conglomerating std files##########
std_1 = fits.open(stdfiles[0])
std_2 = fits.open(stdfiles[1])
std_array = np.array([std_1[0].data,std_2[0].data])
std_final = np.median(std_array,axis=0)
std_temp = fits.HDUList([fits.PrimaryHDU(std_final)])
std_temp.writeto((pathname+"std_hz44.0001b.C.fits"),overwrite=True)
print("Saved {0}".format("std_hz44.0001b.C.fits"))
