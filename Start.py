import pygame
import sys

def ScreenSize(screen,size):
    pygame.display.set_mode(size)

def ResizeBlit(screen,img,size,x,y):
    img = pygame.transform.scale(img, size)
    screen.blit(img, pygame.rect.Rect(x, y, 0, 0))
    return img

def main():
    screen = pygame.display.set_mode((800, 600))
    img1 = pygame.image.load('bg.png')
    img2 = pygame.image.load('textbox.png').convert_alpha()
    img3 = pygame.image.load('next.png').convert_alpha()

    pygame.init()
    clock = pygame.time.Clock()
    fps = 60
    size = [1200, 720]
    fullsize = [1900, 1040]
    bg = [255, 255, 255]
    
    
    screen = pygame.display.set_mode(size)
    screen.fill(bg)

    pygame.display.flip()

    img1 = ResizeBlit(screen,img1,size,0,0)
    img2 = ResizeBlit(screen,img2,(980,400),100,400)

    img3 = ResizeBlit(screen,img3,(60,30),940,620)    

    #bigbutton = pygame.Rect(200, 500, 150, 150)  # creates a rect object
    # The rect method is similar to a list but with a few added perks
    # for example if you want the position of the button you can simpy type
    # button.x or button.y or if you want size you can type button.width or
    # height. you can also get the top, left, right and bottom of an object
    # with button.right, left, top, and bottom
    #smallbutton = pygame.Rect(400, 500, 150, 150)
    
    while True:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position

                # checks if mouse position is over the button
                print(img3.get_rect())

                if img3.get_rect().collidepoint(mouse_pos):
                        # prints current location of mouse
                    print('next')

        #pygame.draw.rect(screen, [0, 0, 0] , bigbutton)  # draw button
        #pygame.draw.rect(screen, [0, 0, 5], smallbutton)  # draw button

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    sys.exit


if __name__ == '__main__':
    main()
