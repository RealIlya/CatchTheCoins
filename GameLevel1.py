import pygame as pg

from data import graphics as gs
from game_objects import Player, Bomb, HUD
from levels import level_1 as L1


# TODO: добавить новые "опасные объекты"


class GameLevel1:

    def __init__(self):
        pg.init()
        self.fps = 60
        self.size = [640, 800]
        self.win = pg.display.set_mode(self.size)
        self.barrier = 0
        self.bg_img = gs.BG

        self.player = Player(window=self.win, size=self.size, barrier=self.barrier)
        self.level_1 = L1.Level1(window=self.win, size=self.size)
        self.hp = self.player.hp
        self.bomb_speed = [0, 3]

    def new_game_level1(self):
        bombs = []
        hit = 0
        clock = pg.time.Clock()

        running = True
        while running:
            pg.time.delay(10)
            clock.tick(self.fps)

            FPS_now = clock.get_fps()
            # print(FPS_now)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

            if self.hp == 0:
                self.new_game_level1()

            self.background = self.win.blit(self.bg_img, (0, 0))

            keys = pg.key.get_pressed()

            if keys[pg.K_RETURN]:
                if len(bombs) < 6:
                    bombs.append(Bomb(window=self.win, size=self.size, barrier=self.barrier, speed=self.bomb_speed))
                    hit = 0
            for bomb in bombs:
                bomb.draw()

            for _bomb in bombs:
                if _bomb.bomb_rect.y > self.size[1]:
                    bombs.pop(bombs.index(_bomb))

                if _bomb.bomb_rect.bottom > self.player.y and \
                        _bomb.bomb_rect.left < self.player.x + self.player.width and \
                        _bomb.bomb_rect.right > self.player.x and hit == 0:
                    self.hp -= 1
                    hit = 1

            self.update()

        pg.quit()

    def update(self):
        hud = HUD(window=self.win, size=self.size, barrier=self.barrier, status_hp=self.hp)

        hud.draw_hp()
        self.player.control()
        self.player.draw()
        self.level_1.generate()
        pg.display.update()


if __name__ == '__main__':
    game = GameLevel1()
    game.new_game_level1()
