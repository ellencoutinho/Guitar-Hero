# Inicialização
import pygame
from pygame import K_ESCAPE, K_SPACE, NUMEVENTS, mixer #Utilizado para tocar os sons

WIDTH = 1920
HEIGHT = 1020
INTERVALO = 520
INTERVALO_INI = (WIDTH-INTERVALO)/2

#Inicialização
pygame.init()
mixer.init() 

janela = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Guitar Hero')

#Posições
botao_verde = (INTERVALO_INI + 35,900)
botao_vermelho = (INTERVALO_INI + 70 * 1 + 35,900)
botao_amarelo = (960,900)
botao_azul = (1050,900)
botao_laranja = (1140,900)

#Teclas
tecla_verde = pygame.K_g
tecla_vermelha = pygame.K_h 
tecla_amarela = pygame.K_j
tecla_azul = pygame.K_k
tecla_laranja = pygame.K_l

#Cores
verde = (0,255,0)
vermelho = (255,0,0)
amarelo = (255,255,0)
azul = (0,0,255)
laranja = (255,122,0)
branco = (255,255,255)
        

#Dicionário para imagens, sons e fontes
assets = {}
assets['amarelo'] = pygame.image.load('assets/notes/nota_amarela.png').convert_alpha()
assets['vermelho'] =pygame.image.load('assets/notes/nota_vermelha.png').convert_alpha()
assets['verde'] = pygame.image.load('assets/notes/nota_verde.png').convert_alpha()
assets['azul'] = pygame.image.load('assets/notes/nota_azul.png').convert_alpha()
assets['laranja'] = pygame.image.load('assets/notes/nota_laranja.png').convert_alpha()

#Classe de bolinhas
class Notas(pygame.sprite.Sprite):
    def __init__(self, cor):        
        pygame.sprite.Sprite.__init__(self)
        self.image = assets[cor]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 935
        self.rect.y = -12.5
        self.speedy = 10
    
    def update(self):
        self.rect.y += self.speedy
    
    def remove(self):
        transp = (0,0,0,0)
        self.image.fill(transp)

    
clock = pygame.time.Clock()
todas_as_notas = pygame.sprite.Group()
FPS = 30

#Estrutura para tocar a música
pygame.mixer.music.load('song1.mp3') #Carrega a música
pygame.mixer.music.set_volume(1) #o volume vai de 0 a 1

game = True
vd = Notas('verde')
vm = Notas('vermelho')
am = Notas('amarelo')
az = Notas('azul')
lr = Notas('laranja')

music_p = False
tempo = 0

font = pygame.font.SysFont(None, 48)

partitura = {
    5: 'amarelo',
    10: 'azul'
}
# Loop
segundo = 0
while game: 
    clock.tick(FPS)
    segundo = segundo % FPS
    if segundo == 0:
        tempo += 1 
    segundo += 1
    if tempo in partitura:
        variavel = 'para de reclamar do meu codigo porra'
        

    # Eventos
    for event in pygame.event.get():
        # Para sair
        if event.type == pygame.KEYUP:
            if event.key == K_SPACE:
                pygame.mixer.music.play()


            
        if event.type == pygame.QUIT:
            game = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == tecla_verde:
                verde = branco
            if event.key == tecla_vermelha:
                vermelho = branco
            if event.key == tecla_amarela:
                amarelo = branco
                if am.rect.y>865 and am.rect.y<935:
                    am.remove()

            if event.key == tecla_azul:
                azul = branco
            if event.key == tecla_laranja:
                laranja = branco   

        
    
    am.update()

    # Saídas
    janela.fill((0, 0, 0))

    # Bolinhas
    bolinha_amarela = pygame.draw.circle(janela,amarelo,botao_amarelo,35)
    bolinha_vermelha = pygame.draw.circle(janela,vermelho,botao_vermelho,35)
    bolinha_verde = pygame.draw.circle(janela,verde,botao_verde,35)
    bolinha_azul = pygame.draw.circle(janela,azul,botao_azul,35)
    bolinha_laranja = pygame.draw.circle(janela,laranja,botao_laranja,35)

    #Cores
    verde = (0,255,0)
    vermelho = (255,0,0)
    amarelo = (255,255,0)        
    azul = (0,0,255)
    laranja = (255,122,0)
    branco = (255,255,255)
        

    janela.blit(am.image,am.rect)

    #Retas
    reta_direita = pygame.draw.line(janela,branco,((WIDTH-INTERVALO)/2,1080),(700,0)) 
    reta_esquerda = pygame.draw.line(janela,branco,((WIDTH+INTERVALO)/2,1080),(1220,0)) 

    # Desenhando o score
    print(tempo)
    text_surface = font.render("{}".format(tempo), True, (255, 255, 0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (100,  100)
    janela.blit(text_surface, text_rect)

    # Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# Finalização
pygame.quit() 

