import pygame
from sys import exit

#pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('No Internet') 
clock = pygame.time.Clock()  #Setting the celing and the floor rates

#Setting the window icon
img = pygame.image.load('icon.png')
pygame.display.set_icon(img)

test_surface = pygame.Surface((1250,700))  #Creation of a surface - wont display yet
test_surface.fill('Red')

#Quitting pygame window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(test_surface,(100,100))
    pygame.display.update()
    clock.tick(60)

