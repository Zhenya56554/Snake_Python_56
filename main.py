from classes import *
import pygame
import pygame_menu
import random

pygame.init()

dis=pygame.display.set_mode((500,400))
pygame.display.update()

pygame.display.set_caption('Snake Game')
 
game_over=False
 
while not game_over:
   for event in pygame.event.get():
        if event.type==pygame.QUIT:
           game_over = True
 
pygame.quit()