# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 17:49:44 2021
This python script splits all the images in a directory based on defined pixel width=height
Unlike other splitters, this script ignores partial tiles at the edges. Hence, you get perfectly usable 
split images in a new directory!
@author: pyada
"""
import os
import sys
import glob
from PIL import Image
from itertools import product

d=416 #Define pixel width=height that will used for splitting the image      
dir_in="C:/Users/pyada/.spyder-py3/120ft" #Here you define your directory path where all the images are located
dir_out="C:/Users/pyada/.spyder-py3/120ftnew001_split" #Here you define location of directory where you will save the output
filelist = [f for f in glob.glob(dir_in + "**/*.jpg", recursive=True)]


def image_splitter(filename, dir_in, dir_out, d):
    name, ext = os.path.splitext(filename)
    img = Image.open(os.path.join(dir_in, fp))
    w, h = img.size
    
    grid = list(product(range(0, h-h%d, d), range(0, w-w%d, d)))
    for i, j in grid:
        box = (j, i, j+d, i+d)
        crop=img.crop(box)
        savedir="C:/Users/pyada/.spyder-py3/120ftnew001_split" #Same as dir_out
        name = os.path.basename(fp)
        name = os.path.splitext(name)[0]
        save_to= os.path.join(savedir, name+"_{:03}.tif")
        crop.save(save_to.format(image_num))
        

image_num=1        
for fp in filelist:
    image_splitter(fp,dir_in,dir_out,d)
    image_num += 1
    
print("Splitting completed!")
    