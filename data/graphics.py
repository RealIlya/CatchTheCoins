import pygame as pg
import os

PATH = os.path.dirname(os.path.dirname(__file__))

GFX = os.path.join(PATH, 'resources', 'sprites')
SFX = os.path.join(PATH, 'resources', 'sounds')

BG = pg.image.load(os.path.join(GFX, 'backgroundForest.png'))

LEVEL1_BARRIER_BLOCK = pg.image.load(os.path.join(GFX, 'level_1_barrier_block.png'))
LEVEL1_DOWN_BLOCK = pg.image.load(os.path.join(GFX, 'level_1_down_block.png'))

PLAYER1_STAND = pg.image.load(os.path.join(GFX, 'soldier_stand.png'))

PLAYER1_WALK_RIGHT = [pg.image.load(os.path.join(GFX, 'soldier_walk1.png')),
                     pg.image.load(os.path.join(GFX, 'soldier_walk2.png'))]
