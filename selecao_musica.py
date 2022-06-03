from tkinter import RIGHT
import pygame, sys
from config import *

def cardapio(janela):
    click = False
    clock = pygame.time.Clock()
    state = MUSICA

    while state == MUSICA:
        print('entrei no while')
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
                state = GAME
            
        elif jogo_desenhado.collidepoint((mx,my)):
            if click:
                state = GAME_DESENHADO

        pygame.display.flip()

     #   exit = pygame.Rect(width/1.5,300,width/4,50)


      #  if exit.collidepoint((mx,my)):
      #      if click:
        #        pygame.quit()

    print('sai do while')
      #  pygame.draw.rect(janela, (255,0,0), exit)
     #   click = False
        
     #   return state
    return state
