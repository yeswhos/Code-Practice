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
# pygame.display.update()

hero = pygame.image.load("D:\GitR\Code-Practice\python\Game\images\me1.png")
screen.blit(hero, (200, 500))

#可最后同意调用update方法
pygame.display.update()

#创建时钟对象
clock = pygame.time.Clock()

#rect记录飞机初始位置
hero_rect = pygame.Rect(150, 300, 102, 126)


while True:
    #代码执行的频率
    clock.tick(60)

    #捕获事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("tuichuyouxi")
            pygame.quit()
            exit()

    #修改飞机位置
    hero_rect.y -= 1
    if(hero_rect.y <= -126):
        hero_rect.y = 700
    #调用blit方法绘制图像
    screen.blit(background, (0, 0))
    screen.blit(hero, hero_rect)
    pygame.display.update()

    pygame.event.get(1000)
    pass

pygame.quit()