import pygame, sys
from config import * 

pygame.init()

bg = pygame.image.load('imagens/tela_acerto.jpg')

def ganhou(tela1):
    click = False
    state = GANHOU
    clock = pygame.time.Clock()
    while state == GANHOU:
        clock.tick(fps)  
        tela1.fill((0,0,0))

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
        tela1.blit(bg, (0,0))
              


              
        mx, my = pygame.mouse.get_pos()
        novamente = pygame.Rect(width/1.11,460,width/14,55)
        exit = pygame.Rect(width/1.11,530,width/14,55)
        if novamente.collidepoint((mx,my)):
            if click:
                state = MUSICA

        if exit.collidepoint((mx,my)):
            if click:
                pygame.quit()

        click = False
        pygame.display.flip()
        pygame.display.update()

    return state

