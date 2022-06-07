#============= classes =============#

import pygame
from config import *


class Teclas:
    def __init__(self, cor, window, dados_teclas):                         #   recebe self e o nome da cor em string
        self.window = window
        self.dados_teclas = dados_teclas
        self.cor = dados_teclas[cor][0]              #   retorna o codigo RGB da cor 
        self.posi = dados_teclas[cor][1]             #   retorna a posição da tecla
        self.tecla = dados_teclas[cor][2]            #   retorna o input da tecla
        self.radius = 20

    def draw(self):
        pygame.draw.circle(self.window, self.cor, self.posi, self.radius)
    
    def lines(self):
        pygame.draw.line(self.window, branco, linha_d_i, linha_d_f)
        pygame.draw.line(self.window, branco, linha_e_i, linha_e_f)

class Notes(pygame.sprite.Sprite):
    def __init__(self, cor, assets, dados_teclas):
        pygame.sprite.Sprite.__init__(self)
        self.dados_teclas = dados_teclas
        self.nome = cor
        self.color = dados_teclas[cor][0]
        self.image = pygame.transform.scale((assets['notas'][cor]), (36,36))
        self.radius = 18
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = dados_teclas[cor][1][0] - self.radius
        self.rect.y = -(self.radius/2)
        self.speed_y = 10                     
    
    def update(self):
        self.rect.y += self.speed_y

    
    def remove(self):
        self.image.fill(transparente)