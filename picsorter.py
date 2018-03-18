'''
For some reason I couldn't find anywhere online for a script that did exactly this.
The script creates new folders and moves all image files of to their corresponding folder by image size.
You're welcome, world.
'''

from os import mkdir, listdir, path
from PIL import Image as image
from shutil import move as mover
from math import ceil

current_directory = listdir('.')
files = []
folders = []

def nameshorten(image):
    name_length = len(image)
    namediv_even = name_length / 2
    namediv_odd = int(ceil(name_length / 2))
    even_name_first_half = image[:namediv_even - namediv_even / 2 ]
    even_name_second_half = image[- int(ceil(namediv_even / 2)):]
    odd_name_first_half = image[:namediv_odd - namediv_odd / 2 ]
    odd_name_second_half = image[- int(ceil(namediv_odd / 2)):]

    if name_length % 2 == 0 and name_length > 50: #even
        return f"{even_name_first_half} ... {even_name_second_half}"
    elif name_length % 2 != 0 and name_length > 50: #odd
        return f"{odd_name_first_half} ... {odd_name_second_half}"
    else:
        return image

def imagesize(x):
    width = str(image.open(x).width)
    height = str(image.open(x).height)
    
    return f"{width}x{height}"

for i in current_directory:
    
    try:
        fileformat = image.open(i).format
        imgsize = imagesize(i)
        
        if not path.exists(imgsize):
            mkdir(imgsize)
            folders.append('.')
        
        else:
            
            print(f"Image: {nameshorten(i)} -> Folder: '{imgsize}'")
    
    except IOError:
        continue

for i in current_directory:
    
    try:
        imgsize = imagesize(i)
        fileformat = image.open(i).format
        
        if fileformat in ('JPEG', 'BMP', 'GIF', 'PNG'):
            mover(i, imgsize)
            files.append('*')
    
    except IOError:
        continue

print("-"*60)
print("  \n Sorting complete!\n")
print(f"- Files sorted: {len(current_directory)}")
print(f"- Images moved: {len(files)}")
print(f"- Folders created: {len(folders)}")
