import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('FlappyBird') 



#Quitting pygame window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

