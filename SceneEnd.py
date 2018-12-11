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
                    if SceneNum ==0:
                        Start()
                    SceneNo(SceneNum, LineNum)
                elif MenuButton.collidepoint(mouse_pos):
                    Menu()                
        pygame.display.update()
        clock.tick(fps)

def Menu():
    global screen,size, SceneNum, LineNum, saves, inventory, key
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
                    file.write(','+key)
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
                            num, Inventory, key = file.read().split(',')
                            SceneNum, LineNum =num.split(' ')
                            inventory = Inventory.split(' ')
                            file.close()
                            print(inventory)
                            
                            SceneNo(int(SceneNum), int(LineNum)+1) 
                elif imgrect4.collidepoint(mouse_pos):
                    Store()
                    Menu()
                    
                elif imgrect5.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit
        pygame.display.update()
        clock.tick(fps)
    return False

def Store():
    global items,inventory, key
    print(inventory)    
    pygame.mixer.music.load('../Music/M2.mp3')
    pygame.mixer.music.play(-1)
    img0, imgrect0 = ButtonResize('../Img/Vill.jpg',(0,0),(0,0),screen)
    imgrect2,imgrect3,imgrect4,imgrect5,imgrect6,imgrect7,imgrect8 = imgrect0,imgrect0,imgrect0,imgrect0,imgrect0,imgrect0,imgrect0
    img0, imgrect0 = ButtonResize('../Img/Vill.jpg',size,(0,0),screen)
    img0, imgrect0 = ButtonResize('../Img/opbg.png',size,(0,0),screen)
    img1, imgrect1 = ButtonResize('../Img/Inv.png',(1280,300),(150,600),screen)
    Name("Inventory", 120)
    myfont = pygame.font.SysFont("Arial", 35)
    if (inventory.count('1') == 0):
        img2, imgrect2 = ButtonResize('../Img/Chest.png',(300,250),(200,80),screen)
    else:
        label = myfont.render("HAT", 1, [200,200,200])
        screen.blit(label, (250, 720))
    if (inventory.count('2') == 0):
        img3, imgrect3 = ButtonResize('../Img/Chest.png',(300,250),(200,300),screen)
    else:
        label = myfont.render("          COAT", 1, [200,200,200])
        screen.blit(label, (250, 720))
    if (inventory.count('3') == 0):
        img4, imgrect4 = ButtonResize('../Img/Chest.png',(300,250),(600,20),screen)
    else:
        label = myfont.render("                       BREAD", 1, [200,200,200])
        screen.blit(label, (250, 720))
    if (inventory.count('4') == 0):
        img5, imgrect5 = ButtonResize('../Img/Chest.png',(300,250),(600,220),screen)
    else:
        label = myfont.render("                                     SLEEPING PILLS", 1, [200,200,200])
        screen.blit(label, (250, 720))
    if (inventory.count('5') == 0):
        img6, imgrect6 = ButtonResize('../Img/Chest.png',(300,250),(600,420),screen)
    else:
        label = myfont.render("BOOTS", 1, [200,200,200])
        screen.blit(label, (250, 780))
    if (inventory.count('6') == 0):
        img7, imgrect7 = ButtonResize('../Img/Chest.png',(300,250),(1000,80),screen)
    else:
        label = myfont.render("               SILVER BLADE", 1, [200,200,200])
        screen.blit(label, (250, 780))
    if (inventory.count('7') == 0):
        img8, imgrect8 = ButtonResize('../Img/Chest.png',(300,250),(1000,300),screen)
    else:
        label = myfont.render("                                        SUPPRESSANT PILLS", 1, [200,200,200])
        screen.blit(label, (250, 780))
    if key == 'a':
        img, imgrect = ButtonResize('../Img/Key.png',(200,150),(1000,700),screen)
    if key == 'a' or key == 'b' :
        img, imgrect = ButtonResize('../Img/Key.png',(200,150),(1100,700),screen)
    if key == 'a' or key == 'b' or key == 'c:':
        img, imgrect = ButtonResize('../Img/Key.png',(200,150),(1200,700),screen)
    Y = True
    if key == 'd':
        img0, imgrect0 = ButtonResize('../Img/opbg.png',(1600,600),(0,0),screen)
        img0, imgrect0 = ButtonResize('../Img/opbg.png',(1600,600),(0,0),screen)
        myfont = pygame.font.SysFont("Arial", 60)
        label = myfont.render("YOU HAVE NO MORE KEYS", 1, [200,200,200])
        screen.blit(label, (440, 250))
    img1, imgrect1 = ButtonResize('../Img/op1.png',(150,80),(1430,20),screen)
    myfont = pygame.font.SysFont("Arial", 35)
    label = myfont.render("Back", 1, [250,250,250])
    screen.blit(label, (1465, 40))
    if SceneNum == 3 and LineNum ==8:
        img0, imgrect0 = ButtonResize('../Img/opbg.png',size,(0,0),screen)
        img0, imgrect0 = ButtonResize('../Img/opbg.png',size,(0,0),screen)
        myfont = pygame.font.SysFont("Arial", 25)
        label = myfont.render("Welcome! This is are your treasure boxes which may be accessed through the Menu button.", 1, [200,200,200])
        screen.blit(label, (300, 200))
        label = myfont.render("Each contains an item that may come in handy any time during your adventure. Every key ", 1, [200,200,200])
        screen.blit(label, (300, 240))
        label = myfont.render("you have corresponds to a treasure box. You may use your keys to unlock the following items:", 1, [200,200,200])
        screen.blit(label, (300, 280))
        label = myfont.render("HAT, COAT, BREAD, SUPPRESSANT PILLS", 1, [200,200,200])
        screen.blit(label, (550, 330))
        label = myfont.render("BOOTS, SILVER BLADE, SLEEPING PILLS", 1, [200,200,200])
        screen.blit(label, (550, 370))
        label = myfont.render(" Please take note that you can only use a key once. This means that each key you have", 1, [200,200,200])
        screen.blit(label, (330, 440))
        label = myfont.render(" can only afford you an item you need. Use them wisely!", 1, [200,200,200])
        screen.blit(label, (480, 480))
    else:
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
                        if SceneNum == 3 and LineNum ==8:
                            SceneNo(int(SceneNum), int(LineNum)+1)    
                        else:
                            Menu()
                    elif imgrect2.collidepoint(mouse_pos):
                        x =1
                        KeyCount()
                        Y = False
                    elif imgrect3.collidepoint(mouse_pos):
                        x =2
                        KeyCount()
                        Y = False
                    elif imgrect4.collidepoint(mouse_pos):
                        x =3
                        KeyCount()
                        Y = False
                    elif imgrect5.collidepoint(mouse_pos):
                        x =4
                        KeyCount()
                        Y = False
                    elif imgrect6.collidepoint(mouse_pos):
                        x =5
                        KeyCount()
                        Y = False
                    elif imgrect7.collidepoint(mouse_pos):
                        x =6
                        KeyCount()
                        Y = False
                    elif imgrect8.collidepoint(mouse_pos):
                        x =7
                        KeyCount()
                        Y = False
                    else:
                        Y = True
            pygame.display.update()
            clock.tick(fps)
        inventory.append(str(x))
        img0, imgrect0 = ButtonResize('../Img/start.png',size,(0,0),screen)

def KeyCount():
    global key
    if key == 'a':
        key = 'b'
    elif key == 'b':
        key = 'c'
    elif key == 'c':
        key = 'd'
        
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
        elif num ==3:
                Scene3()
        elif num ==4:
                Scene4()
        elif num ==5:
                Scene5()
        elif num ==6:
                Scene6()
    else:
        if num == 1:
            LineNum = 10
            Scene2()
        elif num ==2:
            LineNum = 9
            Scene3()
        elif num ==3:
            LineNum = 8
            Scene4()
        elif num ==4:
            LineNum = 6
            Scene5()
        elif num ==5:
            LineNum = 10
            Scene6()
                
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
    '''Start Menu, has 3 buttons allowing to start a new game, load one or quit'''
    global screen,size, LineNum, inventory, key
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
                            num, Inventory, key = file.read().split(',')
                            SceneNum, LineNum =num.split(' ')
                            inventory = Inventory.split(' ')
                            file.close()
                            SceneNo(int(SceneNum), int(LineNum)+1)
                elif imgrect4.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit
        pygame.display.update()
        clock.tick(fps)
    return False

def Line1(text):
    '''Writes the upper dialogue'''
    myfont = pygame.font.SysFont("Arial", 25)
    label = myfont.render(text, 1, [250,250,250])
    screen.blit(label, (300, 720))
    
def Line2(text):
    myfont = pygame.font.SysFont("Arial", 25)
    label = myfont.render(text, 1, [250,250,250])
    screen.blit(label, (300, 750))        
    
def Scene1():
    global screen,size, SceneNum, LineNum,inventory
    SceneNum = 1
    myfont = pygame.font.SysFont("Arial", 25)
    if LineNum > 13:
        pygame.mixer.music.load('../Music/Eerie.mp3')
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
        Line1(" And the means they were willing to take were unimaginable. For so long they had")
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
        Line1("The agony and the terror these vampires brought to people was unconquerable.")
        Line2("The battle between the two forces lasted for decades")
    elif LineNum == 9:
        Line1("Until the people finally learned to match their skills and invent different ")
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

def Sc2_Sil(myfont):
        img1, imgrect1 = ButtonResize('../Char/Malc.png',(600,850),(100,140),screen)
        img1, imgrect1 = ButtonResize('../Char/Silv.png',(430,850),(1000,50),screen)
        img2, imgrect2 = ButtonResize('../Img/otextbox.png',(1180,600),(200,400),screen)    
        Name("Silver",10)
def Sc2_Mal(myfont):
        img1, imgrect1 = ButtonResize('../Char/Malc.png',(600,850),(100,100),screen)
        img1, imgrect1 = ButtonResize('../Char/Silv.png',(430,850),(1000,90),screen)
        img2, imgrect2 = ButtonResize('../Img/otextbox.png',(1180,600),(200,400),screen)    
        Name("Malcolm",0)
    
def Scene2():
    global screen,size, SceneNum, LineNum,inventory
    SceneNum = 2
    myfont = pygame.font.SysFont("Arial", 25)
    pygame.mixer.music.load('../Music/Chill.mp3')
    pygame.mixer.music.play(-1)
    img1, imgrect1 = ButtonResize('../Img/Work.jpg',size,(0,0),screen)

    if LineNum == 10:
        img1, imgrect1 = ButtonResize('../Char/Silv.png',(430,850),(1000,50),screen)
        img2, imgrect2 = ButtonResize('../Img/otextbox.png',(1180,600),(200,400),screen)
        Name("Silver",10)
        Line1("What a load of bollocks! You’ve probably been drinking too much these days, eh?")
        
    elif LineNum == 9:
        Sc2_Mal(myfont)
        Line1("Oh, they are real. You just don’t see them these days. As I said, vam-")
        
    elif LineNum == 8:
        Sc2_Sil(myfont)
        Line1("Those bastards are on the verge of extinction. I listened. ")
        Line2("They might not be even true inthe first place.")
        
    elif LineNum == 7:
        Sc2_Mal(myfont)
        Line1("You heard me. There’s a difference.")
        
    elif LineNum == 6:
        Sc2_Sil(myfont)
        Line1("Fine, whatever you say.")

    elif LineNum == 5:
        Sc2_Mal(myfont)
        Line1("By the way, don’t you have work to do?")
    elif LineNum == 4:
        Sc2_Sil(myfont)
        Line1("Oh, right.")
        Line2("Remember what I said. They’re not real.")
    elif LineNum == 3:
        Sc2_Mal(myfont)
        Line1("Remember what “I” said. You’ll see I’m telling the truth.")
    else:
        img1, imgrect1 = ButtonResize('../Char/Malc.png',(600,850),(100,100),screen)
        img2, imgrect2 = ButtonResize('../Img/otextbox.png',(1180,600),(200,400),screen)    
        Name("Macolm",0)
        Line1(" *Silver goes back to his work.* ")
        Line2("Hey, you forgot your pet! Which one of those is yours again? ")
        if LineNum == 1:
            pygame.mixer.music.load('../Music/HB.mp3')
            pygame.mixer.music.play(-1)
            img0, imgrect0 = ButtonResize('../Img/opbg.png',size,(0,0),screen)
            img1, imgrect1 = ButtonResize('../Char/Squirtle.png',(420,400),(600,70),screen)
            img2, imgrect2 = ButtonResize('../Char/Charmander.png',(500,500),(1070,30),screen)
            img3, imgrect3 = ButtonResize('../Char/Bulb.png',(360,300),(910,400),screen)
            while True:
                for event in pygame.event.get():            
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = event.pos
                        Y = False
                        if imgrect1.collidepoint(mouse_pos) or imgrect2.collidepoint(mouse_pos) or imgrect3.collidepoint(mouse_pos):
                            SceneNo(SceneNum,LineNum)
                pygame.display.update()
                clock.tick(fps)
    pygame.display.update()
    img3, imgrect3 = ButtonResize('../Img/next.png',(100,50),(1180,770),screen)
    img4, imgrect4 = ButtonResize('../Img/op1.png',(150,80),(1430,20),screen)
    myfont = pygame.font.SysFont("Arial", 35)
    label = myfont.render("Menu", 1, [250,250,250])
    screen.blit(label, (1463, 40))
    ButtonNext(imgrect3,imgrect4)


def Scene3():
    global screen,size, SceneNum, LineNum,inventory
    SceneNum = 3
    myfont = pygame.font.SysFont("Arial", 25)
    pygame.mixer.music.load('../Music/Chill.mp3')
    pygame.mixer.music.play(-1)
    img1, imgrect1 = ButtonResize('../Img/Work.jpg',size,(0,0),screen)
    if LineNum < 8:
        img1, imgrect1 = ButtonResize('../Img/Out.jpg',size,(0,0),screen)
        
    if LineNum == 9:
        Sc2_Mal(myfont)
        Line1("Well, have you fed it yet?")
    elif LineNum == 8:
        Store()
    elif LineNum == 7:
        img2, imgrect2 = ButtonResize('../Img/otextbox.png',(1180,600),(200,400),screen)
        Line1("     *Both of the characters go home together with their co workers*")
    elif LineNum == 6:
        Sc2_Sil(myfont)
        Line1("Oh no, the night is dark. We better hurry home before the vampires catch us!")
        Line2("     *laughs with workmates*")
    elif LineNum == 5:
        Sc2_Mal(myfont)
        Line1("You mock them now but not even the church can save your arse when they come" )
        Line2("knocking on your door at midnight.")
    elif LineNum == 4:
        Sc2_Sil(myfont)
        Line1("Oh, lighten up, Malcolm! I told you they’re not real. That’s just one of the stories your grand" )
        Line2("parents tell you to get you to sleep. I couldn’t believe you’d actually take them seriously.")
    elif LineNum == 3:
        Sc2_Sil(myfont)
        Line1("Oh, lighten up, Malcolm! I told you they’re not real. That’s just one of the stories your grand" )
        Line2("parents tell you to get you to sleep. I couldn’t believe you’d actually take them seriously.")
    elif LineNum == 2:
        Sc2_Mal(myfont)
        Line1("*acts weirdly*")
        Line2("I have to go.")
    elif LineNum == 1:
        img1, imgrect1 = ButtonResize('../Char/Silv.png',(430,850),(1000,50),screen)
        img2, imgrect2 = ButtonResize('../Img/otextbox.png',(1180,600),(200,400),screen)
        Name("Silver",10)
        Line1("Malcolm must be seeing things. *chuckles*")
        Line2("Damn, I wanna have what he’s having. What could it be?")
        
    pygame.display.update()
    img3, imgrect3 = ButtonResize('../Img/next.png',(100,50),(1180,770),screen)
    img4, imgrect4 = ButtonResize('../Img/op1.png',(150,80),(1430,20),screen)
    myfont = pygame.font.SysFont("Arial", 35)
    label = myfont.render("Menu", 1, [250,250,250])
    screen.blit(label, (1463, 40))
    ButtonNext(imgrect3,imgrect4)

def Scene4():
    global screen,size, SceneNum, LineNum,inventory
    SceneNum = 4
    myfont = pygame.font.SysFont("Arial", 25)
    pygame.mixer.music.load('../Music/Bed.mp3')
    pygame.mixer.music.play(-1)
    img1, imgrect1 = ButtonResize('../Img/BedN.png',size,(0,0),screen)
    if LineNum < 6:
        img1, imgrect1 = ButtonResize('../Img/Work.jpg',size,(0,0),screen)
        
    if LineNum == 8:
        img2, imgrect2 = ButtonResize('../Img/otextbox.png',(1180,600),(200,400),screen)
        Line1("*Silver arrives home safely and goes to sleep*")
    elif LineNum == 7:
        img1, imgrect1 = ButtonResize('../Char/Silv.png',(430,850),(1000,50),screen)
        img2, imgrect2 = ButtonResize('../Img/otextbox.png',(1180,600),(200,400),screen)
        Name("Silver",10)
        Line1("*Silver was awaken by weird noises in his backyard*")
        Line2("What was that?")
    elif LineNum == 6:
        img1, imgrect1 = ButtonResize('../Char/Silv.png',(430,850),(1000,50),screen)
        img2, imgrect2 = ButtonResize('../Img/otextbox.png',(1180,600),(200,400),screen)
        Name("Silver",10)
        Line1("*Yawns*")
        Line2("Oh well, I better go back to sleep, it’s a busy day tomorrow.")
    elif LineNum == 5:
        img2, imgrect2 = ButtonResize('../Img/otextbox.png',(1180,600),(200,400),screen)
        Line1("*The next day, Silver goes back to work*")
        Line2("*Silver Looks for Malcolm*")
    elif LineNum == 4:
        img1, imgrect1 = ButtonResize('../Char/Silv.png',(430,850),(1000,50),screen)
        img2, imgrect2 = ButtonResize('../Img/otextbox.png',(1180,600),(200,400),screen)
        Name("Silver",10)
        Line1("Hey, have you seen Malcolm?")
    elif LineNum == 3:
        img2, imgrect2 = ButtonResize('../Img/otextbox.png',(1180,600),(200,400),screen)
        Name("Workmate",0)
        Line1("Nope. He's probably out, drinking again.")
    else:
        img1, imgrect1 = ButtonResize('../Char/Silv.png',(430,850),(1000,50),screen)
        img2, imgrect2 = ButtonResize('../Img/otextbox.png',(1180,600),(200,400),screen)
        Name("Silver",10)
        Line1("He better not be drinking or I may end up hearing another one of his")
        Line2("ghost stories again. *Silver finds Malcolm sitting still in the corner*")
        if LineNum == 1:
            pygame.mixer.music.load('../Music/HB.mp3')
            pygame.mixer.music.play(-1)
            img0, imgrect0 = ButtonResize('../Img/opbg.png',size,(0,0),screen)
            img2, imgrect2 = ButtonResize('../Img/op1.png',(650,200),(470,200),screen)
            img3, imgrect3 = ButtonResize('../Img/op2.png',(650,200),(470,340),screen)

            myfont = pygame.font.SysFont("Arial", 55)
            label = myfont.render("Approach Malcolm", 1, [200,200,200])
            screen.blit(label, (565, 260))   
            label = myfont.render("Leave him alone", 1, [200,200,200])
            screen.blit(label, (590, 400))   
            
            pygame.display.update()

            while True:
                for event in pygame.event.get():            
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = event.pos
                        Y = False
                        if imgrect2.collidepoint(mouse_pos):
                            SceneNum = 5
                            SceneNo(SceneNum,LineNum)
                        elif imgrect3.collidepoint(mouse_pos):
                            SceneNo(SceneNum,LineNum)
                pygame.display.update()
                clock.tick(fps)
        
    pygame.display.update()
    img3, imgrect3 = ButtonResize('../Img/next.png',(100,50),(1180,770),screen)
    img4, imgrect4 = ButtonResize('../Img/op1.png',(150,80),(1430,20),screen)
    myfont = pygame.font.SysFont("Arial", 35)
    label = myfont.render("Menu", 1, [250,250,250])
    screen.blit(label, (1463, 40))
    ButtonNext(imgrect3,imgrect4)

def Scene5():
    global screen,size, SceneNum, LineNum,inventory
    SceneNum = 5
    myfont = pygame.font.SysFont("Arial", 25)
    pygame.mixer.music.load('../Music/M2.mp3')
    pygame.mixer.music.play(-1)
    img1, imgrect1 = ButtonResize('../Img/Work.jpg',size,(0,0),screen)

    img1, imgrect1 = ButtonResize('../Char/Silv.png',(430,850),(1000,50),screen)
    img2, imgrect2 = ButtonResize('../Img/otextbox.png',(1180,600),(200,400),screen)
    Name("Silver",10)
    if LineNum == 6:
        Line1(" *Silver notices his pet is missing* ")
    elif LineNum == 5:
        Line1("Here boy, I brought you your favorite treats!")
    elif LineNum == 4:
        Line1(" *wonders* ")
    elif LineNum == 3:
        Line1("That's strange, These are his favorite")
    elif LineNum == 2:
        Line1(" *Silver continues to look for his pet* ")
    elif LineNum == 1:
        Line1(" *He finds himself back in the corner where Malcolm was* ")
    
    pygame.display.update()
    img3, imgrect3 = ButtonResize('../Img/next.png',(100,50),(1180,770),screen)
    img4, imgrect4 = ButtonResize('../Img/op1.png',(150,80),(1430,20),screen)
    myfont = pygame.font.SysFont("Arial", 35)
    label = myfont.render("Menu", 1, [250,250,250])
    screen.blit(label, (1463, 40))
    ButtonNext(imgrect3,imgrect4)

def Scene6():
    global screen,size, SceneNum, LineNum,inventory
    SceneNum = 6
    myfont = pygame.font.SysFont("Arial", 25)
    if LineNum > 7:
        pygame.mixer.music.load('../Music/M2.mp3')
        pygame.mixer.music.play(-1)
    else:
        pygame.mixer.music.load('../Music/M3.mp3')
        pygame.mixer.music.play(-1)

    img1, imgrect1 = ButtonResize('../Img/Work.jpg',size,(0,0),screen)
    if LineNum < 3:
        img1, imgrect1 = ButtonResize('../Img/Out.jpg',size,(0,0),screen)
    
    if LineNum == 10:
        img1, imgrect1 = ButtonResize('../Char/Malc.png',(600,850),(100,100),screen)
        img2, imgrect2 = ButtonResize('../Img/otextbox.png',(1180,600),(200,400),screen)    
        Line1(" *Malcolm’s bloodlust intensifies* ")
    elif LineNum == 9:
        Sc2_Sil(myfont)
        Line1("Ah, there you are. I was looking every... where for…")
        Line2("*Silver noticed Malcom making strange “eating” noises* ")
    elif LineNum == 8:
        Sc2_Sil(myfont)
        Line1("Uh, Malcolm, you okay pal?")
        Line2("Malcolm? ")
        
    elif LineNum == 7:
        img2, imgrect2 = ButtonResize('../Img/otextbox.png',(1180,600),(200,400),screen)
        Line1("*Malcom attempts to bite Silver*")
    elif LineNum == 6:
        Sc2_Sil(myfont)
        Line1("WHAT THE F***??? Malcolm, GET THE F*** OFF ME!!!")
        Line2(" *Silver Fights back* ")
    elif LineNum == 5:
        img1, imgrect1 = ButtonResize('../Char/Silv.png',(430,850),(1000,50),screen)
        img2, imgrect2 = ButtonResize('../Img/otextbox.png',(1180,600),(200,400),screen)
        Name("Silver",10)
        Line1("*Silver gets bitten*")
        Line2("AAAAAHHHHH!!!! WHAT THE H***, MALCOLM!!! WHY THE H*** DID YOU BITE ME??? ")
    elif LineNum == 4:
        img1, imgrect1 = ButtonResize('../Char/Malc.png',(600,850),(100,100),screen)
        img2, imgrect2 = ButtonResize('../Img/otextbox.png',(1180,600),(200,400),screen)    
        Line1(" *Malcolm’s bloodlust intensifies* ")
    elif LineNum == 3:
        img1, imgrect1 = ButtonResize('../Char/Silv.png',(430,850),(1000,50),screen)
        img2, imgrect2 = ButtonResize('../Img/otextbox.png',(1180,600),(200,400),screen)
        Name("Silver",10)
        Line1("S***!!! HELP!!! HELP ME!!! S***!!!")
    elif LineNum == 2:
        img2, imgrect2 = ButtonResize('../Img/otextbox.png',(1180,600),(200,400),screen)
        Line1("*Silver excapes with a bite*")
    elif LineNum == 1:
        img0, imgrect0 = ButtonResize('../Img/opbg.png',size,(0,0),screen)
        img2, imgrect2 = ButtonResize('../Img/otextbox.png',(1180,600),(200,400),screen)
        Line1("*Silver faints*")
    pygame.display.update()
    img3, imgrect3 = ButtonResize('../Img/next.png',(100,50),(1180,770),screen)
    img4, imgrect4 = ButtonResize('../Img/op1.png',(150,80),(1430,20),screen)
    myfont = pygame.font.SysFont("Arial", 35)
    label = myfont.render("Menu", 1, [250,250,250])
    screen.blit(label, (1463, 40))
    ButtonNext(imgrect3,imgrect4)

def Scene7():
    global screen,size, SceneNum, LineNum,inventory
    SceneNum = 7
    myfont = pygame.font.SysFont("Arial", 25)
    pygame.mixer.music.load('../Music/M2.mp3')
    pygame.mixer.music.play(-1)
    
    img1, imgrect1 = ButtonResize('../Img/Bed.png',size,(0,0),screen)
    
    if LineNum == 3:
        img1, imgrect1 = ButtonResize('../Char/Silv.png',(430,850),(1000,50),screen)
        img2, imgrect2 = ButtonResize('../Img/otextbox.png',(1180,600),(200,400),screen)
        Name("Silver",10)
        Line1("*Silver woke up with a different feeling. He tried to recall what had happened. *")
        Line2("*He remembered what Malcolm did to him.*")
    else:
        img2, imgrect2 = ButtonResize('../Img/otextbox.png',(1180,600),(200,400),screen)
        Line1("*Now that he found out the truth about Malcolm, *")
        Line2("*he plans to go to the priests and alert them about the incident*")
        if LineNum == 1:
            pygame.mixer.music.load('../Music/HB.mp3')
            pygame.mixer.music.play(-1)
            img0, imgrect0 = ButtonResize('../Img/opbg.png',size,(0,0),screen)
            img2, imgrect2 = ButtonResize('../Img/op1.png',(650,200),(470,200),screen)
            img3, imgrect3 = ButtonResize('../Img/op2.png',(650,200),(470,340),screen)

            myfont = pygame.font.SysFont("Arial", 55)
            label = myfont.render("Go Outside", 1, [200,200,200])
            screen.blit(label, (605, 260))   
            label = myfont.render("Stay Inside", 1, [200,200,200])
            screen.blit(label, (620, 400))               
            pygame.display.update()
            while True:
                for event in pygame.event.get():            
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = event.pos
                        Y = False
                        if imgrect2.collidepoint(mouse_pos):
                            SceneNo(SceneNum,LineNum)
                        elif imgrect3.collidepoint(mouse_pos):
                            SceneNum = 8
                            SceneNo(SceneNum,LineNum)
                pygame.display.update()
                clock.tick(fps)


def SceneEnd():
    '''credit scene, has 2 buttons play again and the menu button which redirect you to the menu '''
    global SceneNum
    SceneNum = 0
    img0, imgrect0 = ButtonResize('../Img/start.png',size,(0,0),screen)
    img0, imgrect0 = ButtonResize('../Img/credits.png',size,(0,0),screen)
    myfont = pygame.font.SysFont("Arial", 60)
    pygame.display.update()
    img3, imgrect3 = ButtonResize('../Img/op1.png',(200,80),(1180,20),screen)
    myfont = pygame.font.SysFont("Arial", 35)
    label = myfont.render("Play again", 1, [250,250,250])
    screen.blit(label, (1200, 40))
    img4, imgrect4 = ButtonResize('../Img/op1.png',(150,80),(1430,20),screen)
    label = myfont.render("Menu", 1, [250,250,250])
    screen.blit(label, (1463, 40))
    ButtonNext(imgrect3,imgrect4)

#if (inventory.count('1') == 0) or (inventory.count('2') == 0):

def main():
    global size,screen,clock,fps,myfont,saves,inventory,key
    pygame.init()
    clock = pygame.time.Clock()
    fps = 60
    size = [1600, 900]
    screen = pygame.display.set_mode(size)
    img1, imgrect1 = ButtonResize('../Img/start.png',size,(0,0),screen)
    inventory = ['0']
    key = 'a'
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
