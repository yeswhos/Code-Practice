import pygame

pygame.init()
#set_mode(resolution = (0, 0), flags = 0, depth = 0)
#resolution屏幕宽和高
#flag是否全屏等等
#depth颜色的位数，自动匹配

screen = pygame.display.set_mode((480, 700))

#加载图像
background = pygame.image.load("D:\GitR\Code-Practice\python\Game\images\\background.png")
#绘制图像
screen.blit(background, (0, 0))
#更新屏幕显示
pygame.display.update()
while True:
    pygame.event.get(1000)
    pass

pygame.quit()