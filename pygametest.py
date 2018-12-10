import pygame
import sys
'''
def ScreenSize(screen,size,fullsize):
    x = input("Full or nah")
    if x == "full":
        pygame.display.set_mode(fullsize)
    else:
        pygame.display.set_mode(size)
'''

def ScreenSize(screen,size):
    pygame.display.set_mode(size)

def main():
    pygame.init()
    clock = pygame.time.Clock()
    fps = 60
    size = [1280, 720]
    fullsize = [1900, 1040]
    bg = [255, 255, 255]

    screen = pygame.display.set_mode(size)
    screen.fill(bg)

    bigbutton = pygame.Rect(200, 500, 150, 150)  # creates a rect object
    # The rect method is similar to a list but with a few added perks
    # for example if you want the position of the button you can simpy type
    # button.x or button.y or if you want size you can type button.width or
    # height. you can also get the top, left, right and bottom of an object
    # with button.right, left, top, and bottom
    smallbutton = pygame.Rect(400, 500, 150, 150)
    
    while True:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position

                # checks if mouse position is over the button

                if bigbutton.collidepoint(mouse_pos):
                        # prints current location of mouse
                    ScreenSize(screen,fullsize)
                elif smallbutton.collidepoint(mouse_pos):
                        # prints current location of mouse
                    ScreenSize(screen,size)



        pygame.draw.rect(screen, [255, 0, 0], bigbutton)  # draw button
        pygame.draw.rect(screen, [0, 0, 255], smallbutton)  # draw button

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    sys.exit


if __name__ == '__main__':
    main()
