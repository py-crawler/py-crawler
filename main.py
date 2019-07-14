import pygame

from src.game.game import Game


def main():
    g = Game()
    g.show_start_screen()
    while g.running:
        g.new()
        g.show_go_screen()

    pygame.quit()


if __name__ == '__main__':
    main()
