# Inicialização
import pygame

#Inicialização
pygame.init()

janela = pygame.display.set_mode((1920, 1020))
pygame.display.set_caption('Guitar Hero')

#Cores
amarelo = (255,255,0)
vermelho = (255,0,0)
azul = (0,0,255)
verde = (0,255,0)
laranja = (255,122,0)
branco = (255,255,255)

game = True

# Loop
while game: 
    # Eventos
    for event in pygame.event.get():
        # Para sair
        if event.type == pygame.QUIT:
            game = False

    # Saídas
    janela.fill((0, 0, 0))

    # Bolinhas
    bolinha_amarela = pygame.draw.circle(janela,amarelo,(960,900),35)
    bolinha_vermelha = pygame.draw.circle(janela,vermelho,(870,900),35)
    bolinha_verde = pygame.draw.circle(janela,verde,(780,900),35)
    bolinha_azul = pygame.draw.circle(janela,azul,(1050,900),35)
    bolinha_laranja = pygame.draw.circle(janela,laranja,(1140,900),35)

    #Retas
    reta_direita = pygame.draw.line(janela,branco,(700,1080),(700,0)) 
    reta_esquerda = pygame.draw.line(janela,branco,(1220,1080),(1220,0)) 

    # Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# Finalização
pygame.quit() 

