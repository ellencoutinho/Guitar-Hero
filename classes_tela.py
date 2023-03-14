import pygame, sys
from config import *

class Telas:
    def __init__(self, tela, resultado):
        self.tela = tela
        self.resultado = resultado

    def main_menu(self):
        bg = pygame.image.load('imagens/tela_inicial.jpg')
        state = INIT
        clock = pygame.time.Clock()
        while state == INIT:
            clock.tick(fps)  
            self.tela.fill((0,0,0))

            click = self.closeGame()
            self.tela.blit(bg, (0,0))
                
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

    def playlist(self):
        bg = pygame.image.load('imagens/sem_goat.jpg')
        click = False
        clock = pygame.time.Clock()
        state = MUSICA
        musica_escolhida = ''

        while state == MUSICA:
            clock.tick(fps)  
            self.tela.fill((0,0,0))

            click = self.closeGame()
            self.tela.blit(bg, (0,0))

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

        return lista_return

    def ganhou(self):
        bg = pygame.image.load('imagens/tela_acerto.jpg')
        fonte = pygame.font.SysFont(None, 60)
        porcentagem_acertos = (self.resultado[1]['acertos']/self.resultado[1]['notas'])*100
        valor = '{0:.2f}'.format(porcentagem_acertos)
        valor = str(valor)
        texto_acertos = fonte.render(valor + '%',True,verde)
        texto_erros = fonte.render(str(self.resultado[1]['erros']), True, verde)
        texto_combo_maximo = fonte.render(str(self.resultado[1]['combo']), True, verde)

        click = False
        state = GANHOU
        clock = pygame.time.Clock()
        while state == GANHOU:
            clock.tick(fps)  
            self.tela.fill((0,0,0))

            click = self.closeGame()
            self.tela.blit(bg, (0,0))

            #=== Blits dos textos ===#
            self.tela.blit(texto_acertos,(623,219))
            self.tela.blit(texto_erros,(506,314)) 
            self.tela.blit(texto_combo_maximo, (669,394))             

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

    def perdeu(self):
        bg = pygame.image.load('imagens/tela_erro.jpg')
        click = False
        state = PERDEU
        clock = pygame.time.Clock()
        while state == PERDEU:
            clock.tick(fps)  
            self.tela.fill((0,0,0))

            click = self.closeGame()
            self.tela.blit(bg, (0,0))           
                
            mx, my = pygame.mouse.get_pos()
            novamente = pygame.Rect(width/1.54,310,width/14,55)
            exit = pygame.Rect(width/1.53,495,width/14,55)
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
    
    def closeGame(self):
        click = False
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