# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame, sys
from config import *
from esqueleto import game
from classes_tela import *

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
        telas = Telas(window, None)
        state = telas.main_menu() 
    if state == MUSICA:
        state = telas.playlist()
    if state[0] == 2:
        state = game(window)
        dados = state
    if dados[0] == 3:
        telas = Telas(window, dados)
        state = telas.ganhou()
    if dados[0] == 5:
        telas = Telas(window, None)
        state = telas.perdeu()

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados