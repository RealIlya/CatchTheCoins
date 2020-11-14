import pygame as pg
from data import graphics as gs
from game_objects import Player, Bomb
from level_1 import Level1


# TODO:

class Game:

    def __init__(self):
        pg.init()
        self.fps = 60
        self.size = [640, 800]
        self.win = pg.display.set_mode(self.size)
        self.barrier = 0
        self.bg_img = gs.BG
        self.background = self.win.blit(self.bg_img, (0, 0))

    def new_game(self):
        player = Player(window=self.win, size=self.size, barrier=self.barrier)
        level_1 = Level1(window=self.win, size=self.size)

        bombs = []

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

            for _bomb in bombs:
                if _bomb.bomb_rect.y > self.size[1]:
                    bombs.pop(bombs.index(_bomb))

                if _bomb.bomb_rect.bottom > player.y and _bomb.bomb_rect.left < player.x and _bomb.bomb_rect.right < player.x:
                    print("Уничтожен")

            keys = pg.key.get_pressed()

            if keys[pg.K_f]:
                if len(bombs) < 1:
                    print("Успешно")
                    bombs.append(Bomb(window=self.win, size=self.size, barrier=self.barrier))
            for bomb in bombs:
                bomb.draw()

            print(player.x)

            player.control()
            player.draw()
            level_1.generate()

            self.update()

        pg.quit()

    def update(self):
        pg.display.update()


if __name__ == '__main__':
    game = Game()
    game.new_game()
