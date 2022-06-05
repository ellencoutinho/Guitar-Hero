######### importando bibliotecas #########
import pygame
import random
from sprites import *
from config import *  
from selecao_musica import cardapio

def game(window):
    lista = cardapio(window)
    print(lista)


    #======= condições =======#
    game = True
    inicio = True


    clock = pygame.time.Clock()


    #======= janela =======#
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Guitar Hero')
    window.fill((0,0,0))


    dados_teclas = {
        'verde' : [verde, (terco+sexto , y_teclas), pygame.K_g],
        'vermelho' :[vermelho,(terco + 2 * sexto, y_teclas), pygame.K_h],
        'amarelo' : [amarelo,(terco + sexto*3, y_teclas), pygame.K_j],
        'azul' : [azul,(terco+4*sexto, y_teclas), pygame.K_k],
        'laranja' : [laranja,(terco+5*sexto, y_teclas), pygame.K_l]
    }

    #======= dicionarios =======#

            #== dados das teclas ==#
    assets = {
        'notas' : {
            'verde' : pygame.image.load('assets/notes/nota_verde.png').convert_alpha(),
            'vermelho' : pygame.image.load('assets/notes/nota_vermelha.png').convert_alpha(),
            'amarelo' : pygame.image.load('assets/notes/nota_amarela.png').convert_alpha(),
            'azul' : pygame.image.load('assets/notes/nota_azul.png').convert_alpha(),
            'laranja' : pygame.image.load('assets/notes/nota_laranja.png').convert_alpha()
        },
        'holds' : {
            'amarelo' : pygame.image.load('assets/notes/hold_amarelo.png').convert_alpha()
        }
    }

    todas_as_notas = pygame.sprite.Group()
    
    #======= inicializando as sprites =======#

    atual = 'amarelo'
    nota = Notes(atual, assets, dados_teclas)
    tecla = Teclas(atual, window, dados_teclas)
    acertos = 0
    tempo = 0
    segundo = 0
    ta = 0

    #====== estrutura para tocar música ======#
    pygame.mixer.music.load(lista[1])            #Carrega a música
    pygame.mixer.music.set_volume(1)                     #o volume vai de 0 a 1

    #========== fonte para textos ============#
    font = pygame.font.SysFont(None, 48)
    state = GAME
    while game:
        if inicio == False: 
            clock.tick(fps)
            segundo = segundo % fps
            if segundo == 0:
                tempo += 1 
            segundo += 1
            print(tempo)
            if tempo != ta:
                ta+=1
            # Notes(random.choice(['verde', 'vermelho','amarelo','azul','laranja']))
                nota = Notes(random.choice(['verde', 'vermelho','amarelo','azul','laranja']),assets, dados_teclas)    

        tecla_start = font.render("Aperte uma tecla para começar", True,  (255,255,255)) 

        #===== eventos =====#
        for event in pygame.event.get():
            

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    dados_teclas['verde'][0] = branco
                    gpress = nota.nome == 'verde'
                    if nota.rect.y+2*nota.radius>tecla.posi[1]-tecla.radius and nota.rect.y<tecla.posi[1]+tecla.radius and gpress:
                        acertos+=1
                        nota.remove()
                
                if event.key == pygame.K_h:
                    dados_teclas['vermelho'][0] = branco
                    hpress = nota.nome == 'vermelho'
                    if nota.rect.y+2*nota.radius>tecla.posi[1]-tecla.radius and nota.rect.y<tecla.posi[1]+tecla.radius and hpress:
                        acertos+=1
                        nota.remove()
                
                if event.key == pygame.K_j:
                    dados_teclas['amarelo'][0] = branco
                    jpress = nota.nome == 'amarelo'
                    if nota.rect.y+2*nota.radius>tecla.posi[1]-tecla.radius and nota.rect.y<tecla.posi[1]+tecla.radius and jpress:
                        acertos += 1
                        nota.remove()

                if event.key == pygame.K_k:
                    dados_teclas['azul'][0] = branco
                    kpress = nota.nome == 'azul'
                    if nota.rect.y+2*nota.radius>tecla.posi[1]-tecla.radius and nota.rect.y<tecla.posi[1]+tecla.radius and kpress:
                        acertos +=1
                        nota.remove()

                if event.key == pygame.K_l:
                    dados_teclas['laranja'][0] = branco
                    lpress = nota.nome  == 'laranja'
                    if nota.rect.y+2*nota.radius>tecla.posi[1]-tecla.radius and nota.rect.y<tecla.posi[1]+tecla.radius and lpress:
                        acertos+=1
                        nota.remove()


            if event.type == pygame.KEYUP:
                if inicio:
                    inicio = False
                    pygame.mixer.music.play()

                if event.key == pygame.K_ESCAPE:
                    game = False


                if event.key == pygame.K_g:
                    dados_teclas['verde'][0] = verde
                    gpress = False

                if event.key == pygame.K_h:
                    dados_teclas['vermelho'][0] = vermelho
                    hpress = False

                if event.key == pygame.K_j:
                    dados_teclas['amarelo'][0] = amarelo
                    jpress = False   

                if event.key == pygame.K_k:
                    dados_teclas['azul'][0] = azul
                    kpress = False

                if event.key == pygame.K_l:

                    dados_teclas['laranja'][0] = laranja
                    lpress = False

            if event.type == pygame.QUIT:
                game = False
                state = QUIT        
        
        nota.update()
        window.fill((0,0,0))
        window.blit(nota.image, nota.rect)

        if inicio:
            window.blit(tecla_start,(terco-101,height/3))  
        
        tecla.draw()
        for c in dados_teclas:
            tecla = Teclas(c, window, dados_teclas)
            tecla.draw()
            tecla.lines()
        
        pygame.display.update()
        
    return state