# -*- coding: utf-8 -*-
import subprocess
import picamera
import os
from time import sleep

shutter_numb = 0
photo_dir = os.path.expanduser('/home/pi/photo_data')
preview_time = 2

camera = picamera.PiCamera()
camera.resolution = (2592,1944)

shutter_state = 0

def photodirCheck():
    if os.path.isdir(photo_dir):
        print("photo directory is already existed")
    else:
        print("make photo directory")
        os.mkdir(photo_dir)

def cameraLoad():
    global shutter_numb
    filename = os.path.join(photo_dir, 'camera.set')
    try:
        fp = open(filename)
        tmp_shutter_numb = fp.readlines()
        tmp2_shutter_numb = tmp_shutter_numb[0].rstrip()
        shutter_numb = int(tmp2_shutter_numb)
        fp.close()
    except IOError:
        print('no camera.set data, make set files')

def cameraSave():
    filename = os.path.join(photo_dir, 'camera.set')
    fp = open(filename, 'w')
    fp.write(str(shutter_numb))
    fp.close()

def shutter():
    global shutter_numb
    shutter_numb +=1

    filename = os.path.join(photo_dir, str("{0:06d}".format(shutter_numb)) + '.jpg')
    photofile = open(filename, 'wb')
    print(photofile)

    camera.capture(photofile)
    photofile.close()
    # camera.stop_preview()

if __name__ == '__main__':
    cameraLoad()
    shutter()
    cameraSave()
