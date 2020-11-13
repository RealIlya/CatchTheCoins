import pygame as pg
from data import graphics as gs


class Level1:

    def __init__(self, window, size):
        self.win = window
        self.size = size

        self.down_block = gs.LEVEL1_DOWN_BLOCK
        self.down_block_width, self.down_block_height = self.down_block.get_width(), \
                                                        self.down_block.get_height()

    def generate(self):
        self.down_block_x, self.down_block_y = 0, 768

        level = [
            '--------------------'
        ]

        for row in level:
            for symbol in row:
                if symbol == '-':
                    self.win.blit(self.down_block, (self.down_block_x, self.down_block_y))

                self.down_block_x += self.down_block_width
            self.down_block_y += self.down_block_height
            self.down_block_x = 0
