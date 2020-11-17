import pygame as pg
import os

PATH = os.path.dirname(os.path.dirname(__file__))

GFX = os.path.join(PATH, 'resources', 'sprites')
SFX = os.path.join(PATH, 'resources', 'sounds')

BG = pg.image.load(os.path.join(GFX, 'backgroundForest.jpg'))

LEVEL1_BARRIER_BLOCK = pg.image.load(os.path.join(GFX, 'level_1_barrier_block.jpg'))
LEVEL1_DOWN_BLOCK = pg.image.load(os.path.join(GFX, 'level_1_down_block.jpg'))

CHAR1_STAND = pg.image.load(os.path.join(GFX, 'character1/character1_idle.png'))

CHAR1_DODGE_RIGHT = pg.image.load(os.path.join(GFX, 'character1/character1_dodge_right.png'))

CHAR1_DODGE_LEFT = pg.image.load(os.path.join(GFX, 'character1/character1_dodge_left.png'))

CHAR1_WALK_RIGHT = [
    pg.image.load(os.path.join(GFX, 'character1/walk_right/character1_walk_right1.png')),
    pg.image.load(os.path.join(GFX, 'character1/walk_right/character1_walk_right2.png')),
    pg.image.load(os.path.join(GFX, 'character1/walk_right/character1_walk_right3.png')),
    pg.image.load(os.path.join(GFX, 'character1/walk_right/character1_walk_right4.png')),
    pg.image.load(os.path.join(GFX, 'character1/walk_right/character1_walk_right5.png')),
    pg.image.load(os.path.join(GFX, 'character1/walk_right/character1_walk_right6.png')),
    pg.image.load(os.path.join(GFX, 'character1/walk_right/character1_walk_right7.png')),
    pg.image.load(os.path.join(GFX, 'character1/walk_right/character1_walk_right8.png')),
]

CHAR1_WALK_LEFT = [
    pg.image.load(os.path.join(GFX, 'character1/walk_left/character1_walk_left1.png')),
    pg.image.load(os.path.join(GFX, 'character1/walk_left/character1_walk_left2.png')),
    pg.image.load(os.path.join(GFX, 'character1/walk_left/character1_walk_left3.png')),
    pg.image.load(os.path.join(GFX, 'character1/walk_left/character1_walk_left4.png')),
    pg.image.load(os.path.join(GFX, 'character1/walk_left/character1_walk_left5.png')),
    pg.image.load(os.path.join(GFX, 'character1/walk_left/character1_walk_left6.png')),
    pg.image.load(os.path.join(GFX, 'character1/walk_left/character1_walk_left7.png')),
    pg.image.load(os.path.join(GFX, 'character1/walk_left/character1_walk_left8.png')),
]

BOMB = pg.image.load(os.path.join(GFX, 'danger_objects/bomb.png'))

HP0 = pg.image.load(os.path.join(GFX, 'hp0.png'))
HP1 = pg.image.load(os.path.join(GFX, 'hp1.png'))
HP2 = pg.image.load(os.path.join(GFX, 'hp2.png'))
