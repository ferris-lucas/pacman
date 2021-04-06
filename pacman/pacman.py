import pygame

AMARELO = (255, 255, 0)
PRETO = (0,0,0)
VELOCIDADE = 1.0
RAIO = 30

pygame.init()

tela = pygame.display.set_mode((640,480), 0)
x = 10
y = 10
vel_x = VELOCIDADE
vel_y = VELOCIDADE

while True:

    # Parte 1: Calcula as regras
    x = x + vel_x
    if x + RAIO > 640:
        vel_x = -VELOCIDADE
    if x - RAIO < 0:
        vel_x = VELOCIDADE

    y = y + vel_y
    if y + RAIO > 480:
        vel_y = -VELOCIDADE
    if y - RAIO < 0:
        vel_y = VELOCIDADE


    # Parte 2: Pintar tela
    tela.fill(PRETO)
    pygame.draw.circle(tela, AMARELO, (int(x), int(y)), RAIO, 0)
    pygame.display.update()


    # Parte 3: Eventos do jogo
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()