import pygame
from pygame.locals import *

#define tamanho da tela
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 800
SPEED = 10
GRAVITY = 1

#cria o passarinho
class Bird(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        #dicionario das imagens
        self.images = [pygame.image.load('F:/flappy_bird_python/sprites/bluebird-upflap.png',).convert_alpha(),
                       pygame.image.load('F:/flappy_bird_python/sprites/bluebird-midflap.png',).convert_alpha(),
                       pygame.image.load('F:/flappy_bird_python/sprites/bluebird-downflap.png').convert_alpha()]
        
        self.current_image = 0
        
        self.speed = SPEED
        
        #chama a imagem e converte os pixels transparentes (convert_alpha)
        self.image = pygame.image.load('F:/flappy_bird_python/sprites/bluebird-upflap.png').convert_alpha()
        self.rect = self.image.get_rect() #define a posição na tela
        self.rect[0] = SCREEN_WIDTH / 2
        self.rect[1] = SCREEN_HEIGHT / 2
        print(self.rect) 
    
    def update(self): #função para os estados da imagem
       self.current_image = (self.current_image + 1) % 3
       self.image = self.images[ self.current_image ]
       
       #UPDATE HEIGHT
       self.rect[1] += self.speed #passaro cai
       
       self.speed += GRAVITY
       
    def bump(self):
        self.speed = -SPEED #passaro sobe
        
        

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#adiciona o background
BACKGROUND = pygame.image.load('F:/flappy_bird_python/sprites/background-day.png')
BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))

#adiciona o grupo do passarinho
bird_group = pygame.sprite.Group()
bird = Bird()
bird_group.add(bird)

clock = pygame.time.Clock() #define o fps/velocidade do bate asa


#cria laço principal do jogo
while True:
    clock.tick(30)
#testa os eventos do game    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                bird.bump()
            
#cria o backgound na tela.
    screen.blit(BACKGROUND, (0,0)) #os zeros indicam a posição no canto da tela
    
    bird_group.update() #muda opassarinho conforme o game
    
    #desenha os elementos do grupo bird
    bird_group.draw(screen)
    
    pygame.display.update()
