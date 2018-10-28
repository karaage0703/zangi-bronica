# -*- coding: utf-8 -*-
import subprocess
import picamera
import os
from time import sleep

shutter_numb = 0
photo_dir = os.path.expanduser('/home/pi/photo_data')
preview_time = 2

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

    with picamera.PiCamera() as camera:
        camera.resolution = (2592,1944)
        # camera.brightness = 50
        # camera.flash_mode = 'on'
        # camera.exposure_compensation = 0
        camera.start_preview()
        sleep(preview_time)
        camera.capture(photofile)

    photofile.close()

def shutter_small():
    global shutter_numb
    shutter_numb +=1

    filename = os.path.join(photo_dir, str("{0:06d}".format(shutter_numb)) + '.jpg')
    photofile = open(filename, 'wb')
    print(photofile)

    with picamera.PiCamera() as camera:
        camera.resolution = (320,240)
        # camera.resolution = (259,194)
        camera.start_preview()
        sleep(3.000)
        camera.capture(photofile)

    photofile.close()


if __name__ == '__main__':
    cameraLoad()
    shutter()
    cameraSave()
