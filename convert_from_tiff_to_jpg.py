import os
from PIL import Image 

# get all files within current directory
files = os.listdir(".")
for filename in files:

    portion = os.path.splitext(filename)
    
    if portion[1] == ".tif":
        newname = portion[0] + ".jpg"
        img = Image.open(filename) 
        img.save(newname)

    
