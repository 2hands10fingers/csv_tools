'''
For some reason I couldn't find anywhere online for a script that did exactly this.
The script creates new folders and moves all image files of to their corresponding folder by image size.
You're welcome, world.
'''

from os import mkdir, listdir, path
from PIL import Image as image
from shutil import move as mover

currentpath = '.'

def imagesize(x):
    width = str(image.open(x).width)
    height = str(image.open(x).height)
    return "{}x{}".format(width, height)

for i in listdir(currentpath):
    try:
        imgsize = imagesize(i)
        if not path.exists(imgsize):
            mkdir(imgsize)
        else:
            mover(i, imgsize)
            print "{} -> {}".format(i, imgsize)
    except IOError:
        pass

