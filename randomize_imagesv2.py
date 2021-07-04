import random
from os import listdir
from os.path import isfile, join
from shutil import copyfile
croppedpath="./cropped/"
files = [f for f in listdir(croppedpath) if isfile(join(croppedpath, f))]


orderliness = 0.9 #that parameter + random.gauss are responsible for randomness of image. More of 'orderliness'- less random. Read about Gauss- it gets position between two variables.
def tuplify(x, y):
    return (orderliness * y + random.gauss(0,1), x)

values = files
print(values)
pairs = list(map(tuplify, values, range(len(values))))
pairs.sort()
shufflelist = [p[1] for p in pairs]


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