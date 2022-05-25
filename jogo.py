######### importando bibliotecas #########
import pygame
from pygame import K_ESCAPE, mixer

#======= inicialização =======#
pygame.init()
mixer.init()



#======= condições =======#
game = True

#======= variáveis e dimensões =======#
width = 800
height = 600

terco = int(width/3)
sexto = int(terco/6)

linha_e_i = (terco, 0)
linha_e_f = (terco, height)

linha_d_i = (2*terco, 0)
linha_d_f = (2*terco, height)

y_teclas = int(height * 15/17)

clock = pygame.time.Clock()
fps = 30

branco = (255,255,255)
verde = (0,255,0)
vermelho = (255,0,0)
amarelo = (255,255,0)
azul = (0,0,255)
laranja = (255,122,0)
transparente = (0,0,0,0)

#======= janela =======#
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Guitar Hero')
window.fill((0,0,0))


#======= dicionarios =======#

        #== dados das teclas ==#
dados_teclas = {
    'verde' : [verde, (terco+sexto , y_teclas), pygame.K_g],
    'vermelho' :[vermelho,(terco + 2 * sexto, y_teclas), pygame.K_h],
    'amarelo' : [amarelo,(terco + sexto*3, y_teclas), pygame.K_j],
    'azul' : [azul,(terco+4*sexto, y_teclas), pygame.K_k],
    'laranja' : [laranja,(terco+5*sexto, y_teclas), pygame.K_l]
}
        #=== dicionario para imagens, sons e fontes ===#
assets = {
    'amarelo' : pygame.image.load('assets/notes/nota_amarela.png').convert_alpha()
}





#============= classes =============#

class Teclas:
    def __init__(self, cor):                         #   recebe self e o nome da cor em string
        self.cor = dados_teclas[cor][0]              #   retorna o codigo RGB da cor 
        self.posi = dados_teclas[cor][1]             #   retorna a posição da tecla
        self.tecla = dados_teclas[cor][2]            #   retorna o input da tecla
        self.radius = 20

    def draw(self):
        pygame.draw.circle(window, self.cor, self.posi, self.radius)
    
    def lines(self):
        pygame.draw.line(window, branco, linha_d_i, linha_d_f)
        pygame.draw.line(window, branco, linha_e_i, linha_e_f)

class Notes(pygame.sprite.Sprite):
    def __init__(self, cor):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale((assets[cor]), (36,36))
        self.radius = 18
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = dados_teclas[cor][1][0] - self.radius
        self.rect.y = -(self.radius/2)
        self.speed_y = 10
    
    def update(self):
        self.rect.y += self.speed_y
        print(self.rect.y)
    
    def remove(self):
        self.image.fill(transparente)

todas_as_notas = pygame.sprite.Group()

#======= inicializando as sprites =======#

cor = 'amarelo'
nota = Notes(cor)



while game:
    
    clock.tick(fps)


    #===== eventos =====#
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key() == pygame.K_j:
                dados_teclas[cor][0] = branco

        if event.type == pygame.KEYUP:
            if event.key() == K_ESCAPE:
                game = False
            if event.key() == pygame.K_j:
                dados_teclas[cor][0] = amarelo
        if event.type == pygame.QUIT:
            game = False

            

        
        
    
    nota.update()
    window.fill((0,0,0))
    window.blit(nota.image, nota.rect)
    for c in dados_teclas:
        tecla = Teclas(c)
        tecla.draw()
        tecla.lines()
    
    pygame.display.update()
    


pygame.quit()