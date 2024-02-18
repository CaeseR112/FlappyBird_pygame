import pygame
from sys import exit

#pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('No Internet') 
clock = pygame.time.Clock()  #Setting the celing and the floor frame rates

################### Font declaration ##############################

test_font = pygame.font.Font( None, 50)



test_surface = pygame.Surface((100,200))
test_surface.fill('Red')

####################### Image Declaration ##########################

Sky_Image = pygame.image.load('Graphics/Backgrounds/Sky.png')
Floor_Image = pygame.image.load('Graphics/Backgrounds/ground.png')

###################### Text surfaces ################################

text_surface = test_font.render('Lolla', True ,'White')

    

#Quitting pygame window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            exit()

    screen.blit(Sky_Image,(0,0))
    screen.blit(Floor_Image,(0,300))
    screen.blit(test_surface,(300,50))

    pygame.display.update()
    clock.tick(60)

