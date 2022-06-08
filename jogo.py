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

    #======= variaveis =======#
    player_data = {
        'combo' : 0,
        'acertos' : 0,
        'erros' : 0, 
        'notas' : 0
    }
    combo = 0
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
        'lifebar' : {
            '5' : pygame.image.load('assets/barra/barra de vida.png').convert_alpha(),
            '4' : pygame.image.load('assets/barra/barra de vida-1.png').convert_alpha(),
            '3' : pygame.image.load('assets/barra/barra de vida-2.png').convert_alpha(),
            '2' : pygame.image.load('assets/barra/barra de vida-3.png').convert_alpha(),
            '1' : pygame.image.load('assets/barra/barra de vida-4.png').convert_alpha(),
            '0' : pygame.image.load('assets/barra/barra de vida-5.png').convert_alpha()
        }
    }

    todas_as_notas = pygame.sprite.Group()
    
    #======= inicializando as sprites =======#

    atual = 'verde'
    nota = Notes(atual, assets, dados_teclas)
    tecla = Teclas(atual, window, dados_teclas)
    acertos = 0
    vida=5
    tempo = 0
    segundo = 0
    ta = 0

    pygame.mixer.init()

    #====== estrutura para tocar música ======#
    pygame.mixer.music.load(lista[1])                    #Carrega a música
    pygame.mixer.music.set_volume(1)                     #o volume vai de 0 a 1

    #========== fonte para textos ============#
    font = pygame.font.SysFont(None, 48)
    state = GAME
    while state == GAME:
        
        cenario = pygame.image.load('imagens/background.jpg')
        lifebar = assets['lifebar'][str(vida)]

        if inicio == False: 
            clock.tick(fps)
            segundo = segundo % fps
            if segundo == 0:
                tempo += 1 
            segundo += 1
#print(tempo)
            if tempo != ta:
                ta+=1
            # Notes(random.choice(['verde', 'vermelho','amarelo','azul','laranja']))
                nota = Notes(random.choice(['verde', 'vermelho','amarelo','azul','laranja']),assets, dados_teclas)
                todas_as_notas.add(nota)
                player_data['notas'] +=1    

        else:
            tecla_start = font.render("Aperte uma tecla para começar", True,  (255,255,255)) 

        #===== eventos =====#
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            
            #if tempo >= 2:
                state = PERDEU
                
            if tempo >= dicio[lista[1]]:
                state = GANHOU


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    dados_teclas['verde'][0] = branco
                    gpress = nota.nome == 'verde'
                    if nota.rect.y+2*nota.radius>tecla.posi[1]-tecla.radius and nota.rect.y<tecla.posi[1]+tecla.radius and gpress:
                        player_data['acertos']+=1
                        nota.remove()
                        vida+=1
                    else:
                        player_data['erros'] +=1
                        if combo>player_data['combo']:
                            player_data['combo'] = combo
                        vida-=1
                
                if event.key == pygame.K_h:
                    dados_teclas['vermelho'][0] = branco
                    hpress = nota.nome == 'vermelho'
                    if nota.rect.y+2*nota.radius>tecla.posi[1]-tecla.radius and nota.rect.y<tecla.posi[1]+tecla.radius and hpress:
                        player_data['acertos']+=1
                        nota.remove()
                        vida+=1
                    else:
                        player_data['erros'] +=1
                        vida-=1
                        if combo>player_data['combo']:
                            player_data['combo'] = combo
                
                if event.key == pygame.K_j:
                    dados_teclas['amarelo'][0] = branco
                    jpress = nota.nome == 'amarelo'
                    if nota.rect.y+2*nota.radius>tecla.posi[1]-tecla.radius and nota.rect.y<tecla.posi[1]+tecla.radius and jpress:
                        player_data['acertos'] += 1
                        nota.remove()
                        vida+=1      
                    else:
                        player_data['erros'] +=1
                        vida-=1
                        if combo>player_data['combo']:
                            player_data['combo'] = combo

                if event.key == pygame.K_k:
                    dados_teclas['azul'][0] = branco
                    kpress = nota.nome == 'azul'
                    if nota.rect.y+2*nota.radius>tecla.posi[1]-tecla.radius and nota.rect.y<tecla.posi[1]+tecla.radius and kpress:
                        player_data['acertos'] +=1
                        nota.remove()
                        player_data['combo']+=1
                        vida+=1                    
                    else:
                        player_data['erros'] +=1
                        vida-=1
                        if combo>player_data['combo']:
                            player_data['combo'] = combo

                if event.key == pygame.K_l:
                    dados_teclas['laranja'][0] = branco
                    lpress = nota.nome  == 'laranja'
                    if nota.rect.y+2*nota.radius>tecla.posi[1]-tecla.radius and nota.rect.y<tecla.posi[1]+tecla.radius and lpress:
                        player_data['acertos']+=1
                        nota.remove()
                        player_data['combo']+=1
                        vida+=1
                    else:
                        player_data['erros'] +=1
                        vida-=1
                        if combo>player_data['combo']:
                            player_data['combo'] = combo
                


            if event.type == pygame.KEYUP:
                if inicio:
                    inicio = False
                    pygame.mixer.music.play()

                if event.key == pygame.K_ESCAPE:
                    exit()


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
        if nota.rect.y - 60 == y_teclas-2*tecla.radius+2:
            print('entrei')
            player_data['erros']+=1
            vida-=1

        if vida > 5:
            vida = 5
        if vida < 0:
            vida = 0
        
        

        window.blit(cenario,(0,0))
        window.blit(nota.image, nota.rect)
        window.blit(lifebar, (terco-2*sexto, y_teclas))
        todas_as_notas.update()
        if inicio:
            window.blit(tecla_start,(terco-101,height/3))  
        
        tecla.draw()
        for c in dados_teclas:
            tecla = Teclas(c, window, dados_teclas)
            tecla.draw()
            tecla.lines()
        
        lista_para_return = [state, player_data]
        print('erro', player_data['erros'], 'vida', vida, '\n', 'y', nota.rect.y, 'limite', y_teclas-2*tecla.radius+2)
        pygame.display.update()
        
    return lista_para_return