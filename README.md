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

######################################  
bias.py should be run first with the absolute path to the folder containing all the data (or at least bias, flat, and galspec) (in unix style).  
Will create new files of flats and galspecs with "B" at the end to signify that bias has been subtracted.  
Creates FullBias.fits which is the averaged bias 2d array as a fits fill for later use if necessary.