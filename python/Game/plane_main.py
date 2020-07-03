import pygame
from plane_sprites import *

class PlaneGame(object):
    #主程序
    def __init__(self):
        print("游戏初始化")

        #创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        #创建时钟
        self.clock = pygame.time.Clock()
        #调用私有方法，精灵的创建
        self.__create_sprites()

        #设置定时器事件, 创建敌机
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)


    def __create_sprites(self):
        #创建背景精灵和精灵组
        # bg1 = Background("D:\GitR\Code-Practice\python\Game\images\\background.png")
        # bg2 = Background("D:\GitR\Code-Practice\python\Game\images\\background.png")
        #bg2.rect.y = -bg2.rect.height

        #初始化background之后的方法
        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)

        #创建精灵组
        self.enemy_group = pygame.sprite.Group()

    def start_game(self):
        print("游戏开始")
        while True:
            #设置刷新率
            self.clock.tick(FRAME_PER_SECOND)
            #事件监听
            self.__event_handler()
            #碰撞检测
            self.__check_collide()
            #更新/绘制精灵组
            self.__update_sprites()
            #更新显示
            pygame.display.update()
            pass

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif (event.type == CREATE_ENEMY_EVENT):
                #创建敌机精灵
                enemy = Enemy()
                self.enemy_group.add(enemy)
                print("敌机出场")

    def __check_collide(self):
        pass
    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()

if __name__ == '__main__':
    #创建游戏
    game = PlaneGame()
    game.start_game()