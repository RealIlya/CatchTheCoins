import pygame as pg


class Player:
    def __init__(self, window, size, barrier):
        self.win = window
        self.size = size
        self.barrier = barrier

        self.color_red = (255, 0, 0)
        self.width, self.height = 30, 55
        self.x, self.y = (self.size[0] - self.width) // 2, self.size[1] - self.height - 32
        self.speed = (2, 2)

        self.max_dashes = 5
        self.right_dash_count = 8
        self.is_right_dash = False
        self.left_dash_count = 8
        self.is_left_dash = False

    # управление персонажем
    def control(self):
        keys = pg.key.get_pressed()

        print(self.max_dashes)

        if self.is_right_dash:
            self.dash_right()
        elif self.is_left_dash:
            self.dash_left()

        # блок проверки дэша
        if self.max_dashes > 0:
            # вправо
            if keys[pg.K_RIGHT] and keys[pg.K_SPACE]:
                self.is_right_dash = True

            # влево
            elif keys[pg.K_LEFT] and keys[pg.K_SPACE]:
                self.is_left_dash = True

        if self.x > self.size[0] - self.width - self.barrier:
            self.x = self.size[0] - self.width - self.barrier

        if self.x < self.barrier:
            self.x = self.barrier

        # передвижение персонажа вправо
        if keys[pg.K_RIGHT] and self.x < self.size[0] - self.width - self.barrier:
            self.x += self.speed[0]

        # передвижение персонажа влево
        if keys[pg.K_LEFT] and self.x > self.barrier:
            self.x -= self.speed[0]

    # дэш вправо
    def dash_right(self):
        if self.right_dash_count >= 0:
            self.x += self.right_dash_count * 2
            self.right_dash_count -= 1
        else:
            self.right_dash_count = 8
            self.is_right_dash = False
            self.max_dashes -= 1

    # дэш влево
    def dash_left(self):
        if self.left_dash_count >= 0:
            self.x -= self.left_dash_count * 2
            self.left_dash_count -= 1
        else:
            self.left_dash_count = 8
            self.is_left_dash = False
            self.max_dashes -= 1

    def draw_player(self):
        self.rect = pg.draw.rect(self.win, self.color_red, (self.x, self.y, self.width, self.height))
        # self.rect = self.rect.move(self.x, self.y)


class Ball:
    pass
