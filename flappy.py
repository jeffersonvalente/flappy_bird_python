import pygame
from pygame.locals import *

#define tamanho da tela
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 800

#cria o passarinho
class Bird(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        #chama a imagem e converte os pixels transparentes (convert_alpha)
        self.image = pygame.image.load('F:/flappy_bird_python/sprites/bluebird-midflap.png').convert_alpha()
        self.rect = self.image.get_rect() #define a posição na tela
        print(self.rect) 
    
    def update(self):
        pass

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#adiciona o background
BACKGROUND = pygame.image.load('F:/flappy_bird_python/sprites/background-day.png')
BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))

#adiciona o grupo do passarinho
bird_group = pygame.sprite.Group()
bird = Bird()
bird_group.add(bird)

#cria laço principal do jogo
while True:
    
#testa os eventos do game    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            
#cria o backgound na tela.
    screen.blit(BACKGROUND, (0,0)) #os zeros indicam a posição no canto da tela
    
    bird_group.update() #muda opassarinho conforme o game
    
    #desenha os elementos do grupo bird
    bird_group.draw(screen)
    
    pygame.display.update()
