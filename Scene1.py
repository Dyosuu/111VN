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

                    x = Saved(2)
                    
                    DateTime =  str( datetime.datetime.now() )
                    DateTime = DateTime[:-7]
                    saves[x] = DateTime

                    x = "../Saves/" + str(x)
                    file = open( x ,"w") 
                    file.write(str(SceneNum)+" "+str(LineNum)+',')
                    for item in inventory:
                        file.write(str(item)+' ')
                    file.close()
                    
                    files = open( "../Saves/Name.txt" ,"w")
                    for word in saves:
                        files.write(word+',')
                    files.close()      

                    Menu()
                                            
                elif imgrect3.collidepoint(mouse_pos):
                    
                    while True:
                        x = Saved(2)
                        x = "../Saves/" + str(x)
                        if os.path.isfile(x):
                            file = open(x ,"r")
                            num, Inventory = file.read().split(',')
                            SceneNum, LineNum =num.split(' ')
                            inventory = Inventory.split(' ')
                            file.close()
                            SceneNo(int(SceneNum), int(LineNum)+1)                            

                elif imgrect4.collidepoint(mouse_pos):
                    Store()
                    
                elif imgrect5.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit
        pygame.display.update()
        clock.tick(fps)
    return False

def Store():
    global items
    img0, imgrect0 = ButtonResize('../Img/Vill.jpg',size,(0,0),screen)
    img0, imgrect0 = ButtonResize('../Img/opbg.png',size,(0,0),screen)
    img1, imgrect1 = ButtonResize('../Img/Inv.png',(1280,300),(150,600),screen)
    Name("Inventory", 120)
    img2, imgrect2 = ButtonResize('../Img/Chest.png',(300,250),(200,80),screen)
    img3, imgrect3 = ButtonResize('../Img/Chest.png',(300,250),(200,300),screen)
    img4, imgrect4 = ButtonResize('../Img/Chest.png',(300,250),(600,20),screen)
    img5, imgrect5 = ButtonResize('../Img/Chest.png',(300,250),(600,220),screen)
    img6, imgrect6 = ButtonResize('../Img/Chest.png',(300,250),(600,420),screen)
    img7, imgrect7 = ButtonResize('../Img/Chest.png',(300,250),(1000,80),screen)
    img8, imgrect8 = ButtonResize('../Img/Chest.png',(300,250),(1000,300),screen)

    while Y:
        for event in pygame.event.get():            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                Y = False
                if imgrect1.collidepoint(mouse_pos):
                    img0, imgrect0 = ButtonResize('../Img/start.png',size,(0,0),screen)
                    if menu == 1:
                        Start()
                    else:
                        Menu()
                elif imgrect2.collidepoint(mouse_pos):
                    x =1
                elif imgrect3.collidepoint(mouse_pos):
                    x =2
                elif imgrect4.collidepoint(mouse_pos):
                    x =3
                elif imgrect5.collidepoint(mouse_pos):
                    x =4
                elif imgrect6.collidepoint(mouse_pos):
                    x =5
                elif imgrect7.collidepoint(mouse_pos):
                    x =6
                elif imgrect8.collidepoint(mouse_pos):
                    x =7
                else:
                    Y = True
        pygame.display.update()
        clock.tick(fps)
    img0, imgrect0 = ButtonResize('../Img/start.png',size,(0,0),screen)
    
def Saved(menu):
    Y = True
    x = 0
    screen.fill([0,0,0])
    img0, imgrect0 = ButtonResize('../Img/start.png',size,(0,0),screen)
    img0, imgrect0 = ButtonResize('../Img/opbg.png',size,(0,0),screen)
    img1, imgrect1 = ButtonResize('../Img/op1.png',(150,80),(1430,20),screen)
    myfont = pygame.font.SysFont("Arial", 35)
    label = myfont.render("Back", 1, [250,250,250])
    screen.blit(label, (1465, 40))
    img2, imgrect2 = ButtonResize('../Img/op1.png',(500,200),(550,100),screen)
    label = myfont.render(saves[0], 1, [250,250,250])
    screen.blit(label, (630, 180))
    img3, imgrect3 = ButtonResize('../Img/op2.png',(500,200),(550,240),screen)
    label = myfont.render(saves[1], 1, [250,250,250])
    screen.blit(label, (630, 310))
    img4, imgrect4 = ButtonResize('../Img/op3.png',(500,200),(550,390),screen)
    label = myfont.render(saves[2], 1, [250,250,250])
    screen.blit(label, (630, 470))
    img5, imgrect5 = ButtonResize('../Img/op4.png',(500,200),(550,530),screen)
    label = myfont.render(saves[3], 1, [250,250,250])
    screen.blit(label, (630, 610))
    img6, imgrect6 = ButtonResize('../Img/op1.png',(500,200),(70,200),screen)
    img7, imgrect7 = ButtonResize('../Img/op2.png',(500,200),(70,340),screen)
    img8, imgrect8 = ButtonResize('../Img/op3.png',(500,200),(70,490),screen)

    label = myfont.render(saves[4], 1, [250,250,250])
    screen.blit(label, (150, 280))
    label = myfont.render(saves[5], 1, [250,250,250])
    screen.blit(label, (150, 420))
    label = myfont.render(saves[6], 1, [250,250,250])
    screen.blit(label, (150, 570))
    
    img9, imgrect9 = ButtonResize('../Img/op1.png',(500,200),(1070,200),screen)
    img10, imgrect10 = ButtonResize('../Img/op2.png',(500,200),(1070,340),screen)
    img11, imgrect11 = ButtonResize('../Img/op3.png',(500,200),(1070,490),screen)
    
    label = myfont.render(saves[7], 1, [250,250,250])
    screen.blit(label, (1150, 280))
    label = myfont.render(saves[8], 1, [250,250,250])
    screen.blit(label, (1150, 420))
    label = myfont.render(saves[9], 1, [250,250,250])
    screen.blit(label, (1150, 570))
    pygame.display.update()
    
    while Y:
        for event in pygame.event.get():            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                Y = False
                if imgrect1.collidepoint(mouse_pos):
                    img0, imgrect0 = ButtonResize('../Img/start.png',size,(0,0),screen)
                    if menu == 1:
                        Start()
                    else:
                        Menu()
                elif imgrect2.collidepoint(mouse_pos):
                    x =0
                elif imgrect3.collidepoint(mouse_pos):
                    x =1
                elif imgrect4.collidepoint(mouse_pos):
                    x =2
                elif imgrect5.collidepoint(mouse_pos):
                    x =3
                elif imgrect6.collidepoint(mouse_pos):
                    x =4
                elif imgrect7.collidepoint(mouse_pos):
                    x =5
                elif imgrect8.collidepoint(mouse_pos):
                    x =6
                elif imgrect9.collidepoint(mouse_pos):
                    x =7
                elif imgrect10.collidepoint(mouse_pos):
                    x =8
                elif imgrect11.collidepoint(mouse_pos):
                    x =9
                else:
                    Y = True
        pygame.display.update()
        clock.tick(fps)
    img0, imgrect0 = ButtonResize('../Img/start.png',size,(0,0),screen)
    return x
                            
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

def Name(text,x):
    myfont = pygame.font.SysFont("Arial", 35)
    label = myfont.render(text, 1, [200,200,200])
    screen.blit(label, (960+x, 652))
    
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
    screen.blit(label, (738, 542))   
    label = myfont.render("Quit", 1, [200,200,200])
    screen.blit(label, (740, 540))
    
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
                    LineNum = 17
                    Scene1()
                elif imgrect3.collidepoint(mouse_pos):
                    while True:
                        x = Saved(1)
                        x = "../Saves/" + str(x)
                        if os.path.isfile(x):
                            file = open(x ,"r")
                            SceneNum, LineNum =file.read().split(' ')
                            file.close()
                            SceneNo(int(SceneNum), int(LineNum)+1)

                elif imgrect4.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit
        pygame.display.update()
        clock.tick(fps)
    return False

def Line1(text):
    myfont = pygame.font.SysFont("Arial", 25)
    label = myfont.render(text, 1, [250,250,250])
    screen.blit(label, (300, 720))
    
def Line2(text):
    myfont = pygame.font.SysFont("Arial", 25)
    label = myfont.render(text, 1, [250,250,250])
    screen.blit(label, (300, 750))        
    
def Scene1():
    global screen,size, SceneNum, LineNum
    SceneNum = 1
    myfont = pygame.font.SysFont("Arial", 25)
    if LineNum > 13:
        pygame.mixer.music.load('../Music/M2.mp3')
        pygame.mixer.music.play(-1)
        img1, imgrect1 = ButtonResize('../Img/ChurchOut.jpg',size,(0,0),screen)
    elif LineNum > 5:
        pygame.mixer.music.load('../Music/M3.mp3')
        pygame.mixer.music.play(-1)
        img1, imgrect1 = ButtonResize('../Img/Kill.jpg',size,(0,0),screen)
    else:
        pygame.mixer.music.load('../Music/M2.mp3')
        pygame.mixer.music.play(-1)
        img1, imgrect1 = ButtonResize('../Img/Vill.jpg',size,(0,0),screen)
    
    img2, imgrect2 = ButtonResize('../Img/otextbox.png',(1180,600),(200,400),screen)
    Name("Malcolm",0)
    
    if LineNum == 17:
        Line1("Ever since the Middle ages, the church has established power to several kingdoms of")
        Line2("the world, wielding a formidable weapon many have bowed down to- religion.")
    elif LineNum == 16:
        Line1("The power it possessed was not archetypal and targeted the mind of the opponent")
        Line2("instead of the flesh, making them submit to blind obedience.")
    elif LineNum == 15:
        Line1("Many of us may agree that their influence has helped bring prosperity")
        Line2("to the kingdoms we have today. But their method was mostly ruthless")
    elif LineNum == 14:
        Line1(" and the means they were willing to take were unimaginable. For so long they had")
        Line2(" control over the kingdoms, until their strongest nemesis yet rose to power in Europe. ")
        
    elif LineNum == 13:
        Line1("They were the vampires. Direct descendants of Vlad III or who we know as The Impaler.")
        Line2("These vile creatures that roamed Europe were once knights.")
    elif LineNum == 12:
        Line1("They wiped out the Ottoman Empire during the 1400’s. They were far more vicious, more")
        Line2("dangerous and they threatened the lives of every mortal that walked on Earth.")        
    elif LineNum == 11:
        Line1("The church had the people, the living people. Sadly, they weren’t enough against the")
        Line2("spawns of hell themselves. Even with the villagers beside them,")
    elif LineNum == 10:
        Line1("the agony and the terror these vampires brought to people was unconquerable.")
        Line2("The battle between the two forces lasted for decades")
    elif LineNum == 9:
        Line1(" until the people finally learned to match their skills and invent different ")
        Line2("strategies that lead to their annihilation. ")
    elif LineNum == 8:
        Line1("These gave the church and the people the upper hand against these tyrants.")
        Line2("The streets were dominated by loathing and trepidation.")
    elif LineNum == 7:
        Line1("The vampires were hunted down and driven away from existence. Every man, woman")
        Line2(" and child trembled in fear as they witnessed the slaughter of their loved ones ")
    elif LineNum == 6:
        Line1("They fought for their lives in what our elders thought as the manifestation of")
        Line2("the Bible’s Revelation.")
    elif LineNum == 5:
        Line1("The vampires have been persecuted, ostracized, and massacred for")
        Line2("as long as anyone can remember.")
                
    elif LineNum == 4:
        Line1("The bloody war is the reason we don’t see vampires today. Once you understand ")
        Line2("how they feasted of human flesh, you’d be thankful to have lived in this generation.")
    elif LineNum == 3:
        Line1("But be wary, Silver. Legend has it, they still run rampant today, hunting and feeding;")
        Line2("taking children from their mothers; cutting throats; and drinking blood.")
    elif LineNum == 2:
        Line1("You can still hear queer noises at night.")
        Line2("The villagers mistake them for squirrels or rats searching for food.")
    elif LineNum == 1:
        Line1("But the elders would warn you that they’re vampires, preying on you as you sleep.")
        Line2("")
    pygame.display.update()
    img3, imgrect3 = ButtonResize('../Img/next.png',(100,50),(1180,770),screen)
    img4, imgrect4 = ButtonResize('../Img/op1.png',(150,80),(1430,20),screen)
    myfont = pygame.font.SysFont("Arial", 35)
    label = myfont.render("Menu", 1, [250,250,250])
    screen.blit(label, (1463, 40))
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
    global size,screen,clock,fps,myfont,saves,inventory
    pygame.init()
    clock = pygame.time.Clock()
    fps = 60
    size = [1600, 900]
    screen = pygame.display.set_mode(size)
    img1, imgrect1 = ButtonResize('../Img/start.png',size,(0,0),screen)
    inventory = [0]
    
    file = open('../Saves/Name.txt' ,"r") 
    saves =file.read().split(',')
    file.close()

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
