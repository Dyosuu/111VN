import pygame
import sys

def ScreenSize(screen,size):
    pygame.display.set_mode(size)
    
def ButtonNext(button, SceneNum,LineNum):
    global size,screen,clock,fps

    while True:        
        for event in pygame.event.get():            
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if button.collidepoint(mouse_pos):
                    SceneNo(SceneNum,LineNum)
        pygame.display.update()
        clock.tick(fps)

def SceneNo(num,line):
    if line != 1:
        if num == 1:
                Scene1(line-1)
        elif num ==2:
                Scene2(line-1)
    else:
        if num == 1:
                Scene2(3)
        elif num ==2:
                Scene3(line)
                
def ButtonResize(pic, size, cord, screen):
    img = pygame.image.load(pic).convert_alpha()
    img = pygame.transform.scale(img, size)
    imgrect = img.get_rect()
    imgrect.topleft = cord
    screen.blit(img, imgrect)
    return img, imgrect

def Start():
    global screen,size
    img1, imgrect1 = ButtonResize('start.jpg',size,(0,0),screen)
    img0, imgrect0 = ButtonResize('opbg.png',size,(0,0),screen)
    img2, imgrect2 = ButtonResize('op1.png',(650,200),(470,200),screen)
    img3, imgrect3 = ButtonResize('op2.png',(650,200),(470,340),screen)
    img4, imgrect4 = ButtonResize('op3.png',(650,200),(470,490),screen)

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
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if imgrect2.collidepoint(mouse_pos):
                    Scene1(3)
                elif imgrect3.collidepoint(mouse_pos):
                    print("Load Game")
                    #load something
                elif imgrect4.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit
        pygame.display.update()
        clock.tick(fps)
    return False

def Scene1(line):
    global screen,size
    SNum = 1
    img1, imgrect1 = ButtonResize('bg.jpg',size,(0,0),screen)
    img2, imgrect2 = ButtonResize('otextbox.png',(1180,600),(200,400),screen)
    img3, imgrect3 = ButtonResize('next.png',(100,50),(1180,770),screen)
    if line == 3:
        label = myfont.render("Text goes here, Text goes here", 1, [250,250,250])
        screen.blit(label, (598, 722))
        pygame.display.update()
    elif line == 2:
        label = myfont.render("Text does not go here", 1, [250,250,250])
        screen.blit(label, (658, 722))
        pygame.display.update()
    elif line == 1:
        label = myfont.render("End of Scene", 1, [250,250,250])
        screen.blit(label, (708, 722))
        pygame.display.update()
    ButtonNext(imgrect3, SNum, line)
    
    
def Scene2(line):
    global screen,size
    SNum = 2
    img1, imgrect1 = ButtonResize('bg1.jpg',size,(0,0),screen)
    img2, imgrect2 = ButtonResize('otextbox.png',(1180,600),(200,400),screen)
    img3, imgrect3 = ButtonResize('next.png',(100,50),(1180,770),screen)
    if line == 3:
        label = myfont.render("Scene 2, Idk what happens", 1, [250,250,250])
        screen.blit(label, (598, 722))
        pygame.display.update()
    elif line == 2:
        label = myfont.render("Space holder lng to :D", 1, [250,250,250])
        screen.blit(label, (658, 722))
        pygame.display.update()
    elif line == 1:
        label = myfont.render("End of Scene", 1, [250,250,250])
        screen.blit(label, (708, 722))
        pygame.display.update()
    ButtonNext(imgrect3, SNum , line)
    
def main():
    global size,screen,clock,fps,myfont
    pygame.init()
    clock = pygame.time.Clock()
    fps = 60
    size = [1600, 900]
    screen = pygame.display.set_mode(size)
    img1, imgrect1 = ButtonResize('start.jpg',size,(0,0),screen)

    myfont = pygame.font.SysFont("Arial", 35)
    label = myfont.render("Click anywhere to start", 1, [0,0,0])
    screen.blit(label, (598, 722))
    label = myfont.render("Click anywhere to start", 1, [250,250,250])
    screen.blit(label, (600, 720))
    pygame.display.update()

    while True:        
        for event in pygame.event.get():            
            if event.type == pygame.QUIT:
                return False
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
