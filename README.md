useful git commands

#This will check to see if there are updated files in the github(I believe)  
git fetch origin  
git diff --name-only origin

#This will edit and add those new changes to your current directory  
git pull

#This will add the changes you've made to the said filename to the commit you will send to github  
git add ---filename---

#This will commit those changes with a specific name of the version  
git commit -m "NAME OF COMMIT"

#This will push your changes to github so everyone can access them  
git push
