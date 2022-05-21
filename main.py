# Inicialização
import pygame
from pygame import NUMEVENTS, mixer #Utilizado para tocar os sons

#Inicialização
pygame.init()
mixer.init() 

janela = pygame.display.set_mode((1920, 1020))
pygame.display.set_caption('Guitar Hero')

#Cores
verde = (0,255,0)
vermelho = (255,0,0)
amarelo = (255,255,0)
azul = (0,0,255)
laranja = (255,122,0)
branco = (255,255,255)

#Posições
botao_verde = (780,900)
botao_vermelho = (870,900)
botao_amarelo = (960,900)
botao_azul = (1050,900)
botao_laranja = (1140,900)

#Teclas
tecla_verde = pygame.K_g
tecla_vermelha = pygame.K_h 
tecla_amarela = pygame.K_j
tecla_azul = pygame.K_k
tecla_laranja = pygame.K_l
 
#Estrutura para tocar a música
pygame.mixer.music.load('song1.mp3') #Carrega a música
pygame.mixer.music.set_volume(1) #o volume vai de 0 a 1
pygame.mixer.music.play()

game = True

# Loop
while game: 
    
    # Eventos
    for event in pygame.event.get():
        # Para sair

        if event.type == pygame.QUIT:
            game = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == tecla_verde:
                verde = (122, 255, 122)
            if event.key == tecla_vermelha:
                vermelho = (255,122,122)
            if event.key == tecla_amarela:
                amarelo = (255,255,122)
            if event.key == tecla_azul:
                azul = (122,122,255)
            if event.key == tecla_laranja:
                laranja = (255,0,122)

    # Saídas
    janela.fill((0, 0, 0))

    # Bolinhas
    bolinha_amarela = pygame.draw.circle(janela,amarelo,botao_amarelo,35)
    bolinha_vermelha = pygame.draw.circle(janela,vermelho,botao_vermelho,35)
    bolinha_verde = pygame.draw.circle(janela,verde,botao_verde,35)
    bolinha_azul = pygame.draw.circle(janela,azul,botao_azul,35)
    bolinha_laranja = pygame.draw.circle(janela,laranja,botao_laranja,35)

    #Retas
    reta_direita = pygame.draw.line(janela,branco,(700,1080),(700,0)) 
    reta_esquerda = pygame.draw.line(janela,branco,(1220,1080),(1220,0)) 

    # Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# Finalização
pygame.quit() 

