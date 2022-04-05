import pygame
from pygame.locals import *

#define tamanho da tela
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 800

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#cria laço principal do jogo

while True:
    
#testa os eventos do game    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    
    pygame.display.update()
