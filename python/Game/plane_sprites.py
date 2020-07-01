import pygame

#屏幕大小常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
FRAME_PER_SECOND = 60

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
