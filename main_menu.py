# Inicialização
import pygame
from pygame import NUMEVENTS, mixer #Utilizado para tocar os sons

#Inicialização
pygame.init()
mixer.init() 
main_menu = True
janela = pygame.display.set_mode((1920, 1020))
pygame.display.set_caption('Guitar Hero')

#Posições
botao_verde = (780,900)
botao_vermelho = (870,900)
botao_amarelo = (960,900)
botao_azul = (1050,900)
botao_laranja = (1140,900)

#Teclas
tecla_verde = pygame.K_g
tecla_vermelha = pygame.K_h 
tecla_amarela = pygame.K_j
tecla_azul = pygame.K_k
tecla_laranja = pygame.K_l

#Cores
verde = (0,255,0)
vermelho = (255,0,0)
amarelo = (255,255,0)
azul = (0,0,255)
laranja = (255,122,0)
branco = (255,255,255)
        

#Dicionário para imagens, sons e fontes
assets = {}
assets['amarelo'] = pygame.image.load('assets/notes/nota_amarela.png').convert_alpha()
assets['vermelho'] =pygame.image.load('assets/notes/nota_vermelha.png').convert_alpha()
assets['verde'] = pygame.image.load('assets/notes/nota_verde.png').convert_alpha()
assets['azul'] = pygame.image.load('assets/notes/nota_azul.png').convert_alpha()
assets['laranja'] = pygame.image.load('assets/notes/nota_laranja.png').convert_alpha()
start_img = pygame.image.load('imagens/tela_inicio/start.png').convert_alpha()
exit_img = pygame.image.load('imagens/tela_inicio/start.png').convert_alpha()

class botao:
    def __init__(self, x, y, imagem, escala):
        largura = imagem.get_width()
        altura = imagem.get_height()
        self.imagen = pygame.transform.scale(imagem, (int(largura * escala), int(altura * escala)))
        self.rect = self.imagen.get_rect()
        self.rect.topleft = (x, y)
        self.clicou = False
    def draw(self):
        clicou = False
        posmouse = pygame.mouse.get_pos()
        if self.rect.collidepoint(posmouse):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                clicou = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        janela.blit(self.image, (self.rect.x, self.rect.y))
        return clicou

start_botao = botao(100, 200, start_img, 0.8)
exit_botao = botao(450, 200, exit_img, 0.8)


#Classe de bolinhas
class Notas(pygame.sprite.Sprite):
    def __init__(self, cor):        
        pygame.sprite.Sprite.__init__(self)
        self.image = assets[cor]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 935
        self.rect.y = -12.5
        self.speedy = 5
    
    def update(self):
        self.rect.y += self.speedy
    
clock = pygame.time.Clock()
todas_as_notas = pygame.sprite.Group()
FPS = 30

#Estrutura para tocar a música
pygame.mixer.music.load('song1.mp3') #Carrega a música
pygame.mixer.music.set_volume(1) #o volume vai de 0 a 1
pygame.mixer.music.play()

game = True
move = Notas('amarelo')

# Loop
while game: 
    clock.tick(FPS)
    janela.fill((202,228,241))
    if main_menu == True:
        if start_botao.draw():
            main_menu = False
        if exit_botao.draw():
            game = False
    else:
# Eventos
        for event in pygame.event.get():
            # Para sair

            if event.type == pygame.QUIT:
                game = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == tecla_verde:
                    verde = (122, 255, 122)
                if event.key == tecla_vermelha:
                    vermelho = (255,122,122)
                if event.key == tecla_amarela:
                    amarelo = (255,255,122)
                if event.key == tecla_azul:
                    azul = (122,122,255)
                if event.key == tecla_laranja:
                    laranja = (255,0,122)   
        pygame.display.update()
            
        move.update()
        # Saídas
        janela.fill((0, 0, 0))

        # Bolinhas
        bolinha_amarela = pygame.draw.circle(janela,amarelo,botao_amarelo,35)
        bolinha_vermelha = pygame.draw.circle(janela,vermelho,botao_vermelho,35)
        bolinha_verde = pygame.draw.circle(janela,verde,botao_verde,35)
        bolinha_azul = pygame.draw.circle(janela,azul,botao_azul,35)
        bolinha_laranja = pygame.draw.circle(janela,laranja,botao_laranja,35)

        #Cores
        verde = (0,255,0)
        vermelho = (255,0,0)
        amarelo = (255,255,0)        
        azul = (0,0,255)
        laranja = (255,122,0)
        branco = (255,255,255)
            

        janela.blit(move.image,move.rect)

        #Retas
        reta_direita = pygame.draw.line(janela,branco,(700,1080),(700,0)) 
        reta_esquerda = pygame.draw.line(janela,branco,(1220,1080),(1220,0)) 

        # Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador

# Finalização
pygame.quit()