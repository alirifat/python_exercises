# pip install pillow

from PIL import Image
import glob, os

for infile in glob.glob('playing_cards/*.png'):
    file, ext = os.path.splitext(infile)
    filename = file.split('\\')[1]
    with Image.open(infile) as im:
        width, height = im.size
        new_size = (int(width / 5), int(height / 5))
        im1 = im.resize(new_size)
        im1.save('playing_cards/{0}_resized.png'.format(filename))