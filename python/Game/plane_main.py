import pygame
from plane_sprites import *

class PlaneGame(object):
    #主程序
    def __init__(self):
        print("游戏初始化")

    def start_game(self):
        print("游戏开始")

if __name__ == '__main__':
    #创建游戏
    game = PlaneGame()
    game.start_game()