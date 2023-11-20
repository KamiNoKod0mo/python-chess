import pygame, sys
from settings import Confs, PartsW, PartsB
from functions import *
import threading
from menu_xadrez import *


def play():
    # Inicio
    pygame.init()
    confs = Confs()

    Wpeaces = PartsW()
    Bpeaces = PartsB()

    screen = pygame.display.set_mode((confs.screen_width,confs.screen_height))#externa
    screeni = pygame.Surface((confs.screeni_width,confs.screeni_height))# interna

    pygame.display.set_caption("Chess")#titulo

    
    screeni.fill(confs.colori)#cor interna
    screen.fill(confs.color)#cor externa

    #Lugar da tela interna
    screeni_rect = screeni.get_rect()
    screeni_rect.center = (confs.screen_width / 2, confs.screen_height / 2)

    create_tabu(screeni,confs)
    w = peaces(Wpeaces,2,1,'w',)
    b = peaces(Bpeaces,7,8,'b')
    w.draw_peace(screeni,'w',screen,w,b)
    b.draw_peace(screeni,'b',screen,w,b)
    
    while True:
        if confs.game == 0:
            available_po(w,b,screeni,confs)
            checkW(w,b,screeni,confs)
            checkB(w,b,screeni,confs)
            #print(w.coordPe) 
            #print(b.coordPc) 
            if confs.t == 1:
                select(screeni,confs,w,w,b)
                #print('white')
            
            if confs.t == -1:
                select(screeni,confs,b,w,b)
                #print('black')
        
            w.draw_peace(screeni,'w',screen,w,b)
            b.draw_peace(screeni,'b',screen,w,b)
        else:
            if check_mate(confs.game,screeni,confs):
                if main_menu():
                    play()
                confs.game=0
        
        updateT(screeni,screen,confs,screeni_rect,w,b)


if __name__ == "__main__":
    x = threading.Thread(target=play_music, args=())
    x.daemon = True
    x.start()
    if main_menu():
        play()

