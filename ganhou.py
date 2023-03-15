import pygame, sys
from config import * 

pygame.init()

bg = pygame.image.load('imagens/tela_acerto.jpg')

def ganhou_function(tela1, resultado):
    fonte = pygame.font.SysFont(None, 60)
    porcentagem_acertos = (resultado[1]['acertos']/resultado[1]['notas'])*100
    valor = '{0:.2f}'.format(porcentagem_acertos)
    valor = str(valor)
    texto_acertos = fonte.render(valor + '%',True,verde)
    texto_erros = fonte.render(str(resultado[1]['erros']), True, verde)
    texto_combo_maximo = fonte.render(str(resultado[1]['combo']), True, verde)



    click = False
    state = GANHOU
    clock = pygame.time.Clock()
    while state == GANHOU:
        clock.tick(fps)  
        tela1.fill((0,0,0))

        click = closeGame()
        tela1.blit(bg, (0,0))

        #=== Blits dos textos ===#
        tela1.blit(texto_acertos,(623,219))
        tela1.blit(texto_erros,(506,314)) 
        tela1.blit(texto_combo_maximo, (669,394))             

              
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

def closeGame():
    
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
    return click

