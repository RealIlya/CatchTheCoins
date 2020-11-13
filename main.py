import pygame as pg
from data import graphics as gs
from game_objects import Player
from level_1 import Level1


# TODO: оптимизировать отрисовку изображений

class Game:

    def __init__(self):
        pg.init()
        self.fps = 60
        self.size = [640, 800]
        self.win = pg.display.set_mode(self.size)
        self.barrier = 32
        self.bg_img = gs.BG
        self.background = self.win.blit(self.bg_img, (0, 0))

    def new_game(self):
        player = Player(window=self.win, size=self.size, barrier=self.barrier)
        level_1 = Level1(window=self.win, size=self.size)

        clock = pg.time.Clock()

        running = True
        while running:

            clock.tick(self.fps)

            FPS_now = clock.get_fps()
            print(FPS_now)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

            self.background = self.win.blit(self.bg_img, (0, 0))

            level_1.generate()
            player.control()
            player.draw_player()

            self.update()

        pg.quit()

    def update(self):
        pg.display.update()


if __name__ == '__main__':
    game = Game()
    game.new_game()
