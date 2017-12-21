'''
For some reason I couldn't find anywhere online for a script that did exactly this.
The script creates new folders and moves all image files of to their corresponding folder by image size.
You're welcome, world.
'''

from os import mkdir, listdir, path
from PIL import Image as image
import shutil

currentpath = '.'

def imagesize(x):
    width = image.open(x).width
    height = image.open(x).height
    return str(width) + 'x' + str(height)

for i in listdir(currentpath):
    imgsize = imagesize(i)
    if (i == 'picsorter.py') or i == '.DS_Store':
        pass
    else:
        print (imgsize)
        if not path.exists(imgsize):
            mkdir(imagesize(imgsize)

        shutil.move(i, imgsize)
