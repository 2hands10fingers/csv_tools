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
    return "{}x{}".format(str(width), str(height))

for i in listdir(currentpath):
    try:
        imgsize = imagesize(i)
        if not path.exists(imgsize):
            mkdir(imgsize)
        else:
            shutil.move(i, imgsize)
            print "{} -> {}".format(i, imgsize)
    except IOError:
        pass
