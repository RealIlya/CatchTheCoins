import pygame as pg
from data import graphics as gs


class Player:

    def __init__(self, window, size, barrier):
        self.win = window
        self.size = size
        self.barrier = barrier

        self.char1_stand = gs.CHAR1_STAND
        self.char1_walk_right = gs.CHAR1_WALK_RIGHT
        self.char1_walk_left = gs.CHAR1_WALK_LEFT
        self.char1_dodge_right = gs.CHAR1_DODGE_RIGHT
        self.char1_dodge_left = gs.CHAR1_DODGE_LEFT
        self.anim_count = None

        self.width, self.height = 96, 128
        self.x, self.y = (self.size[0] - self.width) // 2, self.size[1] - self.height - 32
        self.speed = (2, 2)

        self.is_right = False
        self.is_left = False

        self.max_dashes = 5
        self.right_dash_count = 8
        self.is_right_dodge = False
        self.left_dash_count = 8
        self.is_left_dodge = False

    # управление персонажем
    def control(self):
        keys = pg.key.get_pressed()

        # передвижение персонажа вправо
        if keys[pg.K_RIGHT] and self.x < self.size[0] - self.width - self.barrier:
            self.x += self.speed[0]
            self.is_right = True
            self.is_left = False
        # передвижение персонажа влево
        elif keys[pg.K_LEFT] and self.x > self.barrier:
            self.x -= self.speed[0]
            self.is_right = False
            self.is_left = True
        # персонаж стоит
        else:
            self.is_right = False
            self.is_left = False
            self.is_right_dodge = False
            self.is_left_dodge = False
            self.anim_count = 0

        if self.is_right_dodge:
            self.dodge_right()
        elif self.is_left_dodge:
            self.dodge_left()

        # блок проверки переката
        if self.max_dashes > 0:
            # вправо
            if keys[pg.K_RIGHT] and keys[pg.K_SPACE]:
                self.is_right_dodge = True
                self.is_right = False
                self.is_left = False
            # влево
            elif keys[pg.K_LEFT] and keys[pg.K_SPACE]:
                self.is_left_dodge = True
                self.is_right = False
                self.is_left = False

        if self.x > self.size[0] - self.width - self.barrier:
            self.x = self.size[0] - self.width - self.barrier
        if self.x < self.barrier:
            self.x = self.barrier

        if self.anim_count + 1 >= 60:
            self.anim_count = 0

    # перекат вправо
    def dodge_right(self):
        if self.right_dash_count >= 0:
            self.x += self.right_dash_count * 2
            self.right_dash_count -= 1
        else:
            self.right_dash_count = 8
            self.is_right_dodge = False
            self.max_dashes -= 1

    # перекат влево
    def dodge_left(self):
        if self.left_dash_count >= 0:
            self.x -= self.left_dash_count * 2
            self.left_dash_count -= 1
        else:
            self.left_dash_count = 8
            self.is_left_dodge = False
            self.max_dashes -= 1

    def draw(self):
        if self.is_right_dodge is False and self.is_left_dodge is False:
            if self.is_right:
                self.win.blit(self.char1_walk_right[self.anim_count // 8], (self.x, self.y))
                self.anim_count += 1
            elif self.is_left:
                self.win.blit(self.char1_walk_left[self.anim_count // 8], (self.x, self.y))
                self.anim_count += 1
            else:
                self.win.blit(self.char1_stand, (self.x, self.y))

        else:
            if self.is_right_dodge:
                self.win.blit(self.char1_dodge_right, (self.x, self.y))
            elif self.is_left_dodge:
                self.win.blit(self.char1_dodge_left, (self.x, self.y))


class Bomb:

    def __init__(self, window, size, barrier):
        import random
        self.win = window
        self.size = size
        self.barrier = barrier

        self.bomb_img = gs.BOMB
        self.bomb_rect = self.bomb_img.get_rect()
        self.bomb_rect = self.bomb_rect.move(random.randint(0, self.size[0] - self.bomb_img.get_width()),
                                             random.randrange(-90, -120, -10))
        self.width = self.bomb_rect.width
        self.height = self.bomb_rect.height

        self.x = self.bomb_rect.centerx
        self.y = self.bomb_rect.centery

    def draw(self):
        self.bomb_rect = self.bomb_rect.move(0, 3)
        self.win.blit(self.bomb_img, self.bomb_rect)
        pg.draw.rect(self.win, (230, 0, 0), self.bomb_rect)
