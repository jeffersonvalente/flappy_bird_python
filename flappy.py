import pygame, random
from pygame.locals import *

#define tamanho da tela
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 800
SPEED = 10
GRAVITY = 1
GAMESPEED = 10

GROUND_WIDTH = 2 * SCREEN_WIDTH
GROUND_HEIGHT = 100

PIPE_WIDTH = 80
PIPE_HEIGHT = 500
PIPE_GAP = 200



#cria o passarinho
class Bird(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        #dicionario das imagens
        self.images = [pygame.image.load('F:/flappy_bird_python/sprites/bluebird-upflap.png',).convert_alpha(),
                       pygame.image.load('F:/flappy_bird_python/sprites/bluebird-midflap.png',).convert_alpha(),
                       pygame.image.load('F:/flappy_bird_python/sprites/bluebird-downflap.png').convert_alpha()]
        
        self.speed = SPEED
        
        
        self.current_image = 0  
        
        
        #chama a imagem e converte os pixels transparentes (convert_alpha)
        self.image = pygame.image.load('F:/flappy_bird_python/sprites/bluebird-upflap.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.image) #mascara de colisão
        
        self.rect = self.image.get_rect() #define a posição na tela
        self.rect[0] = SCREEN_WIDTH / 2
        self.rect[1] = SCREEN_HEIGHT / 2
        print(self.rect) 
    
    def update(self): #função para os estados da imagem
       self.current_image = (self.current_image + 1) % 3
       self.image = self.images[ self.current_image ]
       
       self.mask = pygame.mask.from_surface(self.image) #mascara de colisão
       
       #UPDATE HEIGHT
       self.rect[1] += self.speed #passaro cai
       
       self.speed += GRAVITY
       
    def bump(self):
        self.speed = -SPEED #passaro sobe
    
#cria os canos
class Pipe(pygame.sprite.Sprite):
    
    def __init__(self, inverted, xpos, ysize,):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load('F:/flappy_bird_python/sprites/pipe-red.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (PIPE_WIDTH, PIPE_HEIGHT))
        self.mask = pygame.mask.from_surface(self.image) #mascara de colisão
        
        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        
        if inverted:
            self.image = pygame.transform.flip(self.image, False, True) # flipa o cano ao contrario
            self.rect[1] = - (self.rect[3] -ysize)
        else:
            self.rect [1] = SCREEN_HEIGHT - ysize
        
        self.mask = pygame.mask.from_surface(self.image)
    
    def update(self):
        self.rect[0] -= GAMESPEED
        
class Ground(pygame.sprite.Sprite): #cria a base/chao
    
    def __init__(self, xpos):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load('F:/flappy_bird_python/sprites/base.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (GROUND_WIDTH, GROUND_HEIGHT))
     
        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.rect[1] = SCREEN_HEIGHT - GROUND_HEIGHT
        
    def update(self):
        self.rect[0] -= GAMESPEED

def is_off_screen(sprite):
    return sprite.rect[0] < -(sprite.rect[2])

#cria os canos randomicamente
def get_random_pipes(xpos):
    size = random.randint(100 , 300)
    pipe = Pipe(False, xpos, size)
    pipe_inverted = Pipe(True, xpos, SCREEN_HEIGHT - size - PIPE_GAP)
    return (pipe, pipe_inverted)
    

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#adiciona o background
BACKGROUND = pygame.image.load('F:/flappy_bird_python/sprites/background-day.png')
BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))

#adiciona o grupo do passarinho
bird_group = pygame.sprite.Group()
bird = Bird()
bird_group.add(bird)

#adiciona o grupo do chao
ground_group = pygame.sprite.Group()
for i in range(2):
    ground = Ground(GROUND_WIDTH * i )
    ground_group.add(ground)

clock = pygame.time.Clock() #define o fps/velocidade do bate asa

#adiciona grupo de canos
pipe_group = pygame.sprite.Group()
for i in range(2):
    pipes = get_random_pipes(SCREEN_WIDTH * i + 800)
    pipe_group.add(pipes[0])
    pipe_group.add(pipes[1])
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
    
    #valida se o ground está em tela ainda e remove
    if is_off_screen(ground_group.sprites()[0]):
        ground_group.remove(ground_group.sprites()[0])
        
        new_ground = Ground(GROUND_WIDTH - 20)
        ground_group.add(new_ground)
        
    if is_off_screen(pipe_group.sprites()[0]):
        pipe_group.remove(pipe_group.sprites()[0])
        pipe_group.remove(pipe_group.sprites()[0])
        
        pipes = get_random_pipes(SCREEN_WIDTH * 2)
        pipe_group.add(pipes[0])
        pipe_group.add(pipes[1])
       
        
    bird_group.update() #muda opassarinho conforme o game
    ground_group.update()
    pipe_group.update()
    
    #desenha os elementos do grupo bird
    bird_group.draw(screen)
    pipe_group.draw(screen)
    #desenha os elementos do grupo ground
    ground_group.draw(screen)
    
    #criando colisão
    if (pygame.sprite.groupcollide(bird_group, ground_group, False, False, pygame.sprite.collide_mask) or 
        pygame.sprite.groupcollide(bird_group, pipe_group, False, False, pygame.sprite.collide_mask)):
        input()
        break
    
    pygame.display.update()
