import pygame
import sys

def ScreenSize(screen,size):
    pygame.display.set_mode(size)

def ButtonResize(pic, size, cord, screen):
    img = pygame.image.load(pic).convert_alpha()
    img = pygame.transform.scale(img, size)
    imgrect = img.get_rect()
    imgrect.topleft = cord
    screen.blit(img, imgrect)
    return img, imgrect

def Scene1(screen,size):
    img1, imgrect1 = ButtonResize('bg.jpg',size,(0,0),screen)
    img2, imgrect2 = ButtonResize('otextbox.png',(1180,600),(200,400),screen)
    img3, imgrect3 = ButtonResize('next.png',(100,50),(1180,770),screen)
    return img3, imgrect3

def Scene2(screen,size):
    img1, imgrect1 = ButtonResize('bg1.jpg',size,(0,0),screen)
    img2, imgrect2 = ButtonResize('otextbox.png',(1180,600),(200,400),screen)
    img3, imgrect3 = ButtonResize('next.png',(100,50),(1180,770),screen)
    return img3, imgrect3

def main():
    pygame.init()
    clock = pygame.time.Clock()
    fps = 60
    size = [1600, 900]
    
    screen = pygame.display.set_mode(size)
    screen.fill([55,55,50])
    
    img1, imgrect1 = ButtonResize('bg.png',size,(0,0),screen)
    
    pygame.display.flip()
    img3, imgrect3 = Scene1(screen,size)
    
    while True:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position

                # checks if mouse position is over the button
                if imgrect3.collidepoint(mouse_pos):
                        # prints current location of mouse
                    Scene2(screen,size)
                    print('next')

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

