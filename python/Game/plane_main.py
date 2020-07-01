import pygame
from plane_sprites import *

class PlaneGame(object):
    #主程序
    def __init__(self):
        print("游戏初始化")

        #创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size())
        #创建时钟
        self.clock = pygame.time.Clock()
        #调用私有方法，精灵的创建
        self.__create_sprites()

    def __create_sprites(self):
        pass

    def start_game(self):
        print("游戏开始")

if __name__ == '__main__':
    #创建游戏
    game = PlaneGame()
    game.start_game()