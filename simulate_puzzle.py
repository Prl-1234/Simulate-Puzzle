import random, sys, time, pygame
from pygame.locals import *

YELLOW=(255,165,0)
BRIGHTYELLOW=	(255,255,0)
BLUE=(25,25,112)
BRIGHTBLUE=	(30,144,255)
GREEN=(0,128,0)
BRIGHTGREEN=(0,255,0)
RED=(139,0,0)
BRIGHTRED=(255,0,0)
BGCOLOR=(255,255,255)

WINDOWWIDTH=600
WINDOWHEIGHT=600

COLORS=(BLUE,GREEN,RED,YELLOW)
BRIGHTCOLORS=(BRIGHTBLUE,BRIGHTGREEN,BRIGHTRED,BRIGHTYELLOW)

YELLOWRECT=pygame.Rect(100,80,150,150)
BLUERECT=pygame.Rect(260,80,150,150)
REDRECT=pygame.Rect(100,240,150,150)
GREENRECT=pygame.Rect(260,240,150,150)
TIMEANIMATION=150




def main():
    global BGCOLOR
    pygame.init()
    FPSCLOCK=pygame.time.Clock()
    DISPLAYSURF=pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    DISPLAYSURF.fill(BGCOLOR)
    BASICFONT = pygame.font.Font('freesansbold.ttf', 36)
    score=0
    text = BASICFONT.render('Score: '+str(score), 1, YELLOW)
    textRect = text.get_rect()
    textRect.topleft = (10, 10)
    pygame.draw.rect(DISPLAYSURF,YELLOW,YELLOWRECT)
    pygame.draw.rect(DISPLAYSURF,RED,(100,240,150,150))
    pygame.draw.rect(DISPLAYSURF,BLUE,(260,80,150,150))
    pygame.draw.rect(DISPLAYSURF,GREEN,(260,240,150,150))
    p=0
    start=0
    numbers=[0,1,2,3]
    click=0
    color=[]
    for i in range(256):
        color.append(i)
    question=[]
    answer=[]
    BEEP1 = pygame.mixer.Sound('beep1.ogg')
    BEEP2 = pygame.mixer.Sound('beep2.ogg')
    BEEP3 = pygame.mixer.Sound('beep3.ogg')
    BEEP4 = pygame.mixer.Sound('beep4.ogg')
    waiting_for_sleep_to_over = True
    pl=0
    while True:
        if p==0 and start==1 and score==0:
            DISPLAYSURF.fill(BGCOLOR)
            text = BASICFONT.render('OUT!! ', 1, BLUE)
            textRect = text.get_rect()
            textRect.topleft = (250, 250)
            DISPLAYSURF.blit(text, textRect)
            pygame.display.update()


        if p==0:
            BGCOLOR=(random.choice(color),random.choice(color),random.choice(color))
        DISPLAYSURF.fill(BGCOLOR)
        pygame.draw.rect(DISPLAYSURF,YELLOW,YELLOWRECT)
        pygame.draw.rect(DISPLAYSURF,BLUE,BLUERECT)
        pygame.draw.rect(DISPLAYSURF,RED,REDRECT)
        pygame.draw.rect(DISPLAYSURF,GREEN,GREENRECT)
        text = BASICFONT.render('Score: '+str(score), 1, BLUE)
        textRect = text.get_rect()
        textRect.topleft = (10, 10)
        DISPLAYSURF.blit(text, textRect)
        pygame.display.update()
        if p==0:
            pygame.display.update()
            pygame.time.wait(TIMEANIMATION+400)
            for i in range(score+1):
                x=random.choice(numbers)
                question.append(x)
                if x==0:
                    pygame.draw.rect(DISPLAYSURF,BRIGHTBLUE,BLUERECT)
                    BEEP1.play()
                    pygame.display.update()
                    pygame.time.wait(TIMEANIMATION+300)
                    pygame.draw.rect(DISPLAYSURF,BLUE,BLUERECT)
                    pygame.display.update()
                    pygame.time.wait(TIMEANIMATION+400)
                elif x==1:
                    pygame.draw.rect(DISPLAYSURF,BRIGHTGREEN,GREENRECT)
                    pygame.display.update()
                    BEEP2.play()
                    pygame.time.wait(TIMEANIMATION+300)
                    pygame.draw.rect(DISPLAYSURF,GREEN,GREENRECT)
                    pygame.display.update()
                    pygame.time.wait(TIMEANIMATION+400)
                elif x==2:
                    pygame.draw.rect(DISPLAYSURF,BRIGHTRED,REDRECT)
                    pygame.display.update()
                    BEEP3.play()
                    pygame.time.wait(TIMEANIMATION+300)
                    pygame.draw.rect(DISPLAYSURF,RED,REDRECT)
                    pygame.display.update()
                    pygame.time.wait(TIMEANIMATION+400)
                elif x==3:
                    pygame.draw.rect(DISPLAYSURF,BRIGHTYELLOW,YELLOWRECT)
                    pygame.display.update()
                    BEEP4.play()
                    pygame.time.wait(TIMEANIMATION+300)
                    pygame.draw.rect(DISPLAYSURF,YELLOW,YELLOWRECT)
                    pygame.display.update()
                    pygame.time.wait(TIMEANIMATION+400)
            
            p=1
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==MOUSEBUTTONDOWN and pl==0:
                posx,posy=event.pos
                if YELLOWRECT.collidepoint(posx,posy):
                    pl=1
                    BEEP4.play()
                    answer=3
                    click=click+1
                    pygame.draw.rect(DISPLAYSURF,BRIGHTYELLOW,YELLOWRECT)
                    pygame.display.update()
                    pygame.time.wait(TIMEANIMATION)
                    pygame.draw.rect(DISPLAYSURF,YELLOW,YELLOWRECT)
                elif BLUERECT.collidepoint(posx,posy):
                    pl=1
                    BEEP1.play()
                    click=click+1
                    answer=0
                    pygame.draw.rect(DISPLAYSURF,BRIGHTBLUE,BLUERECT)
                    pygame.display.update()
                    pygame.time.wait(TIMEANIMATION)
                    pygame.draw.rect(DISPLAYSURF,BLUE,BLUERECT)
                elif REDRECT.collidepoint(posx,posy):
                    pl=1
                    BEEP3.play()
                    answer=2
                    click=click+1
                    pygame.draw.rect(DISPLAYSURF,BRIGHTRED,REDRECT)
                    pygame.display.update()
                    pygame.time.wait(TIMEANIMATION)
                    pygame.draw.rect(DISPLAYSURF,RED,REDRECT)
                elif GREENRECT.collidepoint(posx,posy):
                    pl=1
                    answer=1
                    click=click+1
                    BEEP2.play()
                    pygame.draw.rect(DISPLAYSURF,BRIGHTGREEN,GREENRECT)
                    pygame.display.update()
                    pygame.time.wait(TIMEANIMATION)
                    pygame.draw.rect(DISPLAYSURF,GREEN,GREENRECT)
    
        
        if click>0 :
            pl=0
            if click>len(question):
                question=[]
                click=0
                p=0
                score=0
                BEEP1.play()
                BEEP2.play()
                BEEP3.play()
                BEEP4.play()
            else:
                if answer==question[click-1]:
                    if click==score+1:
                        click=0
                        score=score+1
                        question=[]
                        p=0
                else:
                    question=[]
                    click=0
                    p=0
                    score=0
                    BEEP1.play()
                    BEEP2.play()
                    BEEP3.play()
                    BEEP4.play()

            
        start=1       
        pygame.display.update()
        FPSCLOCK.tick(30)



if __name__ == '__main__':
    main()   