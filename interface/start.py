import sys
import pygame
def start(screen,image_paths):
    BeginImages=[pygame.image.load(image_paths[0]),pygame.image.load(image_paths[1])]
    BeginImage=BeginImages[0]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()#关闭库？
                sys.exit()#可以抛出异常
            elif event.type==pygame.MOUSEMOTION:
                MousePos=pygame.mouse.get_pos()
                if MousePos[0] in list(range(419,574)) and MousePos[1] in list(range(374,416)):
                    BeginImage=BeginImages[1]
                else:
                    BeginImage=BeginImages[0]
            elif event.type == pygame.MOUSEBUTTONDOWN:
                MousePos=pygame.mouse.get_pos()
                if event.button==1 and MousePos[0] in list(range(419,574)) and MousePos[1] in list(range(374,416)):
                    return True
        screen.blit(BeginImage,(0,0))
        pygame.display.update()