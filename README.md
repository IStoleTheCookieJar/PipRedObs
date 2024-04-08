useful git commands

#This will check to see if there are updated files in the github(I believe)  
git fetch origin  
git diff --name-only origin

#This will edit and add those new changes to your current directory  
git pull

#This will show what files need to be added to the git commit and which files are not monitored by git  
git status

#This will add the changes you've made to the said filename to the commit you will send to github  
git add ---filename---

#This will commit those changes with a specific name of the version  
git commit -m "NAME OF COMMIT"

#This will push your changes to github so everyone can access them  
git push  

############Running Code##############  
Current order of files:  
conglomerate.py  
bias.py  
dark.py  
flat.py  
rotate.py  


conglomerate.py should be run first with the absolute path to the folder containing all the data (or at least bias, flat, and galspec) (in unix style).  
Will create new files of stds and galspecs with "C" at the end to these are the conglomerated files.  
bias.py will create .B.fits files with the bias subtracted and a FullBias.fits file that is the averaged bias photo  
dark.py will subtract the dark regions from all of the files, this area is preselected, but can be overwritten (py dark.py *directory* region_start_x region_start_y region_end_x region_end_y), will end in .D.fits  
flat.py will renormalize photos based on the flat field photos, will create .F.fits files  
rotate.py will rotate and crop the files so that it only shows the spectrum region, .R.files