import pygame, sys
from config import *

def cardapio(janela):
    print('entrei')
    clock = pygame.time.Clock()
    while state == MUSICA:
        clock.tick(fps)  

        for evento in pygame.event.get():
            if evento.type == QUIT:
                state = QUIT
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                state = GAME
               # pygame.quit()
               # sys.exit()
         #   if evento.type == pygame.MOUSEBUTTONDOWN:
          #      if evento.button == 1:
           #         click = True

        janela.fill((0,0,0))
              
        # texto('Guitar Hero', fonte, (255,255,255), tela, 20,20)
        mx, my = pygame.mouse.get_pos()
        song1 = pygame.Rect(width/5,300,width/4,50)
     #   exit = pygame.Rect(width/1.5,300,width/4,50)
        if song1.collidepoint((mx,my)):
            print('iuepa')
          #  if click:
               # state = GAME

      #  if exit.collidepoint((mx,my)):
      #      if click:
        #        pygame.quit()

      #  pygame.draw.rect(janela, (255,0,0), start)
      #  pygame.draw.rect(janela, (255,0,0), exit)
     #   click = False
        pygame.display.flip()
     #   return state
    return state
