import pygame as pg
import os

PATH = os.path.dirname(os.path.dirname(__file__))

GFX = os.path.join(PATH, 'resources', 'sprites')
SFX = os.path.join(PATH, 'resources', 'sounds')

LEVEL1_BARRIER_BLOCK = pg.image.load(os.path.join(GFX, 'level_1_barrier_block.png'))
LEVEL1_DOWN_BLOCK = pg.image.load(os.path.join(GFX, 'level_1_down_block.png'))
