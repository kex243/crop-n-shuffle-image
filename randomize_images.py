import random
from os import listdir
from os.path import isfile, join
from shutil import copyfile
croppedpath="./cropped/"
files = [f for f in listdir(croppedpath) if isfile(join(croppedpath, f))]
shufflelist = files.copy()
random.shuffle(shufflelist)
print(files)
print(shufflelist)
croppedpath="./cropped/"
shuffledpath="./shuffled/"

for i in range(0,len(files)):
    src = croppedpath + files[i]
    print (src)
    dst = shuffledpath + shufflelist[i]
    print (dst)
    copyfile(src, dst)