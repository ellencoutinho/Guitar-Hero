# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from config import *
from ganhou import checa_se_ganhou
from perdeu import perdeu
from main_menu import main_menu
from jogo import game
from selecao_musica import cardapio


#======= inicialização =======#
pygame.init()
pygame.font.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Guitar Hero')

state = INIT
while state != QUIT:
    if state == INIT:
        state = main_menu(window) 
    if state == MUSICA:
        state = cardapio(window)
    if state[0] == 2:
        state = game(window)
        dados = state
    if dados[0] == 3:
        state = checa_se_ganhou(window,dados)
    if dados[0] == 5:
        state = perdeu(window)

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados