#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import time
import os

hmi_state = 0
HOME_STATE = 0
PRVIEW_STATE = 1

# GUI Setting from here------
pygame.init()
pygame.mouse.set_visible(0)

size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
print ("Framebuffer size: %d x %d" % (size[0], size[1]))
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
title_font = pygame.font.Font(os.path.join('/usr/share/fonts/truetype/fonts-japanese-gothic.ttf'), 48)
body_font = pygame.font.Font(os.path.join('/usr/share/fonts/truetype/fonts-japanese-gothic.ttf'), 32)
fpsclock = pygame.time.Clock()
# ----------- GUI

def screen_clear():
    screen.fill((0,0,0))
    pygame.display.update()

def screen_opening():
    title = title_font.render('ZANGI BRONICA Booting...', True, (255,255,255))
    screen.fill((0,0,0))
    screen.blit(title, (30,100))
    pygame.display.update()
    time.sleep(3)
    screen_clear()

def screen_shutter():
    text = title_font.render('Taking Photo', True, (255,255,255))
    screen.fill((0,0,0))
    screen.blit(text, (50,100))
    pygame.display.update()

def screen_nophoto():
    text = title_font.render('No Photo',  True, (255,255,255))
    screen.fill((0,0,0))
    screen.blit(text, (50,100))
    pygame.display.update()

def screen_home():
    global hmi_state
    hmi_state = HOME_STATE

    screen.fill((0,0,0))
    home_text = title_font.render(u'ザンギ ブロニカ', True, (255,255,255))
    screen.blit(home_text,(100,30))
    pygame.display.update()

def screen_preview(filename):
    global hmi_state
    hmi_state = PRVIEW_STATE

    img = pygame.image.load(filename).convert()
    img = pygame.transform.scale(img, (pygame.display.Info().current_w, pygame.display.Info().current_h))
    screen.blit(img, (0,0))
    pygame.display.update()

if __name__ == '__main__':
    pass
