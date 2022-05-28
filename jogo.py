######### importando bibliotecas #########
import pygame
import random
from pygame import K_ESCAPE, mixer, K_j

#======= inicialização =======#
pygame.init()
pygame.font.init()
mixer.init()



#======= condições =======#
game = True
inicio = True

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
fps = 60

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
        self.nome = cor
        self.color = dados_teclas[cor][0]
        self.image = pygame.transform.scale((assets['notas'][cor]), (36,36))
        self.radius = 18
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = dados_teclas[cor][1][0] - self.radius
        self.rect.y = -(self.radius/2)
        self.speed_y = 10                                                 #Seria melhor 5, mas a nota não chegaria até o final
    
    def update(self):
        self.rect.y += self.speed_y

    
    def remove(self):
        self.image.fill(transparente)

    #def hold(self, cor, time):
    #    pygame.sprite.Sprite.__init__(self)
    #    self.len = time*fps
     #   self.image = pygame.transform.scale((assets['holds'][cor]), (36,self.len))
      #  self.mask = pygame.mask.from_surface(self.image)
       # self.rect = self.image.get_rect()
        #self.rect.x = dados_teclas[cor][1][0] - self.radius
        #self.rect.y = -(self.radius)
        

todas_as_notas = pygame.sprite.Group()
 
#======= inicializando as sprites =======#

atual = 'amarelo'
nota = Notes(atual)
tecla = Teclas(atual)
tempo = 0
segundo = 0
ta = 0

#====== estrutura para tocar música ======#
pygame.mixer.music.load('song1.mp3')            #Carrega a música
pygame.mixer.music.set_volume(1)                #o volume vai de 0 a 1

#========== fonte para textos ============#
font = pygame.font.SysFont(None, 48)

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
            nota = Notes(random.choice(['verde', 'vermelho','amarelo','azul','laranja'])) #O problema está aqui        

    tecla_start = font.render("Aperte uma tecla para começar", True,  (255,255,255)) 

    #===== eventos =====#
    for event in pygame.event.get():
        

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                dados_teclas['verde'][0] = branco
                gpress = nota.nome == 'verde'
                if nota.rect.y+2*nota.radius>tecla.posi[1]-tecla.radius and nota.rect.y<tecla.posi[1]+tecla.radius and gpress:
                    nota.remove()
            
            if event.key == pygame.K_h:
                dados_teclas['vermelho'][0] = branco
                hpress = nota.nome == 'vermelho'
                if nota.rect.y+2*nota.radius>tecla.posi[1]-tecla.radius and nota.rect.y<tecla.posi[1]+tecla.radius and hpress:
                    nota.remove()
            
            if event.key == pygame.K_j:
                dados_teclas['amarelo'][0] = branco
                jpress = nota.nome == 'amarelo'
                if nota.rect.y+2*nota.radius>tecla.posi[1]-tecla.radius and nota.rect.y<tecla.posi[1]+tecla.radius and jpress:
                    nota.remove()

            if event.key == pygame.K_k:
                dados_teclas['azul'][0] = branco
                kpress = nota.nome == 'azul'
                if nota.rect.y+2*nota.radius>tecla.posi[1]-tecla.radius and nota.rect.y<tecla.posi[1]+tecla.radius and kpress:
                    nota.remove()

            if event.key == pygame.K_l:
                dados_teclas['laranja'][0] = branco
                lpress = nota.nome  == 'laranja'
                if nota.rect.y+2*nota.radius>tecla.posi[1]-tecla.radius and nota.rect.y<tecla.posi[1]+tecla.radius and lpress:
                    nota.remove()


        if event.type == pygame.KEYUP:
            if inicio:
                inicio = False
                pygame.mixer.music.play()

            if event.key == K_ESCAPE:
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
    
    nota.update()
    window.fill((0,0,0))
    window.blit(nota.image, nota.rect)

    if inicio:
        window.blit(tecla_start,(terco-101,height/3))  
    
    tecla.draw()
    for c in dados_teclas:
        tecla = Teclas(c)
        tecla.draw()
        tecla.lines()
    
    pygame.display.update()
    


pygame.quit()