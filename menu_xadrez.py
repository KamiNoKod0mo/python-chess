import pygame,sys
from settings import Confs
from xadrez import play


def main_menu():
    pygame.init()
    confs = Confs()

    screen = pygame.display.set_mode((confs.screen_width, confs.screen_height))  # Tela externa
    pygame.display.set_caption("Chess")  # Título
    screen.blit(confs.bg,(0,0))# tela de fundo

    menu(screen,confs)
    global pw_rect
    global pb_rect
    global button_rect

    global select_color
    select_color = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:#envento de click
                posicao_mouse = pygame.mouse.get_pos()
                #posicao_mouse = (posicao_mouse[0],posicao_mouse[1])
                if button_rect.collidepoint(posicao_mouse):
                    running = False
                #In the future
                """ if pb_rect.collidepoint(posicao_mouse):
                    menu(screen,confs)
                    pygame.draw.circle(screen,(255,0,0),(557,470),10)
                    pygame.display.update()
                    select_color = 1
                if pw_rect.collidepoint(posicao_mouse):
                    menu(screen,confs)
                    pygame.draw.circle(screen,(255,0,0),(440,470),10)
                    pygame.display.update()
                    select_color = 0 """
    return 1


def menu(screen,confs):
    screen.blit(confs.bg,(0,0))# tela de fundo
    ###In the future
    """ pw = pygame.image.load("/home/carlos_/Desktop/Projects/Python/Games/xadrez/imagens/pawnW.png")
    pw = pygame.transform.scale(pw,(60,60))
    global pw_rect
    pw_rect = pygame.Rect(410,400,60,60)
    screen.blit(pw,(410,400))
    #
    pb = pygame.image.load("/home/carlos_/Desktop/Projects/Python/Games/xadrez/imagens/pawnB.png")
    pb = pygame.transform.scale(pb,(60,60))
    global pb_rect
    pb_rect = pygame.Rect(525,400,60,60)
    screen.blit(pb,(525,400)) """
    ###
    # Butão de play
    global button_rect
    button_rect = pygame.Rect(345, 320, confs.screen_width-700, confs.screen_height-630)
    screen.blit(confs.button,(345,250))

    pygame.display.flip()


def play_music():
    pygame.mixer.init()  # Inicialize o mixer do Pygame
    pygame.mixer.music.load('/home/carlos_/Desktop/Projects/Python/Games/xadrez/musics/neon-gaming.mp3')  # Carregue o arquivo de música desejado

    pygame.mixer.music.set_volume(0.5)

    pygame.mixer.music.play(loops=-1)  # Inicie a reprodução da música

    # Aguarde até que a música termine de tocar

