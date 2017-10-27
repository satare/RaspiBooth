import pygame, sys
import time
pygame.init()
screen = pygame.display.set_mode((1024,768))

image=pygame.image.load("01.jpg")

#show = 0
clock = pygame.time.Clock()
screen.blit(image, (0 , 0))
pygame.display.update()
clock.tick(30)
time.sleep(3)