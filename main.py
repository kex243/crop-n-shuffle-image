import subprocess
from PIL import Image

im = Image.open('zcomix.jpg')
width, height = im.size
print(width,height)
input("Press Enter to continue...")
elementsLenght = 10 # puzzle block number
elementsWidth = 20

cropedwidht = width//elementsLenght*elementsLenght #px after cropping - widht
print(cropedwidht)
input("Press Enter to continue...")
cropheight = height//elementsWidth*elementsWidth #px after cropping - height
print(cropheight)
input("Press Enter to continue...")

partswidth = cropedwidht//elementsLenght #px widht of puzzle element
print(partswidth)
input("Press Enter to continue...")
partsheight = cropheight//elementsWidth #px height of puzzle element
print(partsheight)
input("Press Enter to continue...")

toeval =f'''magick zcomix.jpg -gravity center -crop {cropedwidht}x{cropheight}+0+0 +gravity +repage -crop {partswidth}x{partsheight} +repage ./cropped/comix_ctiles_%04d.png'''
subprocess.call(toeval, shell=True)
input("Press Enter to continue...")
exec(open("./randomize_imagesv2.py").read()) #randomize the image, there are first version called randomize_images.py, it shuffles images absolutely messy.
input("Press Enter to continue...")
toeval2 =f'''magick montage -mode concatenate -tile {elementsLenght}x  ./shuffled/comix_ctiles_*.png ./zfinal/comix_rejoined.jpg'''
subprocess.call(toeval2, shell=True)
input("finish...")