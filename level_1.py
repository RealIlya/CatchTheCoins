import pygame as pg
from data import graphics as gs


class Level1:
    def __init__(self, window, size):
        self.win = window
        self.size = size

        self.barrier_block = gs.LEVEL1_BARRIER_BLOCK
        self.down_block = gs.LEVEL1_DOWN_BLOCK
        self.barrier_block_width, self.barrier_block_height = self.barrier_block.get_width(), \
                                                              self.barrier_block.get_height()
        self.down_block_width, self.down_block_height = self.down_block.get_width(), \
                                                        self.down_block.get_height()

    def generate(self):
        self.barrier_block_x, self.barrier_block_y = 0, 0
        self.down_block_x, self.down_block_y = 0, 0

        level = [
            '=                  =',
            '=                  =',
            '=                  =',
            '=                  =',
            '=                  =',
            '=                  =',
            '=                  =',
            '=                  =',
            '=                  =',
            '=                  =',
            '=                  =',
            '=                  =',
            '=                  =',
            '=                  =',
            '=                  =',
            '=                  =',
            '=                  =',
            '=                  =',
            '=                  =',
            '=                  =',
            '=                  =',
            '=                  =',
            '=                  =',
            '=                  =',
            '=------------------='
        ]

        for row in level:
            for symbol in row:
                if symbol == '=':
                    self.win.blit(self.barrier_block, (self.barrier_block_x, self.barrier_block_y))

                if symbol == '-':
                    self.win.blit(self.down_block, (self.down_block_x, self.down_block_y))

                self.barrier_block_x += self.barrier_block_width
                self.down_block_x += self.down_block_width
            self.barrier_block_y += self.barrier_block_height
            self.down_block_y += self.down_block_height
            self.barrier_block_x = 0
            self.down_block_x = 0
