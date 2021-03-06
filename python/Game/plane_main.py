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
        #发射子弹
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

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

        #创建英雄
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

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
            elif(event.type == HERO_FIRE_EVENT):
                self.hero.fire()
                # print("敌机出场")
            #一种按键操作
            # elif(event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT):
            #     print("向右")
        #第二种按键操作，通过键盘常量，按键的元组，按下就一直有，上面的是按下抬起是一次。
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            print("向右")
            self.hero.speed = 2
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0

    def __check_collide(self):
        #子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
        #敌机撞毁英雄，返回列表
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        #判断列表是否有内容
        if len(enemies) > 0:
            #牺牲
            self.hero.kill()
            #结束游戏
            PlaneGame.__game_over()

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()

if __name__ == '__main__':
    #创建游戏
    game = PlaneGame()
    game.start_game()