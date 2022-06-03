import pygame, sys
from config import * 

pygame.init()

def main_menu(tela):
    click = False
    state = INIT
    clock = pygame.time.Clock()
    while state == INIT:
        clock.tick(fps)  
        tela.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
              
        # texto('Guitar Hero', fonte, (255,255,255), tela, 20,20)
        mx, my = pygame.mouse.get_pos()
        start = pygame.Rect(width/5,300,width/4,50)
        exit = pygame.Rect(width/1.5,300,width/4,50)
        if start.collidepoint((mx,my)):
            if click:
                state = MUSICA

        if exit.collidepoint((mx,my)):
            if click:
                pygame.quit()

        pygame.draw.rect(tela, (255,0,0), start)
        pygame.draw.rect(tela, (255,0,0), exit)
        click = False
        pygame.display.flip()
        pygame.display.update()

    return state

