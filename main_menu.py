import pygame, sys
from config import * 

pygame.init()

bg = pygame.image.load('imagens/tela_inicial.jpg')

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
        tela.blit(bg, (0,0))
              


              
        mx, my = pygame.mouse.get_pos()
        start = pygame.Rect(width/2.1,380,width/8,100)
        exit = pygame.Rect(width/1.35,380,width/8,100)
        if start.collidepoint((mx,my)):
            if click:
                state = MUSICA

        if exit.collidepoint((mx,my)):
            if click:
                pygame.quit()


        click = False
        pygame.display.flip()
        pygame.display.update()

    return state

