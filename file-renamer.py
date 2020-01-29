#!/usr/bin/python3
from os import mkdir, listdir, rename
from shutil import copytree
import argparse

parser = argparse.ArgumentParser(description='Rename all images and append a number to the end')
parser.add_argument('-of','--oldfolder', type=str, help='selects the desired old folder path')
parser.add_argument('-nf','--newfolder', type=str, help='creates the new folder path')
parser.add_argument('-n','--newname', type=str, help='creates the name of the file')
parser.add_argument('-x','--extens', type=str, help='creates the name of the extension')
args = parser.parse_args()

if __name__ == '__main__':

    imgarray = []
    newpath = args.oldfolder + args.newfolder + '/'

    copytree(args.oldfolder, newpath)

    for i in listdir(newpath):
        imgarray.append(newpath + i)

    for x in imgarray:
        change = f"{newpath}{args.newname}-{str(imgarray.index(x))}.{args.extens}"

        if x == newpath + '.DS_Store':
            pass
        else:
            rename(x, change)
            print(f"--------- \n{x}\n ---------- was renamed and sent to: \n change")
