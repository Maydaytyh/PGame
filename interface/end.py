import sys
import pygame
def end(screen,EndImagePaths,AgainImagePaths,ScoreInfo,FontPath,FontColors,ScreenSize):
    EndImage=pygame.image.load(EndImagePaths)
    AgainImages=[pygame.image.load(AgainImagePaths[0]),pygame.image.load(AgainImagePaths[1])]
    AgainImage=AgainImages[0]
    font=pygame.font.Font(FontPath,50)
    ScoreText=font.render('Your Score%s'%ScoreInfo['YourScore'],True,FontColors[0])
    ScoreRect=ScoreText.get_rect()
    ScoreRect.left,ScoreRect.top=(ScreenSize[0]-ScoreRect.width)/2,215
    BestText=font.render("Best Score%s"%ScoreInfo['BestScore'],True,FontColors[1])
    BestTextRect=BestText.get_rect()
    BestTextRect.left,BestTextRect.top=(ScreenSize[0]-BestTextRect.width)/2,275
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.MOUSEMOTION:
                MousePos=pygame.mouse.get_pos()
                if MousePos[0] in list(range(419,574)) and MousePos[1] in list(range(374,416)):
                    AgainImage=AgainImages[1]
                else:
                    AgainImage=AgainImages[0]
            elif event.type==pygame.MOUSEBUTTONDOWN:
                MousePos=pygame.mouse.get_pos()
                if event.button==1 and  MousePos[0] in list(range(419,574)) and MousePos[1] in list(range(374,416)):
                    return True
        screen.blit(EndImage,(0,0))
        screen.blit(AgainImage,(416,370))
        screen.blit(ScoreText,ScoreRect)
        screen.blit(BestText,BestTextRect)
        pygame.display.update()       