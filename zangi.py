#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import os
import pigpio
import syslog
import shutter as sh
import zangi_gui as gui

# global
SleepStepSec = 0.1

preview_numb = 0

loop = True

shutter_button = 6
preview_button = 26

# gpio
pi = pigpio.pi()
pi.set_mode(shutter_button, pigpio.INPUT)
pi.set_mode(preview_button, pigpio.INPUT)
pi.set_pull_up_down(shutter_button, pigpio.PUD_UP)
pi.set_pull_up_down(preview_button, pigpio.PUD_UP)

def go_home():
    global preview_numb
    preview_numb = sh.shutter_numb
    gui.screen_home()

def cb_shutter(gpio, level, tick):
    # print (gpio, level, tick)
    if KeepWatchForSeconds(5, gpio):
        CallShutdown()

    else:
        if gui.hmi_state == gui.PRVIEW_STATE:
            go_home()
        else:
            gui.screen_shutter()
            sh.cameraLoad()
            sh.shutter()
            # sh.shutter_small()
            sh.cameraSave()
            go_home()

def cb_preview(gpio, level, tick):
    # print (gpio, level, tick)
    preview()

def KeepWatchForSeconds(seconds, pin_numb):
    GoFlag = True
    while seconds > 0:
        time.sleep(SleepStepSec)
        seconds -= SleepStepSec
        if (pi.read(pin_numb) == True):
            GoFlag = False
            break
    return GoFlag

def CallShutdown():
    print("Going shutdown by GPIO.")
    syslog.syslog(syslog.LOG_NOTICE, "Going shutdown by GPIO.")
    os.system("/sbin/shutdown -h now 'Poweroff by GPIO'")

def preview():
    print ("preview")
    if preview_numb == 0:
        gui.screen_nophoto()
    else:
        global preview_numb
        filename = os.path.join(sh.photo_dir, str("{0:06d}".format(preview_numb)) + '.jpg')
        gui.screen_preview(filename)

        preview_numb -= 1
        if preview_numb < 1:
            preview_numb = sh.shutter_numb

cb1 = pi.callback(shutter_button, pigpio.FALLING_EDGE, cb_shutter)
cb2 = pi.callback(preview_button, pigpio.FALLING_EDGE, cb_preview)

if __name__ == '__main__':
    sh.photodirCheck()

    if not pi.connected:
        exit()

    sh.cameraLoad()
    preview_numb = sh.shutter_numb

    gui.screen_opening()

    gui.screen_home()

    while loop == True:
        pass
