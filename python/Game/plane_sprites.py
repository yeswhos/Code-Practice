import random

import pygame

#屏幕大小常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
#刷新频率
FRAME_PER_SECOND = 60
#敌机定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
#子弹发射事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1

#封装图像，位置和速度，提供update方法，根据需求更新位置rect
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image_name, speed = 1):
        #不是继承object的类，都需要调用父类的初始化方法
        super().__init__()

        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        #垂直方向移动
        self.rect.y += self.speed

#继承父类的方法，不能满足子类需求
#派生一个新的子类
#在子类针对特有的需求，重写父类方法，并进行扩展
class Background(GameSprite):
    def __init__(self, is_alt = False):
        super().__init__("D:\GitR\Code-Practice\python\Game\images\\background.png")
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        #继承父类方法实现
        super().update()
        #判断是否移出屏幕，如果移出屏幕，将图像设置为屏幕的上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height

class Enemy(GameSprite):
    def __init__(self):
        #调用父类方法创建敌机精灵，同时指定敌机图片
        super().__init__("D:\GitR\Code-Practice\python\Game\images\enemy1.png")
        #指定敌机的初始随即速度
        self.speed = random.randint(1, 3)
        #指定敌机的初始随机位置
        #更平缓出现，y方向的设置
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)
    def update(self):
        #调用父类方法，保持垂直方向飞行
        super().update()
        #判断是否飞出屏幕，如果是，需要从精灵组删除飞机
        if self.rect.y >= SCREEN_RECT.height:
            #将精灵从精灵组移除并自动销毁，避免内存消耗
            self.kill()
            print("删除该精灵")
    def __del__(self):
        pass

class Hero(GameSprite):
    def __init__(self):
        #调用父类方法，设置image & speed
        super().__init__("D:\GitR\Code-Practice\python\Game\images\me1.png", 0)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

    def update(self):
        self.rect.x += self.speed
        #控制英雄不离开屏幕
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        print("发射子弹")