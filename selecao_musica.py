from tkinter import RIGHT
import pygame, sys
from config import *

def cardapio(janela):
    click = False
    clock = pygame.time.Clock()
    state = MUSICA
    musica_escolhida = ''

    while state == MUSICA:
        clock.tick(fps)  
        janela.fill((0,0,0))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                state = QUIT
                pygame.quit()
                sys.exit()
            
            if evento.type == pygame.KEYDOWN:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button:
                if evento.button == 1:
                    click = True
              
        # texto('Guitar Hero', fonte, (255,255,255), tela, 20,20)
        mx, my = pygame.mouse.get_pos()
        jogo_comum = pygame.Rect(width/5,300,width/4,50)
        jogo_desenhado = pygame.Rect(width/1.5,300,width/4,50)
        pygame.draw.rect(janela, branco, jogo_comum)
        pygame.draw.rect(janela, azul, jogo_desenhado)

        if jogo_comum.collidepoint((mx,my)):
            if click:
                #musica_escolhida = 'assets/musicas/jose_gonzalez-killing_for_love.mp3'
                #musica_escolhida = 'assets/musicas/clairo_flamin-hot-cheetos.mp3'
                #musica_escolhida = 'assets/musicas/grapejuice-harry.mp3'
                #Colocar posição de cada música em if
                #musica_escolhida = 'assets/musicas/eyen_plaid.mp3'
                #musica_escolhida = 'assets/musicas/riptide_vance-joy.mp3'
                musica_escolhida = 'assets/musicas/a-drowning_how-to-destroy-angels.mp3'
                state = GAME
            
        elif jogo_desenhado.collidepoint((mx,my)):
            if click:
                state = GAME_DESENHADO

        pygame.display.flip()
        
        lista_return = [state,musica_escolhida]
        print(lista_return)

    return lista_return
