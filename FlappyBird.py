import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True

#Quitting pygame window
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

screen.fill("white")
asurf = pygame.image.load(bg.jpg)