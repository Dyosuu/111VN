import pygame
import sys
import os
import datetime


def ButtonNext(NextButton, MenuButton):
    global size,screen,clock,fps,SceneNum,LineNum

    while True:        
        for event in pygame.event.get():            
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if NextButton.collidepoint(mouse_pos):
                    SceneNo(SceneNum, LineNum)
                elif MenuButton.collidepoint(mouse_pos):
                    Menu()                
        pygame.display.update()
        clock.tick(fps)

def Menu():
    global screen,size, SceneNum, LineNum, saves
    x = 0
    img0, imgrect0 = ButtonResize('../Img/opbg.png',size,(0,0),screen)
    img1, imgrect1 = ButtonResize('../Img/op1.png',(150,80),(1430,20),screen)
    myfont = pygame.font.SysFont("Arial", 35)
    label = myfont.render("Back", 1, [250,250,250])
    screen.blit(label, (1465, 40))
    img2, imgrect2 = ButtonResize('../Img/op1.png',(650,200),(470,100),screen)
    img3, imgrect3 = ButtonResize('../Img/op2.png',(650,200),(470,240),screen)
    img4, imgrect4 = ButtonResize('../Img/op3.png',(650,200),(470,390),screen)
    img5, imgrect5 = ButtonResize('../Img/op4.png',(650,200),(470,530),screen)

    myfont = pygame.font.SysFont("Arial", 60)
    label = myfont.render("Save", 1, [100,100,100])
    screen.blit(label, (723, 162))   
    label = myfont.render("Save", 1, [200,200,200])
    screen.blit(label, (725, 160))   

    label = myfont.render("Load", 1, [100,100,100])
    screen.blit(label, (723, 302))   
    label = myfont.render("Load", 1, [200,200,200])
    screen.blit(label, (725, 300))   

    label = myfont.render("Treasure", 1, [100,100,100])
    screen.blit(label, (683, 442))   
    label = myfont.render("Treasure", 1, [200,200,200])
    screen.blit(label, (685, 440))

    label = myfont.render("Quit", 1, [100,100,100])
    screen.blit(label, (738, 602))   
    label = myfont.render("Quit", 1, [200,200,200])
    screen.blit(label, (740, 600))
    
    pygame.display.update()
    
    while True:        
        for event in pygame.event.get():            
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                pygame.mixer.music.stop()
                if imgrect1.collidepoint(mouse_pos):
                    SceneNo(SceneNum,LineNum+1)
                elif imgrect2.collidepoint(mouse_pos):
                    img0, imgrect0 = ButtonResize('../Img/start.png',size,(0,0),screen)
                    img0, imgrect0 = ButtonResize('../Img/opbg.png',size,(0,0),screen)
                    img1, imgrect1 = ButtonResize('../Img/op1.png',(150,80),(1430,20),screen)
                    myfont = pygame.font.SysFont("Arial", 35)
                    label = myfont.render("Back", 1, [250,250,250])
                    screen.blit(label, (1465, 40))
                    img2, imgrect2 = ButtonResize('../Img/op1.png',(500,200),(550,100),screen)
                    label = myfont.render(saves[0], 1, [250,250,250])
                    screen.blit(label, (560, 150))
                    img3, imgrect3 = ButtonResize('../Img/op2.png',(500,200),(550,240),screen)
                    img4, imgrect4 = ButtonResize('../Img/op3.png',(500,200),(550,390),screen)
                    img5, imgrect5 = ButtonResize('../Img/op4.png',(500,200),(550,530),screen)
                    img6, imgrect6 = ButtonResize('../Img/op1.png',(500,200),(70,200),screen)
                    img7, imgrect7 = ButtonResize('../Img/op2.png',(500,200),(70,340),screen)
                    img8, imgrect8 = ButtonResize('../Img/op3.png',(500,200),(70,490),screen)
                    img2, imgrect2 = ButtonResize('../Img/op1.png',(500,200),(1070,200),screen)
                    img3, imgrect3 = ButtonResize('../Img/op2.png',(500,200),(1070,340),screen)
                    img4, imgrect4 = ButtonResize('../Img/op3.png',(500,200),(1070,490),screen)
                    pygame.display.update()
                    while True:
                        for event in pygame.event.get():            
                            if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                mouse_pos = event.pos
                                if imgrect1.collidepoint(mouse_pos):
                                    img0, imgrect0 = ButtonResize('../Img/start.png',size,(0,0),screen)
                                    Menu()
                                elif imgrect2.collidepoint(mouse_pos):
                                    x =0
                                    print(x)
                                elif imgrect3.collidepoint(mouse_pos):
                                    x =1
                                elif imgrect4.collidepoint(mouse_pos):
                                    x =2
                                elif imgrect5.collidepoint(mouse_pos):
                                    x =3
                        pygame.display.update()
                        clock.tick(fps)
                    x = "../Saves/" + str(x)
                    file = open( x ,"w") 
                    file.write(str(SceneNum)+" "+str(LineNum))
                    file.close()
                    Menu()
                                            
                elif imgrect3.collidepoint(mouse_pos):
                    print("Load Game")
                    #load something
                elif imgrect4.collidepoint(mouse_pos):
                    print("open Store")
                    #load something
                elif imgrect5.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit
        pygame.display.update()
        clock.tick(fps)
    return False


def SceneNo(num,line):
    global LineNum
    if line != 1:
        LineNum = line-1
        if num == 1:
                Scene1()
        elif num ==2:
                Scene2()
    else:
        if num == 1:
            LineNum = 3
            Scene2()
        elif num ==2:
            LineNum = 3
            Scene3()
                
def ButtonResize(pic, size, cord, screen):
    img = pygame.image.load(pic).convert_alpha()
    img = pygame.transform.scale(img, size)
    imgrect = img.get_rect()
    imgrect.topleft = cord
    screen.blit(img, imgrect)
    return img, imgrect

def Start():
    global screen,size, LineNum
    img1, imgrect1 = ButtonResize('../Img/start.png',size,(0,0),screen)
    img0, imgrect0 = ButtonResize('../Img/opbg.png',size,(0,0),screen)
    img2, imgrect2 = ButtonResize('../Img/op1.png',(650,200),(470,200),screen)
    img3, imgrect3 = ButtonResize('../Img/op2.png',(650,200),(470,340),screen)
    img4, imgrect4 = ButtonResize('../Img/op3.png',(650,200),(470,490),screen)

    myfont = pygame.font.SysFont("Arial", 60)
    label = myfont.render("New Game", 1, [100,100,100])
    screen.blit(label, (648, 262))   
    label = myfont.render("New Game", 1, [200,200,200])
    screen.blit(label, (650, 260))   

    label = myfont.render("Load Game", 1, [100,100,100])
    screen.blit(label, (643, 402))   
    label = myfont.render("Load Game", 1, [200,200,200])
    screen.blit(label, (645, 400))   

    label = myfont.render("Quit", 1, [100,100,100])
    screen.blit(label, (723, 542))   
    label = myfont.render("Quit", 1, [200,200,200])
    screen.blit(label, (725, 540))
    
    pygame.display.update()
    
    while True:        
        for event in pygame.event.get():            
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                pygame.mixer.music.stop()
                if imgrect2.collidepoint(mouse_pos):
                    LineNum = 3
                    Scene1()
                elif imgrect3.collidepoint(mouse_pos):
                    print("Load Game")
                    #load something
                elif imgrect4.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit
        pygame.display.update()
        clock.tick(fps)
    return False

def Scene1():
    global screen,size, SceneNum, LineNum
    SceneNum = 1
    myfont = pygame.font.SysFont("Arial", 35)
    if LineNum == 3:
        pygame.mixer.music.load('../Music/M2.mp3')
        pygame.mixer.music.play(-1)
        img1, imgrect1 = ButtonResize('../Img/Vill.jpg',size,(0,0),screen)
        img2, imgrect2 = ButtonResize('../Img/otextbox.png',(1180,600),(200,400),screen)
        label = myfont.render("Text goes here, Text goes here", 1, [250,250,250])
        screen.blit(label, (598, 722))
        pygame.display.update()
    elif LineNum == 2:
        pygame.mixer.music.load('../Music/M3.mp3')
        pygame.mixer.music.play(-1)
        img1, imgrect1 = ButtonResize('../Img/Kill.jpg',size,(0,0),screen)
        img2, imgrect2 = ButtonResize('../Img/otextbox.png',(1180,600),(200,400),screen)
        label = myfont.render("Text does not go here", 1, [250,250,250])
        screen.blit(label, (658, 722))
        pygame.display.update()
    elif LineNum == 1:
        img2, imgrect2 = ButtonResize('../Img/otextbox.png',(1180,600),(200,400),screen)
        label = myfont.render("End of Scene", 1, [250,250,250])
        screen.blit(label, (708, 722))
        pygame.display.update()
    img3, imgrect3 = ButtonResize('../Img/next.png',(100,50),(1180,770),screen)
    img4, imgrect4 = ButtonResize('../Img/op1.png',(150,80),(1430,20),screen)
    label = myfont.render("Menu", 1, [250,250,250])

    screen.blit(label, (1460, 40))
    ButtonNext(imgrect3,imgrect4)
    
    
def Scene2():
    global screen,size, SceneNum, LineNum
    SceneNum = 2
    myfont = pygame.font.SysFont("Arial", 35)
    
    img1, imgrect1 = ButtonResize('../Img/bg1.jpg',size,(0,0),screen)
    img2, imgrect2 = ButtonResize('../Img/otextbox.png',(1180,600),(200,400),screen)
    img3, imgrect3 = ButtonResize('../Img/next.png',(100,50),(1180,770),screen)
    if LineNum == 3:
        label = myfont.render("Scene 2, Idk what happens", 1, [250,250,250])
        screen.blit(label, (598, 722))
        pygame.display.update()
    elif LineNum == 2:
        label = myfont.render("Space holder lng to :D", 1, [250,250,250])
        screen.blit(label, (658, 722))
        pygame.display.update()
    elif LineNum == 1:
        label = myfont.render("End of Scene", 1, [250,250,250])
        screen.blit(label, (708, 722))
        pygame.display.update()
    ButtonNext(imgrect3)
    
def main():
    global size,screen,clock,fps,myfont,saves
    pygame.init()
    clock = pygame.time.Clock()
    fps = 60
    size = [1600, 900]
    screen = pygame.display.set_mode(size)
    img1, imgrect1 = ButtonResize('../Img/start.png',size,(0,0),screen)
    saves = ['--','--','--','--','--','--','--','--','--']

    myfont = pygame.font.SysFont("Arial", 35)
    label = myfont.render("Click anywhere to start", 1, [0,0,0])
    screen.blit(label, (598, 722))
    label = myfont.render("Click anywhere to start", 1, [250,250,250])
    screen.blit(label, (600, 720))
    pygame.display.update()
    pygame.mixer.music.load('../Music/M1.mp3')
    pygame.mixer.music.play(-1)
    while True:        
        for event in pygame.event.get():            
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit
            if event.type == pygame.MOUSEBUTTONDOWN:
                Start()
                return False
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    sys.exit


if __name__ == '__main__':
    main()
    #bigbutton = pygame.Rect(200, 500, 150, 150)  # creates a rect object
    # The rect method is similar to a list but with a few added perks
    # for example if you want the position of the button you can simpy type
    # button.x or button.y or if you want size you can type button.width or
    # height. you can also get the top, left, right and bottom of an object
    # with button.right, left, top, and bottom
    #smallbutton = pygame.Rect(400, 500, 150, 150)

##    img0, imgrect0 = ButtonResize('opbg.png',size,(0,0),screen)
##    img2, imgrect2 = ButtonResize('op1.png',(650,200),(470,100),screen)
##    img3, imgrect3 = ButtonResize('op2.png',(650,200),(470,240),screen)
##    img4, imgrect4 = ButtonResize('op3.png',(650,200),(470,390),screen)
##    img5, imgrect5 = ButtonResize('op4.png',(650,200),(470,530),screen)
