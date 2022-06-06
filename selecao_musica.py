from tkinter import RIGHT
import pygame, sys
from config import *

bgmusica = pygame.image.load('imagens/sem_goat.jpg')


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
        janela.blit(bgmusica, (0,0))

        mx, my = pygame.mouse.get_pos()
        m1 = pygame.Rect(width/12,130,width/2,50)
        m2 = pygame.Rect(width/12,200,width/2.2,50)
        m3 = pygame.Rect(width/12,290,width/1.7,50)
        m4 = pygame.Rect(width/12,350,width/1.9,50)
        m5 = pygame.Rect(width/12,420,width/1.5,50)
        m6 = pygame.Rect(width/12,505,width/4.5,50)

        if m1.collidepoint((mx,my)):
            if click:
                musica_escolhida = 'assets/musicas/riptide_vance-joy.mp3'
                state = GAME
        if m2.collidepoint((mx,my)):
            if click:
                musica_escolhida = 'assets/musicas/grapejuice-harry.mp3'
                state = GAME
        if m3.collidepoint((mx,my)):
            if click:
                musica_escolhida = 'assets/musicas/jose_gonzalez-killing_for_love.mp3'
                state = GAME
        if m4.collidepoint((mx,my)):
            if click:
                musica_escolhida = 'assets/musicas/clairo_flamin-hot-cheetos.mp3'
                state = GAME
        if m5.collidepoint((mx,my)):
            if click:
                musica_escolhida = 'assets/musicas/a-drowning_how-to-destroy-angels.mp3'
                state = GAME
        if m6.collidepoint((mx,my)):
            if click:
                musica_escolhida = 'assets/musicas/eyen_plaid.mp3'
                state = GAME



        pygame.display.flip()
        pygame.display.update()
        click = False
        lista_return = [state,musica_escolhida]
        print(lista_return)

    return lista_return
