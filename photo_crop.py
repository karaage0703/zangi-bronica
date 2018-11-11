# -*- coding: utf-8 -*-
from PIL import Image
import sys

left = 430
upper = 160
right = 2100
lower = 1300

def crop_rot (img):
    img = img.crop((left,upper,right,lower))
    img = img.rotate(180)
    return img

if __name__ == '__main__':
    param = sys.argv
    if (len(param) != 2):
        print ('Usage: $ python ' + param[0] + ' sample.jpg')
        quit()

    img = Image.open(param[1])
    output_img = crop_rot(img)
    output_img.save('out_' + param[1], quality=95)