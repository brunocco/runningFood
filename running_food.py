import pygame, os
from random import randint
from pygame.locals import *

#definindo diretórios
diretorio = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio, "imagens")
diretorio_sons = os.path.join(diretorio, "sons")

#inicializando biblioteca pygame e variáveis
pygame.init()
velocidade_personagem = 1
velocidade_carros = 3
cont_vidas = 3

#nome do jogo
pygame.display.set_caption("Running Food")

#definindo janela
largura = 800
altura = 617
janela = pygame.display.set_mode((largura, altura))

#construção do tempo em tela
relogio = pygame.time.Clock()
fonte_texto = pygame.font.SysFont('Comic Sans', 30)
cont = 120
texto = fonte_texto.render("TIME: "+str(cont), True, (0, 0, 0))
tempo = pygame.USEREVENT+1
pygame.time.set_timer(tempo, 1000)

#posição inicial dos carros que vão para direita
pos_x_azul1 = 0
pos_x_vermelho1 = 0
pos_x_azul2 = -100
pos_x_verde1 = -200

#posição inicial dos carros que vão para esquerda
pos_x_verde2 = 800
pos_x_vermelho2 = 800
pos_x_vermelho3 = 1200
pos_x_azul3 = 1400

#posição inicial dos carros em y
pos_y = 293

#posição dos barramentos no cenário
pos_cenario_x = 0
pos_cenario_y = 450
pos_cenario_y2 = 142
pos_cenario_x2 = 168
pos_cenario_y3 = 125
pos_cenario_x3 = 325
pos_cenario_x4 = 420
pos_cenario_x5 = 600
pos_cenario_x6 = 680

#posição das casas
pos_y_casas = 130
pos_x_casa1 = 120
pos_x_casa2 = 370
pos_x_casa3 = 635

#contadores de casas entregues
cont_casa1 = 0
cont_casa2 = 0
cont_casa3 = 0
cont_total = 0

#imagens do personagem e do cenário
cenario = pygame.image.load(os.path.join(diretorio_imagens, "cenario.png")).convert_alpha()
sprites = pygame.image.load(os.path.join(diretorio_imagens, "sprites.png")).convert_alpha()

#carros para direita
carro1 = pygame.image.load(os.path.join(diretorio_imagens, "carro1.png")).convert_alpha()
carro2 = pygame.image.load(os.path.join(diretorio_imagens, "carro2.png")).convert_alpha()
carro3 = pygame.image.load(os.path.join(diretorio_imagens, "carro3.png")).convert_alpha()

#carros para esquerda
carro4 = pygame.image.load(os.path.join(diretorio_imagens, "carro4.png")).convert_alpha()
carro5 = pygame.image.load(os.path.join(diretorio_imagens, "carro5.png")).convert_alpha()
carro6 = pygame.image.load(os.path.join(diretorio_imagens, "carro6.png")).convert_alpha()

#vidas
cheio3 = pygame.image.load(os.path.join(diretorio_imagens, "3cheio.png")).convert_alpha()
cheio2 = pygame.image.load(os.path.join(diretorio_imagens, "2cheio.png")).convert_alpha()
cheio1 = pygame.image.load(os.path.join(diretorio_imagens, "1cheio.png")).convert_alpha()
vazio = pygame.image.load(os.path.join(diretorio_imagens, "3vazio.png")).convert_alpha()

#tela de fim de jogo
fim = pygame.image.load(os.path.join(diretorio_imagens, "gameover.png")).convert_alpha()

#tela de parabéns
venceu =  pygame.image.load(os.path.join(diretorio_imagens, "venceu.png")).convert_alpha()

#sons presentes no jogo
som_fundo = pygame.mixer.music.load(os.path.join(diretorio_sons, "musica_fundo.mp3"))#música principal
pygame.mixer.music.play(-1)
batida_carro = pygame.mixer.Sound(os.path.join(diretorio_sons, "batida.mp3"))#efeitos sonoros
casa_ok = pygame.mixer.Sound(os.path.join(diretorio_sons, "casa_ok.mp3"))
win = pygame.mixer.Sound(os.path.join(diretorio_sons, "win.mp3"))

#inicializar personagem
class Personagem:
    def __init__(self, pos_x, pos_y, x, y, largura, altura):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.pos_x = pos_x
        self.pos_y = pos_x

#matriz das sprites do personagem e sprite inicial
posicao = [[0, 0, 44, 44], [0, 44, 44, 88], [0, 88, 44, 132], [0, 132, 44, 176]]
sprite = posicao[2]

#posição inicial do personagem
entregador = Personagem(0, 0, 595, 550, 44, 44)

#função para definir como e onde vai aparecer as imagens em tela
def mask_blit(janela, img, sprite, x, y):
    surf = pygame.Surface((44, 44)).convert()
    surf.blit(img, (0,0), (sprite[0], sprite[1], sprite[2], sprite[3]))
    surf.set_colorkey((0,0,0))
    janela.blit(surf, (x,y))

#função de controle do personagem
def controle(obj):
    global sprite
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP] and obj.y > 0:
        obj.y -= velocidade_personagem
        sprite = posicao[3]
    if comandos[pygame.K_DOWN] and obj.y < altura - obj.altura:
        obj.y += velocidade_personagem
        sprite = posicao[0]
    if comandos[pygame.K_RIGHT] and obj.x < largura - obj.largura:
        obj.x += velocidade_personagem
        sprite = posicao[2]
    if comandos[pygame.K_LEFT] and obj.x > 0:
        obj.x -= velocidade_personagem
        sprite = posicao[1]

#looping para o jogo funcionar até ser clicado no x (quit)
jogo = True
while jogo:

    relogio.tick(60)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogo = False
            pygame.quit()
            exit()
        elif evento.type == tempo: #relógio
            cont -= 1
            texto = fonte_texto.render("TIME: "+str(cont), True, (0, 0, 0))
            if cont == -1:
                pygame.time.set_timer(tempo, 0)
                break

    janela.blit(cenario, (0,0))

    janela.blit(cheio3, (7, 17))

    janela.blit(texto, (700, 17))

    controle(entregador)

    mask_blit(janela, sprites, sprite, entregador.x, entregador.y)

    #mudanças da vida
    if cont_vidas == 2:
        janela.blit(cheio2, (7, 17))
    if cont_vidas == 1:
        janela.blit(cheio1, (7, 17))
    if cont_vidas == 0:
        janela.blit(vazio, (7, 17))

    #colocar os carros na tela
    janela.blit(carro1,(pos_x_azul1, pos_y+65))
    janela.blit(carro2,(pos_x_vermelho1, pos_y-50))
    janela.blit(carro1,(pos_x_azul2, pos_y-50))
    janela.blit(carro3,(pos_x_verde1, pos_y+65))
    janela.blit(carro4,(pos_x_azul3, pos_y+112))
    janela.blit(carro5,(pos_x_vermelho2, pos_y+112))
    janela.blit(carro6,(pos_x_verde2, pos_y))
    janela.blit(carro5,(pos_x_vermelho3, pos_y))

    #movimentação dos carros
    pos_x_azul1 += velocidade_carros #direita
    pos_x_vermelho1 += velocidade_carros
    pos_x_azul2 += velocidade_carros
    pos_x_verde1 += velocidade_carros 
    pos_x_verde2 -= velocidade_carros #esquerda
    pos_x_vermelho2 -= velocidade_carros
    pos_x_vermelho3 -= velocidade_carros
    pos_x_azul3 -= velocidade_carros

    #detecta colisão com os carros indo para a direita
    if(entregador.x+44 > pos_x_azul1) and (entregador.x < pos_x_azul1+55) and (entregador.y+44 > pos_y+65)  and (entregador.y < pos_y+65+30):
        batida_carro.play()
        entregador.x = 595
        entregador.y = 550
        cont_vidas -= 1
    if(entregador.x+44 > pos_x_azul2) and (entregador.x < pos_x_azul2+55) and (entregador.y+44 > pos_y-50)  and (entregador.y < pos_y-50+30):
        batida_carro.play()
        entregador.x = 595
        entregador.y = 550
        cont_vidas -= 1
    if(entregador.x+44 > pos_x_vermelho1) and (entregador.x < pos_x_vermelho1+55) and (entregador.y+44 > pos_y-50)  and (entregador.y < pos_y-50+30):
        batida_carro.play()
        entregador.x = 595
        entregador.y = 550
        cont_vidas -= 1
    if(entregador.x+44 > pos_x_verde1) and (entregador.x < pos_x_verde1+55) and (entregador.y+44 > pos_y+65)  and (entregador.y < pos_y+65+30):
        batida_carro.play()
        entregador.x = 595
        entregador.y = 550
        cont_vidas -= 1
    
    #detecta colisão com os carros indo para a esquerda
    if(entregador.x+44 > pos_x_verde2) and (entregador.x < pos_x_verde2+55) and (entregador.y+44 > pos_y)  and (entregador.y < pos_y+30):
        batida_carro.play()
        entregador.x = 595
        entregador.y = 550
        cont_vidas -= 1
    if(entregador.x+44 > pos_x_vermelho3) and (entregador.x < pos_x_vermelho3+55) and (entregador.y+44 > pos_y)  and (entregador.y < pos_y+30):
        batida_carro.play()
        entregador.x = 595
        entregador.y = 550
        cont_vidas -= 1
    if(entregador.x+44 > pos_x_vermelho2) and (entregador.x < pos_x_vermelho2+55) and (entregador.y+44 > pos_y+112)  and (entregador.y < pos_y+112+30):
        batida_carro.play()
        entregador.x = 595
        entregador.y = 550
        cont_vidas -= 1
    if(entregador.x+44 > pos_x_azul3) and (entregador.x < pos_x_azul3+55) and (entregador.y+44 > pos_y+112) and (entregador.y < pos_y+112+30):
        batida_carro.play()
        entregador.x = 595
        entregador.y = 550
        cont_vidas -= 1
    
    #sorteio das posições para toda vez que iniciar o jogo a movimentação dos carros ser diferente
    if (pos_x_vermelho1 >= 1000) and (pos_x_azul1 >= 1000) and (pos_x_azul2 >= 1000) and (pos_x_verde1 >= 1000):#direita
        pos_x_azul1 = randint(-1000, 0)
        pos_x_azul2 = randint(-1400, -1100)
        pos_x_vermelho1 = randint(-1000, 0)
        pos_x_verde1 = randint(-1400, -1100)

    if (pos_x_verde2 <= -100) and (pos_x_vermelho2 <= -100) and (pos_x_vermelho3 <= -100) and (pos_x_azul3 <= -100):#esquerda
        pos_x_verde2 = randint(800, 1000)
        pos_x_vermelho3 = randint(1500, 2000)
        pos_x_vermelho2 = randint(800, 1000)
        pos_x_azul3 = randint(1500, 2000)

    #barramentos do cenário
    if (entregador.x+44 > pos_cenario_x) and (entregador.x < pos_cenario_x+582) and (entregador.y+44 > pos_cenario_y) and (entregador.y < pos_cenario_y+162): #cenário de baixo
        entregador.y -= 1
        entregador.x += 1
    if (entregador.x+44 > pos_cenario_x) and (entregador.x < pos_cenario_x+115) and (entregador.y+44 > pos_cenario_y2) and (entregador.y < pos_cenario_y2+90): #cenário de cima 1
        entregador.y += 1
        entregador.x += 1
    if (entregador.x+44 > pos_cenario_x2) and (entregador.x < pos_cenario_x2+198) and (entregador.y+44 > pos_cenario_y2) and (entregador.y < pos_cenario_y2+90): #cenário de cima 2
        entregador.y += 1
        entregador.x -= 1
    if (entregador.x+44 > pos_cenario_x3) and (entregador.x < pos_cenario_x3+42) and (entregador.y+44 > pos_cenario_y3) and (entregador.y < pos_cenario_y3+90):
        entregador.x += 1
    if (entregador.x+44 > pos_cenario_x4) and (entregador.x < pos_cenario_x4+200) and (entregador.y+44 > pos_cenario_y2) and (entregador.y < pos_cenario_y2+90): #cenário de cima 3
        entregador.y += 1
        entregador.x -= 1
    if (entregador.x+44 > pos_cenario_x5) and (entregador.x < pos_cenario_x5+30) and (entregador.y+44 > pos_cenario_y2) and (entregador.y < pos_cenario_y2+87):
        entregador.x += 1
    if (entregador.x+44 > pos_cenario_x6) and (entregador.x < pos_cenario_x6+133) and (entregador.y+44 > pos_cenario_y2) and (entregador.y < pos_cenario_y2+90): #cenário de cima 4
        entregador.y += 1
        entregador.x -= 1

    #locais de entrega
    if (entregador.x+44 > pos_x_casa1) and (entregador.x < pos_x_casa1+35) and (entregador.y+44 > pos_y_casas) and (entregador.y < pos_y_casas) and (cont_casa1 == 0): # casa 1
        casa_ok.play()
        cont_casa1 += 1
        cont_total +=1
    elif (entregador.x+44 > pos_x_casa2) and (entregador.x < pos_x_casa2+35) and (entregador.y+44 > pos_y_casas) and (entregador.y < pos_y_casas) and (cont_casa2 == 0): # casa 2
        casa_ok.play()
        cont_casa2 += 1
        cont_total +=1
    elif (entregador.x+44 > pos_x_casa3) and (entregador.x < pos_x_casa3+35) and (entregador.y+44 > pos_y_casas) and (entregador.y < pos_y_casas) and (cont_casa3 == 0): # casa 3
        casa_ok.play()
        cont_casa3 += 1
        cont_total +=1
    elif(entregador.y+44 > pos_y_casas) and (entregador.y < pos_y_casas):
        entregador.y += 1

    #congratulations ou game over
    if cont_total == 3:
        janela.blit(venceu, (0,0))
        jogo == False
        pygame.mixer.music.stop()
        win.play()
    elif (cont == -1) or (cont_vidas == 0):
        janela.blit(fim, (0,0))
        jogo == False
        pygame.mixer.music.stop()

    pygame.display.flip()