import pygame
import random
import config
from sprites.hammer import *
from sprites.mole import *
from interface.end import *
from interface.start import *
def InitGame():
    pygame.init()
    pygame.mixer.init()
    screen=pygame.display.set_mode(config.ScreenSize)
    pygame.display.set_caption('GuguMelon\'s Mouse')
    return screen
def main():
    pygame.init()
    pygame.mixer.init()
    screen=pygame.display.set_mode(config.ScreenSize)
    pygame.display.set_caption('GuguMelon\'s Mouse')
    # screen=InitGame()
    pygame.mixer.music.load(config.BgmPath)
    pygame.mixer.music.play(-1)
    audios={
        'CountDown':pygame.mixer.Sound(config.CountdownSoundPath),
        'Hammering':pygame.mixer.Sound(config.HammeringSoundPath)
    }
    font=pygame.font.Font(config.FontPath,40)
    BackImage=pygame.image.load(config.GameBackImagePath)
    start(screen,config.GameBeginImagePaths)
    HolePos=random.choice(config.HolePosition)
    ChangeHoleEvent=pygame.USEREVENT
    pygame.time.set_timer(ChangeHoleEvent,800)
    Mole=mole(config.MoleImagePaths,HolePos)
    hammer=Hammer(config.HammerImagePaths,(500,200))
    clock=pygame.time.Clock()
    score=0
    # print(score)
    flag=False
    # TimeRemain=40
    # print(TimeRemain)
    Timetime=round((61000+pygame.time.get_ticks()))
    # print('Timetime='+str(Timetime))
    while True:
        TimeRemain=round((Timetime-pygame.time.get_ticks())/1000.)
        print(TimeRemain)
        if TimeRemain==40 and not flag:
            HolePos=random.choice(config.HolePosition)
            Mole.reset()
            Mole.SetPosition(HolePos)
            pygame.time.set_timer(ChangeHoleEvent,650)
            flag=True
        elif TimeRemain==20 and flag:
            HolePos=random.choice(config.HolePosition)
            Mole.reset()
            Mole.SetPosition(HolePos)
            pygame.time.set_timer(ChangeHoleEvent,650)
            flag=False
        if TimeRemain==10:
            audios['CountDown'].play()
        if TimeRemain<0:
            break
        CountDownText=font.render('Time: '+str(TimeRemain),True,config.White)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.MOUSEMOTION:
                hammer.SetPosition(pygame.mouse.get_pos())
            elif event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    hammer.SetHammering()
            elif event.type==ChangeHoleEvent:
                HolePos=random.choice(config.HolePosition)
                Mole.reset()
                Mole.SetPosition(HolePos)
        if hammer.is_hammering and not Mole.is_hammer:
            IsHammer=pygame.sprite.collide_mask(hammer,Mole)
            if IsHammer:
                audios['Hammering'].play()
                Mole.SetBeHammered()
                score+=10
        ScoreText=font.render('Score: '+str(score),True,config.Brown)
        screen.blit(BackImage,(0,0))
        screen.blit(CountDownText,(875,8))
        screen.blit(ScoreText,(800,430))
        Mole.draw(screen)
        hammer.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    try:
        BestScore=int(open(config.RecordPath).read())
    except:
        BestScore=0
    if score>BestScore:
        f=open(config.RecordPath,'w')
        f.write(str(score))
        f.close()
    ScoreInfo={'YourScore':score,'BestScore':BestScore}
    IsAgain=end(screen,config.GameEndImagePath,config.GameAgainImagePaths,ScoreInfo,config.FontPath,[config.White,config.Red],config.ScreenSize)
    return IsAgain
if __name__ =='__main__':
    while True:
        IsRestart=main()
        if not IsRestart:
            break            