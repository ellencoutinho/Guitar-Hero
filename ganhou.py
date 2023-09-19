import pygame, sys
from config import * 

pygame.init()

bg = pygame.image.load('imagens/tela_acerto.jpg')

def desenha_texto(surface, text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)

def click(mx, my, buttons):
    for button in buttons:
        if button.rect.collidepoint((mx, my)):
            button.action()

class Button:
    def _init_(self, text, font, color, rect, action):
        self.text = text
        self.font = font
        self.color = color
        self.rect = pygame.Rect(rect)
        self.action = action

def checa_se_ganhou(tela1, resultado):
    fonte = pygame.font.SysFont(None, 60)
    porcentagem_acertos = (resultado[1]['acertos']/resultado[1]['notas'])*100
    valor = '{0:.2f}'.format(porcentagem_acertos)
    valor = str(valor)
    texto_acertos = fonte.render(valor + '%',True,verde)
    texto_erros = fonte.render(str(resultado[1]['erros']), True, verde)
    texto_combo_maximo = fonte.render(str(resultado[1]['combo']), True, verde)

    buttons = [
        Button("Novamente", fonte, verde, (width / 1.11, 460, width / 14, 55), lambda: change_state(MUSICA)),
        Button("Sair", fonte, verde, (width / 1.11, 530, width / 14, 55), pygame.quit),
    ]

    click = False
    state = GANHOU
    clock = pygame.time.Clock()

    def change_state(new_state):
        nonlocal state
        state = new_state

    while state == GANHOU:
        clock.tick(fps)  
        tela1.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                change_state(QUIT)
            if event.type == pygame.KEYDOWN:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True


        tela1.blit(bg, (0,0))

        #=== Blits dos textos ===#
        tela1.blit(texto_acertos,(623,219))
        tela1.blit(texto_erros,(506,314)) 
        tela1.blit(texto_combo_maximo, (669,394))             
              
        mx, my = pygame.mouse.get_pos()

        click(mx, my, buttons)

        click = False
        pygame.display.flip()
        pygame.display.update()

    return state