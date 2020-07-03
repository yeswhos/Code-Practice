import pygame

#屏幕大小常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
FRAME_PER_SECOND = 60
CREATE_ENEMY_EVENT = pygame.USEREVENT

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
        #指定敌机的初始随即速度
        #指定敌机的初始随机位置
        pass
    def update(self):
        #调用父类方法，保持垂直方向飞行
        #判断是否飞出屏幕，如果是，需要从精灵组删除飞机
        pass

