#============= Estados para a troca de telas =============#
INIT = 0
MUSICA = 1
GAME = 2
GANHOU = 3
QUIT = 4
PERDEU = 5

#======= variáveis e dimensões =======#
width = 800
height = 600

fps = 60

branco = (255,255,255)
verde = (0,255,0)
vermelho = (255,0,0)
amarelo = (255,255,0)
azul = (0,0,255)
laranja = (255,122,0)
transparente = (0,0,0,0)

terco = int(width/3)
sexto = int(terco/6)

linha_e_i = (terco, 0)
linha_e_f = (terco, height)

linha_d_i = (2*terco, 0)
linha_d_f = (2*terco, height)

y_teclas = int(height * 15/17)


#========== Dicionário com o tempo de parada para as musicas ==========#
dicio = {'assets/musicas/riptide_vance-joy.mp3':200, 'assets/musicas/grapejuice-harry.mp3':190, 'assets/musicas/jose_gonzalez-killing_for_love.mp3':181, 'assets/musicas/clairo_flamin-hot-cheetos.mp3':125, 'assets/musicas/a-drowning_how-to-destroy-angels.mp3':391, 'assets/musicas/eyen_plaid.mp3':260}

