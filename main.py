import pygame

pygame.init()

window = pygame.display.set_mode([1280, 720])
title = pygame.display.set_caption("Football Pong")

score1 = 0
score1_img = pygame.image.load("assets/score/0.png")
score2 = 0
score2_img = pygame.image.load("assets/score/0.png")

win = pygame.image.load("assets/win.png")

field = pygame.image.load("assets/field.png")

player1 = pygame.image.load("assets/player1.png")
player1_y = 310
player1_moveup = False
player1_movedown = False

player2 = pygame.image.load("assets/player2.png")
player2_x = 310
player2_moveup = False 
player2_movedown = False

ball = pygame.image.load("assets/ball.png")
ball_x = 617
ball_y = 337
ball_dir = -3 # DIREÇÃO DA BOLA
ball_dir_y = 1

# FUNÇÃO PARA A MOVIMENTAÇÃO DO PLAYER 1
def move_playeer1():
    global player1_y

    if player1_moveup:
        player1_y -= 5
    else:
        player1_y += 0

    if player1_movedown:
        player1_y += 5
    else:
        player1_y += 0

    # LIMITANDI A MOVIMENTAÇÃO
    if player1_y <= 0:
        player1_y = 0
    elif player1_y >= 575:
        player1_y = 575

# FUNÇÃO PARA A MOVIMENTAÇÃO DO PLAYER 2 JOGAVEL
def move_playeer2():
    global player2_x

    if player2_moveup:
        player2_x -=5
    else:
        player2_x += 0

    if player2_movedown:
        player2_x += 5
    else:
        player2_x += 0

    # LIMITE DE MOVIMENTAÇÃO
    if player2_x <= 0:
        player2_x = 0
    elif player2_x >= 575:
        player2_x = 575



# O PLAYER 2 VAI ACOMPANHAR A POSIÇÃO DA BOLA (BOT)
'''
def move_playeer2():
    global player2_x
    player2_x = ball_y
'''

# FUNÇÃO PARA A MOVIMENTAÇÃO DA BOLA
def move_ball():
    global ball_x
    global ball_y
    global ball_dir
    global ball_dir_y
    global score1
    global score2
    global score2_img
    global score1_img

    ball_x += ball_dir
    ball_y += ball_dir_y


    if ball_x < 125:
        if player1_y < ball_y + 23:
            if player1_y + 146 > ball_y:
                ball_dir *= -1

    if ball_x > 1105:
        if player2_x < ball_y + 23:
            if player2_x + 146 > ball_y:
                ball_dir *= -1

    
    if ball_y > 670:
        ball_dir_y *= -1
    elif ball_y <= 0:
        ball_dir_y *= -1

    if ball_x < - 50:
        ball_x = 617
        ball_y = 337
        ball_dir_y *= -1
        ball_dir *= -1
        score2 += 1
        score2_img = pygame.image.load("assets/score/" + str(score2) + ".png")


    elif ball_x > 1320:
        ball_x = 617
        ball_y = 337
        ball_dir_y *= -1
        ball_dir *= -1
        score1 += 1
        score1_img = pygame.image.load("assets/score/" + str(score1) + ".png")


# MOSTRAR AS IMAGENS EM SUAS POSIÇÕES
def draw():
    if score1 or score2 < 9:
        window.blit(field, (0, 0))
        window.blit(player1, (50, player1_y))
        window.blit(player2, (1150, player2_x))
        window.blit(ball, (ball_x, ball_y))
        window.blit(score1_img, (500, 50))
        window.blit(score2_img, (710, 50))
        move_ball() # CHAMA A FUNÇÃO MOVEL BOLA
        move_playeer1() # CHAMA A FUNÇÃO MOVER PLAYER 1
        move_playeer2() # CHAMA A FUNÇÃO MOVE PLAYER 2

    else:
        window.blit(win, (300, 330))

# LAÇO PARA ENQUANTO O RODO ESTIVER RODADNDO
loop = True
while loop:

    # PARA PODE FECHAR O EXECUTAVEL NO X
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False

        #MOVIMENTAÇÃO DO PLLAYER 1

        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_w:
                player1_moveup = True
            if events.key == pygame.K_s:
                player1_movedown = True
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_w:
                player1_moveup = False
            if events.key == pygame.K_s:
                player1_movedown = False

        # MOVIMENTAÇÃO DO PLAYER 2

        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_i:
                player2_moveup = True
            if events.key == pygame.K_k:
                player2_movedown = True
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_i:
                player2_moveup = False
            if events.key == pygame.K_k:
                player2_movedown = False
        
    draw() # CHAMA FUNÇÃO DRAW
   

    pygame.display.update()
