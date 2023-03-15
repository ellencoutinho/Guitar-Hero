import pygame, sys
from config import * 

pygame.init()

bg = pygame.image.load('imagens/tela_erro.jpg')

def perdeu(tela2):
    click = False
    state = PERDEU
    clock = pygame.time.Clock()
    while state == PERDEU:
        clock.tick(fps)  
        tela2.fill((0,0,0))

        click = closeGame()
        tela2.blit(bg, (0,0))           
              
        mx, my = pygame.mouse.get_pos()
        novamente1 = pygame.Rect(width/1.54,310,width/14,55)
        exit = pygame.Rect(width/1.53,495,width/14,55)
        if novamente1.collidepoint((mx,my)):
            if click:
                state = MUSICA

        if exit.collidepoint((mx,my)):
            if click:
                pygame.quit()

        click = False
        pygame.display.flip()
        pygame.display.update()

    return state

def closeGame():
    for event in pygame.event.get():
        click = False
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
    return click

