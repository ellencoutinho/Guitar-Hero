import pygame, sys

clock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Tela inicial')
tela = pygame.display.set_mode((1000,700),0,32)

fonte = pygame.font.SysFont(None, 20)

def texto(text, fonte, cor, superficie, x ,y):
    texto_objeto = fonte.render(text, 1, cor)
    texto_rect = texto_objeto.get_rect()
    texto_rect.topleft = (x,y)
    superficie.blit(texto_objeto, texto_rect)
click = False
def main_menu():
    while True:
        tela.fill((0,0,0))
        texto('Guitar Hero', fonte, (255,255,255), tela, 20,20)
        mx, my = pygame.mouse.get_pos()
        start = pygame.Rect(50,100,200,50)
        exit = pygame.Rect(50,200,200,50)
        if start.collidepoint((mx,my)):
            if click:
                game()
        if exit.collidepoint((mx,my)):
            if click:
                pass
        pygame.draw.rect(tela, (255,0,0), start)
        pygame.draw.rect(tela, (255,0,0), exit)
        click = False
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == KEYDOWN:
                pygame.quit()
                sys.exit()
            if evento.type == MOUSEBUTTONDOWN:
                if evento.button == 1:
                    click = True
        pygame.display.update()
        clock.tick(60)
def game():
    rodando = True
    while rodando:
        tela.fill((0,0,0))
        texto('testando start', fonte, (255,255,255), tela, 20,20)
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == K_ESCAPE:
                rodando = False
        pygame.display.update()
        clock.tick(60)
main_menu()