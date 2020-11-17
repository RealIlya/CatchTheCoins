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
        self.background = self.win.blit(self.bg_img, (0, 0))

    def new_game_level1(self):
        hud = HUD(window=self.win, size=self.size, barrier=self.barrier)
        player = Player(window=self.win, size=self.size, barrier=self.barrier)
        level_1 = L1.Level1(window=self.win, size=self.size)

        bombs = []
        hp = 6
        hit = 0
        clock = pg.time.Clock()

        running = True
        while running:
            clock.tick(self.fps)

            FPS_now = clock.get_fps()
            # print(FPS_now)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

            self.background = self.win.blit(self.bg_img, (0, 0))

            # if bombs.count()

            for _bomb in bombs:
                if _bomb.bomb_rect.y > self.size[1]:
                    bombs.pop(bombs.index(_bomb))

                if _bomb.bomb_rect.bottom > player.y and _bomb.bomb_rect.left < player.x + player.width and \
                        _bomb.bomb_rect.right > player.x and hit == 0:
                    hp -= 1
                    hit = 1

            keys = pg.key.get_pressed()

            if keys[pg.K_RETURN]:
                if len(bombs) < 2:
                    bombs.append(Bomb(window=self.win, size=self.size, barrier=self.barrier))
                    hit = 0
            for bomb in bombs:
                bomb.draw()

            print(hp)

            hud.draw_hp()
            player.control()
            player.draw()
            level_1.generate()

            self.update()

        pg.quit()

    def update(self):
        pg.display.update()


if __name__ == '__main__':
    game = GameLevel1()
    game.new_game_level1()
