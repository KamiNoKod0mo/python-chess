import pygame,sys, settings,time
from settings import *


#Variaveis
#global listabc,houses
listabc = ['a','b','c','d','e','f','g','h']
houses = {}

avaible_move_dictW={}
avaible_move_dictB={}
check_w = 0
check_b = 0

#global capeaceCb,capeaceEb
capeaceCb,capeaceEb = {},{}

#global capeaceCw,capeaceEw
capeaceCw,capeaceEw  = {},{}
#
peca = []
pecaB = []
####

#Faz update da das telas
def updateT(screeni,screen,confs,screeni_rect,w,b):
    screen.blit(confs.bg,(0,0))# tela de fundo
    screen.blit(screeni,screeni_rect) #  tela interior
    #coords
    cordsT(screen,confs.colorT,confs.font,w,b)#Escreve na tela

    pygame.display.flip()#Atualiza a tela
  
    
def create_tabu(screeni,confs):
    # Variavel reesetada no updateP para atualizar a posição do jogo
    
    c = 0
    color = (0, 255, 0)
    rects = []
    
    for i in range(8):# linha
        c -= 1 # para permanecer na cor anterior
        for j in range(8): # coluna
            if c % 2 == 0:#alterna cor
                color = (25, 50, 25)
            else:
                color = (0, 255, 0)

            rect = pygame.Rect(j * 75, i * 75, 75, 75) #Coodernadas
            co = pygame.draw.rect(screeni, color, rect)#DEsenha retangolo
            rects.append((co.x,co.y))#desenhar

            c = c + 1# contator para controlar a cor e parada
            

    #Outros valores inicias, Guarda o X e Y dos quadradoss em um dicionaio com as sua casas respectivas
    index = 0
    for number in "87654321":
        for num in range(0,8):#Para letras
            houses[listabc[num]+number] = rects[index] # associar uma coodernada a uma casa e armazena
            #print(rects[index])
            index += 1 # Controla onde no dicionaario sera guardado(64)


def cordsT(screen,color,font,w,b):#Escreve na tela
    y = 75
    ppc = 50
    ppe = 50
    ppx =50
    ppy =50
    pca =[]
    for i in range(8,0,-1):
        textn = font.render(str(i),True,color)
        textn_pos = (175,y)
        textn_rect = textn.get_rect()
        y+=75
        screen.blit(textn,textn_pos)
    x =225
    for a in range(0,8):
        texta = font.render(listabc[a],True,color)
        #print(listabc[a])
        texta_pos = (x,660)
        texta_rect = texta.get_rect()
        x += 75
        screen.blit(texta,texta_pos)
    #print(capeaceCb)
    
    if capeaceCb != {}:
        try:
            for xc in range(8):
                if b.peacesC[int(list(capeaceCb.values())[xc])] not in pca:
                    b.peacesC[int(list(capeaceCb.values())[xc])] = pygame.transform.scale(b.peacesC[int(list(capeaceCb.values())[xc])],(20,20))
                #pygame.transform.scale(b.peacesC[int(list(capeaceCb.values())[x])],(20,20))
                    screen.blit(b.peacesC[int(list(capeaceCb.values())[xc])],(ppc,500))
                    pca.append(b.peacesC[int(list(capeaceCb.values())[xc])])
                    ppc = ppc +10
        except:
            pass
        ###########
    if capeaceEb !={}:
        
        try:
            #print(b.peacesE,'---',capeaceEb.values())
            for xe in range(8):
                                    
                if b.peacesE[int(list(capeaceEb.values())[xe])] not in pca:
                    #print(b.peacesE, '----', capeaceEb)
                    b.peacesE[int(list(capeaceEb.values())[xe])] = pygame.transform.scale(b.peacesE[int(list(capeaceEb.values())[xe])],(20,20))
                #pygame.transform.scale(b.peacesC[int(list(capeaceCb.values())[x])],(20,20))
                    screen.blit(b.peacesE[int(list(capeaceEb.values())[xe])],(ppe,530))
                    pca.append(b.peacesE[int(list(capeaceEb.values())[xe])])
                    ppe = ppe +10
        except:
            pass
        #####
    if capeaceCw != {}:
        try:
            for xc in range(8):
                if w.peacesC[int(list(capeaceCw.values())[xc])] not in pca:
                    w.peacesC[int(list(capeaceCw.values())[xc])] = pygame.transform.scale(w.peacesC[int(list(capeaceCw.values())[xc])],(20,20))
                #pygame.transform.scale(b.peacesC[int(list(capeaceCb.values())[x])],(20,20))
                    screen.blit(w.peacesC[int(list(capeaceCw.values())[xc])],(ppx,100))
                    pca.append(w.peacesC[int(list(capeaceCw.values())[xc])])
                    ppx = ppx +10
        except:
            pass
        ###########
    if capeaceEw !={}:
        #print(capeaceEw)
        try:
            #print(b.peacesE,'---',capeaceEb.values())
            for xe in range(8):
                                    
                if w.peacesE[int(list(capeaceEw.values())[xe])] not in pca:
                    #print(b.peacesE, '----', capeaceEb)
                    w.peacesE[int(list(capeaceEw.values())[xe])] = pygame.transform.scale(w.peacesE[int(list(capeaceEw.values())[xe])],(20,20))
                #pygame.transform.scale(b.peacesC[int(list(capeaceCb.values())[x])],(20,20))
                    screen.blit(w.peacesE[int(list(capeaceEw.values())[xe])],(ppy,70))
                    pca.append(w.peacesE[int(list(capeaceEw.values())[xe])])
                    ppy = ppy +10
        except:
            pass
            
        
######Funções auxiliares#############

def get_key_by_value(dicionario, valor):#Pega a chave com base non valor
    for chave, valor_dicionario in dicionario.items():
        if valor_dicionario == valor:
            return chave
    return None


def get_prev_mullti(n):# Pega o valor no mouse e diminu ate encontrar um multiplo de 75
    for i in range(n, 0, -1):
        if i % 75 == 0:
            return i

    return 0


def conv(key):#Converte casa(key) do dicionario houses na coordenada da mesma
    #print(houses[key])
    return houses[key]


def chenge_turn(confs):
    confs.t = confs.t * -1


def check_pos_moveDW(ho,reiw,w,b):
    global bw
    bw =0
    lae = []
    lad = []
    lup = []
    ldw = []

    elae = []
    elad = []
    elup = []
    eldw = []
    
    peca = '' 
    linha = 0
    try:
        if ((w.coordPc.get(ho)) in list(avaible_move_dictB.get('qb0')) and (w.coordPc.get(ho))[1] == reiw[1] and (w.coordPc.get(ho))[1] == list(b.coordPe.get('qb0'))[1]) or ((w.coordPe.get(ho)) in list(avaible_move_dictB.get('qb0')) and (w.coordPe.get(ho))[1] == reiw[1] and (w.coordPe.get(ho))[1] == list(b.coordPe.get('qb0'))[1]) or ((w.coordPc.get(ho)) in list(avaible_move_dictB.get('qb0')) and (w.coordPc.get(ho))[0] == reiw[0] and (w.coordPc.get(ho))[0] == list(b.coordPe.get('qb0'))[0]) or ((w.coordPe.get(ho)) in list(avaible_move_dictB.get('qb0')) and (w.coordPe.get(ho))[0] == reiw[0] and (w.coordPe.get(ho))[0] == list(b.coordPe.get('qb0'))[0]):
            linha =1
            peca = 'qb0'
    except:
        pass
    try:
        if ((w.coordPc.get(ho)) in list(avaible_move_dictB.get('qb1')) and (w.coordPc.get(ho))[1] == reiw[1] and (w.coordPc.get(ho))[1] == list(b.coordPe.get('qb1'))[1]) or ((w.coordPe.get(ho)) in list(avaible_move_dictB.get('qb1')) and (w.coordPe.get(ho))[1] == reiw[1] and (w.coordPe.get(ho))[1] == list(b.coordPe.get('qb1'))[1]) or ((w.coordPc.get(ho)) in list(avaible_move_dictB.get('qb1')) and (w.coordPc.get(ho))[0] == reiw[0] and (w.coordPc.get(ho))[0] == list(b.coordPe.get('qb1'))[0]) or ((w.coordPe.get(ho)) in list(avaible_move_dictB.get('qb1')) and (w.coordPe.get(ho))[0] == reiw[0] and (w.coordPe.get(ho))[0] == list(b.coordPe.get('qb1'))[0]):
            linha =1
            peca = 'qb1'
    except:
        pass
    try:
        if ((w.coordPc.get(ho)) in list(avaible_move_dictB.get('qb2')) and (w.coordPc.get(ho))[1] == reiw[1] and (w.coordPc.get(ho))[1] == list(b.coordPe.get('qb2'))[1]) or ((w.coordPe.get(ho)) in list(avaible_move_dictB.get('qb2')) and (w.coordPe.get(ho))[1] == reiw[1] and (w.coordPe.get(ho))[1] == list(b.coordPe.get('qb2'))[1]) or ((w.coordPc.get(ho)) in list(avaible_move_dictB.get('qb2')) and (w.coordPc.get(ho))[0] == reiw[0] and (w.coordPc.get(ho))[0] == list(b.coordPe.get('qb2'))[0]) or ((w.coordPe.get(ho)) in list(avaible_move_dictB.get('qb2')) and (w.coordPe.get(ho))[0] == reiw[0] and (w.coordPe.get(ho))[0] == list(b.coordPe.get('qb2'))[0]):
            linha =1
            peca = 'qb2'
    except:
        pass
    try:
        if ((w.coordPc.get(ho)) in list(avaible_move_dictB.get('qb3')) and (w.coordPc.get(ho))[1] == reiw[1] and (w.coordPc.get(ho))[1] == list(b.coordPe.get('qb3'))[1]) or ((w.coordPe.get(ho)) in list(avaible_move_dictB.get('qb3')) and (w.coordPe.get(ho))[1] == reiw[1] and (w.coordPe.get(ho))[1] == list(b.coordPe.get('qb3'))[1]) or ((w.coordPc.get(ho)) in list(avaible_move_dictB.get('qb3')) and (w.coordPc.get(ho))[0] == reiw[0] and (w.coordPc.get(ho))[0] == list(b.coordPe.get('qb3'))[0]) or ((w.coordPe.get(ho)) in list(avaible_move_dictB.get('qb3')) and (w.coordPe.get(ho))[0] == reiw[0] and (w.coordPe.get(ho))[0] == list(b.coordPe.get('qb3'))[0]):
            linha =1
            peca = 'qb3'
    except:
        pass
    try:
        if ((w.coordPc.get(ho)) in list(avaible_move_dictB.get('qb4')) and (w.coordPc.get(ho))[1] == reiw[1] and (w.coordPc.get(ho))[1] == list(b.coordPe.get('qb4'))[1]) or ((w.coordPe.get(ho)) in list(avaible_move_dictB.get('qb4')) and (w.coordPe.get(ho))[1] == reiw[1] and (w.coordPe.get(ho))[1] == list(b.coordPe.get('qb4'))[1]) or ((w.coordPc.get(ho)) in list(avaible_move_dictB.get('qb4')) and (w.coordPc.get(ho))[0] == reiw[0] and (w.coordPc.get(ho))[0] == list(b.coordPe.get('qb4'))[0]) or ((w.coordPe.get(ho)) in list(avaible_move_dictB.get('qb4')) and (w.coordPe.get(ho))[0] == reiw[0] and (w.coordPe.get(ho))[0] == list(b.coordPe.get('qb4'))[0]):
            linha =1
            peca = 'qb4'
    except:
        pass
    try:

        if ((w.coordPc.get(ho)) in list(avaible_move_dictB.get('tb0')) and (w.coordPc.get(ho))[1] == reiw[1] and (w.coordPc.get(ho))[1] == list(b.coordPe.get('tb0'))[1]) or ((w.coordPe.get(ho)) in list(avaible_move_dictB.get('tb0')) and (w.coordPe.get(ho))[1] == reiw[1] and (w.coordPe.get(ho))[1] == list(b.coordPe.get('tb0'))[1]) or ((w.coordPc.get(ho)) in list(avaible_move_dictB.get('tb0')) and (w.coordPc.get(ho))[0] == reiw[0] and (w.coordPc.get(ho))[0] == list(b.coordPe.get('tb0'))[0]) or ((w.coordPe.get(ho)) in list(avaible_move_dictB.get('tb0')) and (w.coordPe.get(ho))[0] == reiw[0] and (w.coordPe.get(ho))[0] == list(b.coordPe.get('tb0'))[0]):
            linha = 1
            peca = 'tb0'
    except:
        pass
    try:
        if ((w.coordPc.get(ho)) in list(avaible_move_dictB.get('tb1')) and (w.coordPc.get(ho))[1] == reiw[1] and (w.coordPc.get(ho))[1] == list(b.coordPe.get('tb1'))[1]) or ((w.coordPe.get(ho)) in list(avaible_move_dictB.get('tb1')) and (w.coordPe.get(ho))[1] == reiw[1] and (w.coordPe.get(ho))[1] == list(b.coordPe.get('tb1'))[1]) or ((w.coordPc.get(ho)) in list(avaible_move_dictB.get('tb1')) and (w.coordPc.get(ho))[0] == reiw[0] and (w.coordPc.get(ho))[0] == list(b.coordPe.get('tb1'))[0]) or ((w.coordPe.get(ho)) in list(avaible_move_dictB.get('tb1')) and (w.coordPe.get(ho))[0] == reiw[0] and (w.coordPe.get(ho))[0] == list(b.coordPe.get('tb1'))[0]):
            linha=1
            peca = 'tb1'
            #(w.coordPc.get(ho))[1] == reiw[1] and (w.coordPc.get(ho))[1] == list(b.coordPe.get('tb1'))[1]):
    except:
        pass
    try:
        if linha == 1:
            for count in w.coordPc.values():
                if count[1] == reiw[1]:
                    #print(ho)
                    if count[0] < reiw[0]:
                        lae.append(get_key_by_value(w.coordPc,(count[0],count[1])))
                        #print(ho)
                            
                    if count[0] > reiw[0]: 
                        lad.append(get_key_by_value(w.coordPc,(count[0],count[1])))

                if count[0] == reiw[0]:
                    if count[1] < reiw[1]:
                        lup.append(get_key_by_value(w.coordPc,(count[0],count[1])))
                    if count[1] > reiw[1]:
                        ldw.append(get_key_by_value(w.coordPc,(count[0],count[1])))
            #print(w.coordPc.get(ho), '---', lae)
            
            #print(ho,'--',len(lad) == 1 and ho in lad)

            w.coordPe_copy = w.coordPe.copy()
            del w.coordPe_copy['kw0']
    #(w.coordPc.get(ho))[1] == reiw[1] and (w.coordPc.get(ho))[1] == list(b.coordPe.get('tb1'))[1]):
        
            for count in w.coordPe_copy.values():
                #print(ho)
                if count[1] == reiw[1]:
                    #print(ho)
                    if count[0] < reiw[0]:
                        elae.append(get_key_by_value(w.coordPe,(count[0],count[1])))
                        #print(ho)
                            
                    if count[0] > reiw[0]: 
                        elad.append(get_key_by_value(w.coordPe,(count[0],count[1])))
                #
                if count[0] == reiw[0]:
                    if count[1] < reiw[1]:
                        elup.append(get_key_by_value(w.coordPe,(count[0],count[1])))
                    if count[1] > reiw[1]:
                        eldw.append(get_key_by_value(w.coordPe,(count[0],count[1])))
    except:
        pass
    
    if lad !=[] or lae != [] or lup != [] or ldw != [] or elad !=[] or elae != [] or elup != [] or eldw != []:
        if len(lad) == 1 and ho in lad and len(elad) ==0:
            bw = 1
        #print(elae)##
        if (len(lae) == 1 and ho in lae) and len(elae) ==0:
            bw = 1
        
        if len(lup) == 1 and ho in lup and len(elup) ==0:
            bw = 1
        if len(ldw) == 1 and ho in ldw and len(eldw) ==0:
            bw = 1

    #print(ho)
        if len(elad) == 1 and ho in elad and len(lad) ==0:
            bw = 1
        #print(elae, '---' ,len(lae))
        if len(elae) == 1 and ho in elae and len(lae) ==0:
            bw = 1
        
        if len(elup) == 1 and ho in elup and len(lup) ==0:
            bw = 1
        if len(eldw) == 1 and ho in eldw and len(ldw) ==0:
            bw = 1
        
        return peca
    peca_d = []
    try:
        if (w.coordPc.get(ho)) in list(avaible_move_dictB.get('bb1')) :
            peca_d =  list(avaible_move_dictB.get('bb1'))
            d_coord = list(b.coordPe.get('bb1'))
    except:
        pass
    try:
        if (w.coordPc.get(ho)) in list(avaible_move_dictB.get('bb0')):
            peca_d =  list(avaible_move_dictB.get('bb0'))
            d_coord = list(b.coordPe.get('bb0'))
    except:
        pass
    try:
        if (w.coordPc.get(ho)) in list(avaible_move_dictB.get('qb0')):
            peca_d =  list(avaible_move_dictB.get('qb0'))
            d_coord = list(b.coordPe.get('qb0'))
    except:
        pass
    try:
        if (w.coordPc.get(ho)) in list(avaible_move_dictB.get('qb1')):
            peca_d =  list(avaible_move_dictB.get('qb1'))
            d_coord = list(b.coordPe.get('qb1'))
    except:
        pass
    try:
        if (w.coordPc.get(ho)) in list(avaible_move_dictB.get('qb2')):
            peca_d =  list(avaible_move_dictB.get('qb2'))
            d_coord = list(b.coordPe.get('qb2'))
    except:
        pass
    try:
        if (w.coordPc.get(ho)) in list(avaible_move_dictB.get('qb3')):
            peca_d =  list(avaible_move_dictB.get('qb3'))
            d_coord = list(b.coordPe.get('qb3'))
    except:
        pass
    try:
        if (w.coordPc.get(ho)) in list(avaible_move_dictB.get('qb4')):
            peca_d =  list(avaible_move_dictB.get('qb4'))
            d_coord = list(b.coordPe.get('qb4'))
    except:
        pass

    # arrumar variavel!!!!!!!!!!!!!!!!!!!!!
    if (w.coordPc.get(ho)) in peca_d:
        #print(ho)
        co = 75
        try:
            while co <525:
                #print(ho)
                #print((list(w.coordPc.get(ho))[0]+co,list(w.coordPc.get(ho))[1]+co),'----',reiw)
                #print(ho)
                #print(list(w.coordPc.get(ho))[1],'---',reiw[1])

                if list(w.coordPc.get(ho))[1] > reiw[1]: # abaixo do rei
                    #print('a')
                    if list(w.coordPc.get(ho))[0] > reiw[0] and (list(w.coordPc.get(ho))[0] < d_coord[0]):#list(b.coordPe.get('qb0'))[0] or list(w.coordPc.get(ho))[0] < list(b.coordPe.get('bb0'))[0] or list(w.coordPc.get(ho))[0] < list(b.coordPe.get('bb1'))[0]):
                        if (list(w.coordPc.get(ho))[0]-co,list(w.coordPc.get(ho))[1]-co) == reiw:
                            bw = 1
                            #print(ho)
                            break

                        if (list(w.coordPc.get(ho))[0]-co,list(w.coordPc.get(ho))[1]-co) in list(w.coordPc.values()) or (list(w.coordPc.get(ho))[0]-co,list(w.coordPc.get(ho))[1]-co) in list(w.coordPe.values()) or (list(w.coordPc.get(ho))[0]-co,list(w.coordPc.get(ho))[1]-co) in list(b.coordPc.values()) or (list(w.coordPc.get(ho))[0]-co,list(w.coordPc.get(ho))[1]-co) in list(b.coordPe.values()):
                            break
                        

                    if list(w.coordPc.get(ho))[0] < reiw[0] and (list(w.coordPc.get(ho))[0] > d_coord[0]):#list(b.coordPe.get('qb0'))[0] or list(w.coordPc.get(ho))[0] > list(b.coordPe.get('bb0'))[0] or list(w.coordPc.get(ho))[0] > list(b.coordPe.get('bb1'))[0]):
                        if (list(w.coordPc.get(ho))[0]+co,list(w.coordPc.get(ho))[1]-co) == reiw:
                            bw = 1
                            #print(ho)
                            break
                        if (list(w.coordPc.get(ho))[0]+co,list(w.coordPc.get(ho))[1]-co) in list(w.coordPc.values()) or (list(w.coordPc.get(ho))[0]+co,list(w.coordPc.get(ho))[1]-co) in list(w.coordPe.values()) or (list(w.coordPc.get(ho))[0]+co,list(w.coordPc.get(ho))[1]-co) in list(b.coordPc.values()) or (list(w.coordPc.get(ho))[0]+co,list(w.coordPc.get(ho))[1]-co) in list(b.coordPe.values()):
                            break
                        

                if list(w.coordPc.get(ho))[1] < reiw[1]: # acima do rei                    
                    #print(list(w.coordPc.get(ho))[0],'---',peca_d[0])
                    
                    if list(w.coordPc.get(ho))[0] > reiw[0] and (list(w.coordPc.get(ho))[0] < d_coord[0]):#list(b.coordPe.get('qb0'))[0] or list(w.coordPc.get(ho))[0] < list(b.coordPe.get('bb0'))[0] or list(w.coordPc.get(ho))[0] < list(b.coordPe.get('bb1'))[0]):
                        if (list(w.coordPc.get(ho))[0]-co,list(w.coordPc.get(ho))[1]+co) == reiw:
                            bw = 1
                            print(ho)
                            break
                        
                        if (list(w.coordPc.get(ho))[0]-co,list(w.coordPc.get(ho))[1]+co) in list(w.coordPc.values()) or (list(w.coordPc.get(ho))[0]-co,list(w.coordPc.get(ho))[1]+co) in list(w.coordPe.values()) or (list(w.coordPc.get(ho))[0]-co,list(w.coordPc.get(ho))[1]+co) in list(b.coordPc.values()) or (list(w.coordPc.get(ho))[0]-co,list(w.coordPc.get(ho))[1]+co) in list(b.coordPe.values()):
                            break

                    if list(w.coordPc.get(ho))[0] < reiw[0] and (list(w.coordPc.get(ho))[0] > d_coord[0]):#list(b.coordPe.get('qb0'))[0] or list(w.coordPc.get(ho))[0] > list(b.coordPe.get('bb0'))[0] or list(w.coordPc.get(ho))[0] > list(b.coordPe.get('bb1'))[0]):
                        #print(list(w.coordPc.values()))
                        #print('a')
                        if (list(w.coordPc.get(ho))[0]+co,list(w.coordPc.get(ho))[1]+co) == reiw:
                            bw = 1
                            #print(ho)
                            break
                        if (list(w.coordPc.get(ho))[0]+co,list(w.coordPc.get(ho))[1]+co) in list(w.coordPc.values()) or (list(w.coordPc.get(ho))[0]+co,list(w.coordPc.get(ho))[1]+co) in list(w.coordPe.values()) or (list(w.coordPc.get(ho))[0]+co,list(w.coordPc.get(ho))[1]+co) in list(b.coordPc.values()) or (list(w.coordPc.get(ho))[0]+co,list(w.coordPc.get(ho))[1]+co) in list(b.coordPe.values()):
                            break        
                    #print(ho, bw)
                co += 75
        except:
            pass
        #print(bw)
    
         
    dia =0
    try:
        if (w.coordPe.get(ho)) in list(avaible_move_dictB.get('bb1')):
            dia = 1
            peca = 'bb1'
            d_peca = list(b.coordPe.get('bb1'))
    except:
        pass
    try:
        if (w.coordPe.get(ho)) in list(avaible_move_dictB.get('bb0')):
            dia =1
            peca ='bb0'
            d_peca = list(b.coordPe.get('bb0'))
    except:
        pass
    try:
        if (w.coordPe.get(ho)) in list(avaible_move_dictB.get('qb0')):
            dia =1
            peca ='qb0'
            d_peca = list(b.coordPe.get('qb0'))
    except:
        pass
    try:
        if (w.coordPe.get(ho)) in list(avaible_move_dictB.get('qb1')):
            dia =1
            peca ='qb1'
            d_peca = list(b.coordPe.get('qb1'))
    except:
        pass
    try:
        if (w.coordPe.get(ho)) in list(avaible_move_dictB.get('qb2')):
            dia =1
            peca ='qb2'
            d_peca = list(b.coordPe.get('qb2'))
    except:
        pass
    try:
        if (w.coordPe.get(ho)) in list(avaible_move_dictB.get('qb3')):
            dia =1
            peca ='qb3'
            d_peca = list(b.coordPe.get('qb3'))
    except:
        pass
    try:
        if (w.coordPe.get(ho)) in list(avaible_move_dictB.get('qb4')):
            dia =1
            peca ='qb4'
            d_peca = list(b.coordPe.get('qb4'))
    except:
        pass


    if dia == 1:
        co = 75
        try:
            while co <525:
                #print((list(w.coordPc.get(ho))[0]+co,list(w.coordPc.get(ho))[1]+co),'----',reiw)
                if list(w.coordPe.get(ho))[1] > reiw[1]: # abaixo do rei
                    if list(w.coordPe.get(ho))[0] > reiw[0] and (list(w.coordPe.get(ho))[0] < d_peca[0]):#list(b.coordPe.get('qb0'))[0] or list(w.coordPe.get(ho))[0] < list(b.coordPe.get('bb0'))[0] or list(w.coordPe.get(ho))[0] < list(b.coordPe.get('bb1'))[0]):
                        if (list(w.coordPe.get(ho))[0]-co,list(w.coordPe.get(ho))[1]-co) == reiw:
                            bw = 1
                            return peca
                        if (list(w.coordPe.get(ho))[0]-co,list(w.coordPe.get(ho))[1]-co) in list(w.coordPe.values()) or (list(w.coordPe.get(ho))[0]-co,list(w.coordPe.get(ho))[1]-co) in list(w.coordPe.values()) or (list(w.coordPe.get(ho))[0]-co,list(w.coordPe.get(ho))[1]-co) in list(b.coordPc.values()) or (list(w.coordPe.get(ho))[0]-co,list(w.coordPe.get(ho))[1]-co) in list(b.coordPe.values()):
                            return peca
                            
                    if list(w.coordPe.get(ho))[0] < reiw[0] and (list(w.coordPe.get(ho))[0] > d_peca[0]):#list(b.coordPe.get('qb0'))[0] or list(w.coordPe.get(ho))[0] > list(b.coordPe.get('bb0'))[0] or list(w.coordPe.get(ho))[0] > list(b.coordPe.get('bb1'))[0]):
                        if (list(w.coordPe.get(ho))[0]+co,list(w.coordPe.get(ho))[1]-co) == reiw:
                            bw = 1
                            return peca
                        if (list(w.coordPe.get(ho))[0]+co,list(w.coordPe.get(ho))[1]-co) in list(w.coordPe.values()) or (list(w.coordPe.get(ho))[0]+co,list(w.coordPe.get(ho))[1]-co) in list(w.coordPe.values()) or (list(w.coordPe.get(ho))[0]+co,list(w.coordPe.get(ho))[1]-co) in list(b.coordPc.values()) or (list(w.coordPe.get(ho))[0]+co,list(w.coordPe.get(ho))[1]-co) in list(b.coordPe.values()):
                            return peca

                if list(w.coordPe.get(ho))[1] < reiw[1]: # acima do rei
                #print(list(avaible_move_dictB.get('qb0'))[0])
                    #print('teste')
                    if list(w.coordPe.get(ho))[0] > reiw[0] and (list(w.coordPe.get(ho))[0] < d_peca[0]):#list(b.coordPe.get('qb0'))[0] or list(w.coordPe.get(ho))[0] < list(b.coordPe.get('bb0'))[0] or list(w.coordPe.get(ho))[0] < list(b.coordPe.get('bb1'))[0]):
                        
                        if (list(w.coordPe.get(ho))[0]-co,list(w.coordPe.get(ho))[1]+co) == reiw:
                            bw = 1
                            return peca

                        if (list(w.coordPe.get(ho))[0]-co,list(w.coordPe.get(ho))[1]+co) in list(w.coordPc.values()) or (list(w.coordPe.get(ho))[0]-co,list(w.coordPe.get(ho))[1]+co) in list(w.coordPe.values()) or (list(w.coordPe.get(ho))[0]-co,list(w.coordPe.get(ho))[1]+co) in list(b.coordPc.values()) or (list(w.coordPc.get(ho))[0]-co,list(w.coordPc.get(ho))[1]+co) in list(b.coordPe.values()):
                            return peca
                        
                    if list(w.coordPe.get(ho))[0] < reiw[0] and (list(w.coordPe.get(ho))[0] > d_peca[0]):#list(b.coordPe.get('qb0'))[0] or list(w.coordPe.get(ho))[0] > list(b.coordPe.get('bb0'))[0] or list(w.coordPe.get(ho))[0] > list(b.coordPe.get('bb1'))[0]):
                        if (list(w.coordPe.get(ho))[0]+co,list(w.coordPe.get(ho))[1]+co) == reiw:
                            bw = 1
                            return peca
                        if (list(w.coordPe.get(ho))[0]+co,list(w.coordPe.get(ho))[1]+co) in list(w.coordPc.values()) or (list(w.coordPe.get(ho))[0]+co,list(w.coordPe.get(ho))[1]+co) in list(w.coordPe.values()) or (list(w.coordPe.get(ho))[0]+co,list(w.coordPe.get(ho))[1]+co) in list(b.coordPc.values()) or (list(w.coordPe.get(ho))[0]+co,list(w.coordPe.get(ho))[1]+co) in list(b.coordPe.values()):
                            return peca
                        
                co += 75
            
        except:
            pass


def check_pos_moveDB(ho,reib,b,w):
    global bp
    bp =0
    lae = []
    lad = []
    lup = []
    ldw = []

    elae = []
    elad = []
    elup = []
    eldw = []
    
    peca = '' 
    linha = 0
    try:
        if ((b.coordPc.get(ho)) in list(avaible_move_dictW.get('qw0')) and (b.coordPc.get(ho))[1] == reib[1] and (b.coordPc.get(ho))[1] == list(w.coordPe.get('qw0'))[1]) or ((b.coordPe.get(ho)) in list(avaible_move_dictW.get('qw0')) and (b.coordPe.get(ho))[1] == reib[1] and (b.coordPe.get(ho))[1] == list(w.coordPe.get('qw0'))[1]) or ((b.coordPc.get(ho)) in list(avaible_move_dictW.get('qw0')) and (b.coordPc.get(ho))[0] == reib[0] and (b.coordPc.get(ho))[0] == list(w.coordPe.get('qw0'))[0]) or ((b.coordPe.get(ho)) in list(avaible_move_dictW.get('qw0')) and (b.coordPe.get(ho))[0] == reib[0] and (b.coordPe.get(ho))[0] == list(w.coordPe.get('qw0'))[0]):
            linha =1
            peca = 'qw0'
    except:
        pass
    try:
        if ((b.coordPc.get(ho)) in list(avaible_move_dictW.get('qw1')) and (b.coordPc.get(ho))[1] == reib[1] and (b.coordPc.get(ho))[1] == list(w.coordPe.get('qw1'))[1]) or ((b.coordPe.get(ho)) in list(avaible_move_dictW.get('qw1')) and (b.coordPe.get(ho))[1] == reib[1] and (b.coordPe.get(ho))[1] == list(w.coordPe.get('qw1'))[1]) or ((b.coordPc.get(ho)) in list(avaible_move_dictW.get('qw1')) and (b.coordPc.get(ho))[0] == reib[0] and (b.coordPc.get(ho))[0] == list(w.coordPe.get('qw1'))[0]) or ((b.coordPe.get(ho)) in list(avaible_move_dictW.get('qw1')) and (b.coordPe.get(ho))[0] == reib[0] and (b.coordPe.get(ho))[0] == list(w.coordPe.get('qw1'))[0]):
            linha =1
            peca = 'qw1'
    except:
        pass
    try:
        if ((b.coordPc.get(ho)) in list(avaible_move_dictW.get('qw2')) and (b.coordPc.get(ho))[1] == reib[1] and (b.coordPc.get(ho))[1] == list(w.coordPe.get('qw2'))[1]) or ((b.coordPe.get(ho)) in list(avaible_move_dictW.get('qw2')) and (b.coordPe.get(ho))[1] == reib[1] and (b.coordPe.get(ho))[1] == list(w.coordPe.get('qw2'))[1]) or ((b.coordPc.get(ho)) in list(avaible_move_dictW.get('qw2')) and (b.coordPc.get(ho))[0] == reib[0] and (b.coordPc.get(ho))[0] == list(w.coordPe.get('qw2'))[0]) or ((b.coordPe.get(ho)) in list(avaible_move_dictW.get('qw2')) and (b.coordPe.get(ho))[0] == reib[0] and (b.coordPe.get(ho))[0] == list(w.coordPe.get('qw2'))[0]):
            linha =1
            peca = 'qw2'
    except:
        pass
    try:
        if ((b.coordPc.get(ho)) in list(avaible_move_dictW.get('qw3')) and (b.coordPc.get(ho))[1] == reib[1] and (b.coordPc.get(ho))[1] == list(w.coordPe.get('qw3'))[1]) or ((b.coordPe.get(ho)) in list(avaible_move_dictW.get('qw3')) and (b.coordPe.get(ho))[1] == reib[1] and (b.coordPe.get(ho))[1] == list(w.coordPe.get('qw3'))[1]) or ((b.coordPc.get(ho)) in list(avaible_move_dictW.get('qw3')) and (b.coordPc.get(ho))[0] == reib[0] and (b.coordPc.get(ho))[0] == list(w.coordPe.get('qw3'))[0]) or ((b.coordPe.get(ho)) in list(avaible_move_dictW.get('qw3')) and (b.coordPe.get(ho))[0] == reib[0] and (b.coordPe.get(ho))[0] == list(w.coordPe.get('qw3'))[0]):
            linha =1
            peca = 'qw3'
    except:
        pass
    try:
        if ((b.coordPc.get(ho)) in list(avaible_move_dictW.get('qw4')) and (b.coordPc.get(ho))[1] == reib[1] and (b.coordPc.get(ho))[1] == list(w.coordPe.get('qw4'))[1]) or ((b.coordPe.get(ho)) in list(avaible_move_dictW.get('qw4')) and (b.coordPe.get(ho))[1] == reib[1] and (b.coordPe.get(ho))[1] == list(w.coordPe.get('qw4'))[1]) or ((b.coordPc.get(ho)) in list(avaible_move_dictW.get('qw4')) and (b.coordPc.get(ho))[0] == reib[0] and (b.coordPc.get(ho))[0] == list(w.coordPe.get('qw4'))[0]) or ((b.coordPe.get(ho)) in list(avaible_move_dictW.get('qw4')) and (b.coordPe.get(ho))[0] == reib[0] and (b.coordPe.get(ho))[0] == list(w.coordPe.get('qw4'))[0]):
            linha =1
            peca = 'qw4'
    except:
        pass
    try:
        if ((b.coordPc.get(ho)) in list(avaible_move_dictW.get('tw0')) and (b.coordPc.get(ho))[1] == reib[1] and (b.coordPc.get(ho))[1] == list(w.coordPe.get('tw0'))[1]) or ((b.coordPe.get(ho)) in list(avaible_move_dictW.get('tw0')) and (b.coordPe.get(ho))[1] == reib[1] and (b.coordPe.get(ho))[1] == list(w.coordPe.get('tw0'))[1]) or ((b.coordPc.get(ho)) in list(avaible_move_dictW.get('tw0')) and (b.coordPc.get(ho))[0] == reib[0] and (b.coordPc.get(ho))[0] == list(w.coordPe.get('tw0'))[0]) or ((b.coordPe.get(ho)) in list(avaible_move_dictW.get('tw0')) and (b.coordPe.get(ho))[0] == reib[0] and (b.coordPe.get(ho))[0] == list(w.coordPe.get('tw0'))[0]):
            linha = 1
            peca = 'tw0'
    except:
        pass
    try:
        if ((b.coordPc.get(ho)) in list(avaible_move_dictW.get('tw1')) and (b.coordPc.get(ho))[1] == reib[1] and (b.coordPc.get(ho))[1] == list(w.coordPe.get('tw1'))[1]) or ((b.coordPe.get(ho)) in list(avaible_move_dictW.get('tw1')) and (b.coordPe.get(ho))[1] == reib[1] and (b.coordPe.get(ho))[1] == list(w.coordPe.get('tw1'))[1]) or ((b.coordPc.get(ho)) in list(avaible_move_dictW.get('tw1')) and (b.coordPc.get(ho))[0] == reib[0] and (b.coordPc.get(ho))[0] == list(w.coordPe.get('tw1'))[0]) or ((b.coordPe.get(ho)) in list(avaible_move_dictW.get('tw1')) and (b.coordPe.get(ho))[0] == reib[0] and (b.coordPe.get(ho))[0] == list(w.coordPe.get('tw1'))[0]):
            linha=1
            peca = 'tw1'
    except:
        pass
    try:
        if linha == 1:
            for count in b.coordPc.values():
                if count[1] == reib[1]:
                    #print(ho)
                    if count[0] < reib[0]:
                        lae.append(get_key_by_value(b.coordPc,(count[0],count[1])))
                        #print(ho)
                            
                    if count[0] > reib[0]: 
                        lad.append(get_key_by_value(b.coordPc,(count[0],count[1])))

                if count[0] == reib[0]:
                    if count[1] < reib[1]:
                        lup.append(get_key_by_value(b.coordPc,(count[0],count[1])))
                    if count[1] > reib[1]:
                        ldw.append(get_key_by_value(b.coordPc,(count[0],count[1])))

            b.coordPe_copy = b.coordPe.copy()
            del b.coordPe_copy['kb0']
        
            for count in b.coordPe_copy.values():
                #print(ho)
                if count[1] == reib[1]:
                    #print(ho)
                    if count[0] < reib[0]:
                        elae.append(get_key_by_value(b.coordPe,(count[0],count[1])))
                        #print(ho)
                            
                    if count[0] > reib[0]: 
                        elad.append(get_key_by_value(b.coordPe,(count[0],count[1])))
                #
                if count[0] == reib[0]:
                    if count[1] < reib[1]:
                        elup.append(get_key_by_value(b.coordPe,(count[0],count[1])))
                    if count[1] > reib[1]:
                        eldw.append(get_key_by_value(b.coordPe,(count[0],count[1])))
    except:
        pass
        
    if lad !=[] or lae != [] or lup != [] or ldw != [] or elad !=[] or elae != [] or elup != [] or eldw != []:
        if len(lad) == 1 and ho in lad and len(elad) ==0:
            bp = 1
        #print(elae)##
        if (len(lae) == 1 and ho in lae) and len(elae) ==0:
            bp = 1
        
        if len(lup) == 1 and ho in lup and len(elup) ==0:
            bp = 1
        if len(ldw) == 1 and ho in ldw and len(eldw) ==0:
            bp = 1

    #print(ho)
        if len(elad) == 1 and ho in elad and len(lad) ==0:
            bp = 1
        #print(elae, '---' ,len(lae))
        if len(elae) == 1 and ho in elae and len(lae) ==0:
            bp = 1
        
        if len(elup) == 1 and ho in elup and len(lup) ==0:
            bp = 1
        if len(eldw) == 1 and ho in eldw and len(ldw) ==0:
            bp = 1
        return peca
    peca_b = []
    try:
        if (b.coordPc.get(ho)) in list(avaible_move_dictW.get('bw1')): 
            peca_b = list(avaible_move_dictW.get('bw1'))
            d_coord = list(w.coordPe.get('bw1'))
    except:
        pass
    try:
        if (b.coordPc.get(ho)) in list(avaible_move_dictW.get('bw0')):
            peca_b = list(avaible_move_dictW.get('bw0'))
            d_coord = list(w.coordPe.get('bw0'))
    except:
        pass
    try:
        if (b.coordPc.get(ho)) in list(avaible_move_dictW.get('qw0')):
            peca_b = list(avaible_move_dictW.get('qw0'))
            d_coord = list(w.coordPe.get('qw0'))
    except:
        pass
    try:
        if (b.coordPc.get(ho)) in list(avaible_move_dictW.get('qw1')):
            peca_b = list(avaible_move_dictW.get('qw1'))
            d_coord = list(w.coordPe.get('qw1'))
    except:
        pass
    try:
        if (b.coordPc.get(ho)) in list(avaible_move_dictW.get('qw2')):
            peca_b = list(avaible_move_dictW.get('qw2'))
            d_coord = list(w.coordPe.get('qw2'))
    except:
        pass
    try:
        if (b.coordPc.get(ho)) in list(avaible_move_dictW.get('qw3')):
            peca_b = list(avaible_move_dictW.get('qw3'))
            d_coord = list(w.coordPe.get('qw3'))
    except:
        pass
    try:
        if (b.coordPc.get(ho)) in list(avaible_move_dictW.get('qw4')):
            peca_b = list(avaible_move_dictW.get('qw4'))
            d_coord = list(w.coordPe.get('qw4'))
    except:
        pass

    if (b.coordPc.get(ho)) in peca_b:
        co = 75   
        try:
            while co <525:
                #print(ho)
                #print((list(w.coordPc.get(ho))[0]+co,list(w.coordPc.get(ho))[1]+co),'----',reiw)
                
                if list(b.coordPc.get(ho))[1] > reib[1]: # abaixo do rei
                    if list(b.coordPc.get(ho))[0] > reib[0] and (list(b.coordPc.get(ho))[0] < d_coord[0]):#list(w.coordPe.get('qw0'))[0] or list(b.coordPc.get(ho))[0] < list(w.coordPe.get('bw0'))[0] or list(b.coordPc.get(ho))[0] < list(w.coordPe.get('bw1'))[0]):
                        if (list(b.coordPc.get(ho))[0]-co,list(b.coordPc.get(ho))[1]-co) == reib:
                            bp = 1
                            #print(ho)
                            break
#####
                        if (list(b.coordPc.get(ho))[0]-co,list(b.coordPc.get(ho))[1]-co) in list(b.coordPc.values()) or (list(b.coordPc.get(ho))[0]-co,list(b.coordPc.get(ho))[1]-co) in list(b.coordPe.values()) or (list(b.coordPc.get(ho))[0]-co,list(b.coordPc.get(ho))[1]-co) in list(w.coordPc.values()) or (list(b.coordPc.get(ho))[0]-co,list(b.coordPc.get(ho))[1]-co) in list(w.coordPe.values()):
                            break
                        

                    if list(b.coordPc.get(ho))[0] < reib[0] and (list(b.coordPc.get(ho))[0] > d_coord[0]):#list(w.coordPe.get('qw0'))[0] or list(b.coordPc.get(ho))[0] > list(w.coordPe.get('bw0'))[0] or list(b.coordPc.get(ho))[0] > list(w.coordPe.get('bw1'))[0]):
                        if (list(b.coordPc.get(ho))[0]+co,list(b.coordPc.get(ho))[1]-co) == reib:
                            bp = 1
                            #print(ho)
                            break
                        if (list(b.coordPc.get(ho))[0]+co,list(b.coordPc.get(ho))[1]-co) in list(b.coordPc.values()) or (list(b.coordPc.get(ho))[0]+co,list(b.coordPc.get(ho))[1]-co) in list(b.coordPe.values()) or (list(b.coordPc.get(ho))[0]+co,list(b.coordPc.get(ho))[1]-co) in list(w.coordPc.values()) or (list(b.coordPc.get(ho))[0]+co,list(b.coordPc.get(ho))[1]-co) in list(w.coordPe.values()):
                            break
                        

                if list(b.coordPc.get(ho))[1] < reib[1]: # acima do rei
                #print(list(avaible_move_dictW.get('qw0'))[0])
                    
                    #print('teste')
                    if list(b.coordPc.get(ho))[0] > reib[0] and (list(b.coordPc.get(ho))[0] < d_coord[0]):#list(w.coordPe.get('qw0'))[0] or list(b.coordPc.get(ho))[0] < list(w.coordPe.get('bw0'))[0] or list(b.coordPc.get(ho))[0] < list(w.coordPe.get('bw1'))[0]):
                        if (list(b.coordPc.get(ho))[0]-co,list(b.coordPc.get(ho))[1]+co) == reib:
                            bp = 1
                            #print(ho)
                            break
                        
                        if (list(b.coordPc.get(ho))[0]-co,list(b.coordPc.get(ho))[1]+co) in list(b.coordPc.values()) or (list(b.coordPc.get(ho))[0]-co,list(b.coordPc.get(ho))[1]+co) in list(b.coordPe.values()) or (list(b.coordPc.get(ho))[0]-co,list(b.coordPc.get(ho))[1]+co) in list(w.coordPc.values()) or (list(b.coordPc.get(ho))[0]-co,list(b.coordPc.get(ho))[1]+co) in list(w.coordPe.values()):
                            break

                    if list(b.coordPc.get(ho))[0] < reib[0] and (list(b.coordPc.get(ho))[0] > d_coord[0]):#list(w.coordPe.get('qw0'))[0] or list(b.coordPc.get(ho))[0] > list(w.coordPe.get('bw0'))[0] or list(b.coordPc.get(ho))[0] > list(w.coordPe.get('bw1'))[0]):
                        #print(list(w.coordPc.values()))
                        #print('a')
                        if (list(b.coordPc.get(ho))[0]+co,list(b.coordPc.get(ho))[1]+co) == reib:
                            bp = 1
                            #print(ho)
                            break
                        if (list(b.coordPc.get(ho))[0]+co,list(b.coordPc.get(ho))[1]+co) in list(b.coordPc.values()) or (list(b.coordPc.get(ho))[0]+co,list(b.coordPc.get(ho))[1]+co) in list(b.coordPe.values()) or (list(b.coordPc.get(ho))[0]+co,list(b.coordPc.get(ho))[1]+co) in list(w.coordPc.values()) or (list(b.coordPc.get(ho))[0]+co,list(b.coordPc.get(ho))[1]+co) in list(w.coordPe.values()):
                            break        
                    #print(ho, bw)
                co += 75
        except:
            pass
    
         
    dia =0
    try:
        if (b.coordPe.get(ho)) in list(avaible_move_dictW.get('bw1')):
            dia = 1
            peca = 'bw1'
            d_peca = list(w.coordPe.get('bw1'))
    except:
        pass
    try:
        if (b.coordPe.get(ho)) in list(avaible_move_dictW.get('bw0')):
            dia =1
            peca ='bw0'
            d_peca = list(w.coordPe.get('bw0'))
    except:
        pass
    try:
        if (b.coordPe.get(ho)) in list(avaible_move_dictW.get('qw0')):
            dia =1
            peca ='qw0'
            d_peca = list(w.coordPe.get('qw0'))
    except:
        pass
    try:
        if (b.coordPe.get(ho)) in list(avaible_move_dictW.get('qw1')):
            dia =1
            peca ='qw1'
            d_peca = list(w.coordPe.get('qw1'))
    except:
        pass
    try:
        if (b.coordPe.get(ho)) in list(avaible_move_dictW.get('qw2')):
            dia =1
            peca ='qw2'
            d_peca = list(w.coordPe.get('qw2'))
    except:
        pass
    try:
        if (b.coordPe.get(ho)) in list(avaible_move_dictW.get('qw3')):
            dia =1
            peca ='qw3'
            d_peca = list(w.coordPe.get('qw3'))
    except:
        pass
    try:
        if (b.coordPe.get(ho)) in list(avaible_move_dictW.get('qw4')):
            dia =1
            peca ='qw4'
            d_peca = list(w.coordPe.get('qw4'))
    except:
        pass
       
    if dia == 1:
        co = 75
        try:
            while co <525:
                #print((list(b.coordPc.get(ho))[0]+co,list(b.coordPc.get(ho))[1]+co),'----',reib)
                if list(b.coordPe.get(ho))[1] > reib[1]: # abaixo do rei
                    if list(b.coordPe.get(ho))[0] > reib[0] and (list(b.coordPe.get(ho))[0] < d_peca[0]):#list(w.coordPe.get('qw0'))[0] or list(b.coordPe.get(ho))[0] < list(w.coordPe.get('bw0'))[0] or list(b.coordPe.get(ho))[0] < list(w.coordPe.get('bw1'))[0]):
                        if (list(b.coordPe.get(ho))[0]-co,list(b.coordPe.get(ho))[1]-co) == reib:
                            bp = 1
                            return peca
                        if (list(b.coordPe.get(ho))[0]-co,list(b.coordPe.get(ho))[1]-co) in list(b.coordPe.values()) or (list(b.coordPe.get(ho))[0]-co,list(b.coordPe.get(ho))[1]-co) in list(b.coordPe.values()) or (list(b.coordPe.get(ho))[0]-co,list(b.coordPe.get(ho))[1]-co) in list(w.coordPc.values()) or (list(b.coordPe.get(ho))[0]-co,list(b.coordPe.get(ho))[1]-co) in list(w.coordPe.values()):
                            return peca
                            
                    if list(b.coordPe.get(ho))[0] < reib[0] and (list(b.coordPe.get(ho))[0] > d_peca[0]):#list(w.coordPe.get('qw0'))[0] or list(b.coordPe.get(ho))[0] > list(w.coordPe.get('bw0'))[0] or list(b.coordPe.get(ho))[0] > list(w.coordPe.get('bw1'))[0]):
                        #print(peca)
                        if (list(b.coordPe.get(ho))[0]+co,list(b.coordPe.get(ho))[1]-co) == reib:
                            bp = 1
                            return peca
                        if (list(b.coordPe.get(ho))[0]+co,list(b.coordPe.get(ho))[1]-co) in list(b.coordPe.values()) or (list(b.coordPe.get(ho))[0]+co,list(b.coordPe.get(ho))[1]-co) in list(b.coordPe.values()) or (list(b.coordPe.get(ho))[0]+co,list(b.coordPe.get(ho))[1]-co) in list(w.coordPc.values()) or (list(b.coordPe.get(ho))[0]+co,list(b.coordPe.get(ho))[1]-co) in list(w.coordPe.values()):
                            return peca

                if list(b.coordPe.get(ho))[1] < reib[1]: # acima do rei
                #print(list(avaible_move_dictW.get('qw0'))[0])
                    #print('teste')
                    if list(b.coordPe.get(ho))[0] > reib[0] and (list(b.coordPe.get(ho))[0] < d_peca[0]):#list(w.coordPe.get('qw0'))[0] or list(b.coordPe.get(ho))[0] < list(w.coordPe.get('bw0'))[0] or list(b.coordPe.get(ho))[0] < list(w.coordPe.get('bw1'))[0]):
                        
                        if (list(b.coordPe.get(ho))[0]-co,list(b.coordPe.get(ho))[1]+co) == reib:
                            bp = 1
                            return peca

                        if (list(b.coordPe.get(ho))[0]-co,list(b.coordPe.get(ho))[1]+co) in list(b.coordPc.values()) or (list(b.coordPe.get(ho))[0]-co,list(b.coordPe.get(ho))[1]+co) in list(b.coordPe.values()) or (list(b.coordPe.get(ho))[0]-co,list(b.coordPe.get(ho))[1]+co) in list(w.coordPc.values()) or (list(b.coordPc.get(ho))[0]-co,list(b.coordPc.get(ho))[1]+co) in list(w.coordPe.values()):
                            return peca
                        
                    if list(b.coordPe.get(ho))[0] < reib[0] and (list(b.coordPe.get(ho))[0] > d_peca[0]):#list(w.coordPe.get('qw0'))[0] or list(b.coordPe.get(ho))[0] > list(w.coordPe.get('bw0'))[0] or list(b.coordPe.get(ho))[0] > list(w.coordPe.get('bw1'))[0]):
                        if (list(b.coordPe.get(ho))[0]+co,list(b.coordPe.get(ho))[1]+co) == reib:
                            bp = 1
                            return peca
                        if (list(b.coordPe.get(ho))[0]+co,list(b.coordPe.get(ho))[1]+co) in list(b.coordPc.values()) or (list(b.coordPe.get(ho))[0]+co,list(b.coordPe.get(ho))[1]+co) in list(b.coordPe.values()) or (list(b.coordPe.get(ho))[0]+co,list(b.coordPe.get(ho))[1]+co) in list(w.coordPc.values()) or (list(b.coordPe.get(ho))[0]+co,list(b.coordPe.get(ho))[1]+co) in list(w.coordPe.values()):
                            return peca
                        
                co += 75
            
        except:
            pass

######Funções auxiliares#############


w,tw0,tw1 = 0,0,0
kb,tb0,tb1 = 0,0,0
qb,qw =0, 0
class peaces():
    def __init__(self,parts,lPc,lPe,c):
        pawns = parts.pawn()
        self.peacesC = {}
        self.coordPc = {}
        n = str(lPc)

        # Peão
        for a in range(0,8):
            self.peacesC[a] = pawns[a]#Guada a renderização das peças
            #print(peaces)
            self.coordPc['p'+c+str(a)] = conv(listabc[a]+str(n))# uma casa e uma coordenada(conv)

        ####
        x = str(lPe)
        self.peacesE = {}
        self.coordPe = {}

        horse = parts.horse()
        bishop = parts.bishop()
        tower = parts.tower()
        self.queen = parts.queen()
        king = parts.king()

        h = 1
        for a in range(0,2): # Criar as outras peças na posição padrão
            self.peacesE[a] = horse[a]
            self.coordPe['h'+c+str(a)] = conv(listabc[a+h]+x)
            h=5

        b=2
        for a in range(0,2):
            self.peacesE[a+2] = bishop[a]
            #print(self.peacesE)
            self.coordPe['b'+c+str(a)] = conv(listabc[a+b]+x)
            b=4

        t=0
        for a in range(0,2):
            self.peacesE[a+4] = tower[a]
            #print(self.peacesE)
            self.coordPe['t'+c+str(a)] = conv(listabc[a+t]+x)
            t=6

        for a in range(1):
            self.peacesE[a+6] = self.queen
            self.peacesE[a+7] = king
            self.coordPe['q'+c+str(a)] = conv(listabc[3]+x)
            self.coordPe['k'+c+str(a)] = conv(listabc[4]+x)
            #print(self.peacesE)

        #Atualização das peças por meio da atualização do dicionario coodPc


    def draw_peace(self,screeni,c,screen,w,b):
        for a in range(0,8):
            try:
                #print(self.coordPc)
                screeni.blit(self.peacesC[a],self.coordPc['p'+c+str(a)])#desenha a peça(render,coordenada(key=casa))
            except:
                pass
        
        for a in range(0,4):
            try:
                #print(b.coordPe,'---',b.peacesE)
                screeni.blit(self.peacesE[a+2],self.coordPe['b'+c+str(a)]) 
            except:
                pass
            try:
                screeni.blit(self.peacesE[a+4],self.coordPe['t'+c+str(a)])
            except:
                pass
            try:
                screeni.blit(self.peacesE[a],self.coordPe['h'+c+str(a)])
            except:
                pass
            #print('q'+c+str(a+1))
            try:
                screeni.blit(self.peacesE[6],self.coordPe['q'+c+'0'])
            except:
                pass
            try:
                screeni.blit(self.peacesE[6],self.coordPe['q'+c+str(a+1)])
            except:
                pass
            try:
                screeni.blit(self.peacesE[7],self.coordPe['k'+c+'0'])
            except:
                pass
        

    def updateP(self,coordP,screeni,posicao_mouse_now,pe,confs,w,b):
        global kw,tw0,tw1 
        global kb,tb0,tb1
        global qb,qw
        #print(dict)
        
        if pe != 1: #Para atualizar Pc

            self.coordPc[coordP] = (posicao_mouse_now) # Atualiza a casa e coordenada da peça pelo mouse
            a=0
        
        elif pe == 1: #Para atualizar Pe, se é especial vou atualizar outro dicionario
            if ((coordP == 'kw0' and posicao_mouse_now[0] == 0) or (coordP == 'kw0' and posicao_mouse_now[0] == 150)) and kw !=1 and tw0 != 1:
                self.coordPe[coordP] = (150,posicao_mouse_now[1])
                self.coordPe['tw0'] = (225, posicao_mouse_now[1])

            elif ((coordP == 'kw0' and posicao_mouse_now[0] == 525) or (coordP == 'kw0' and posicao_mouse_now[0] == 450)) and kw !=1 and tw1 != 1:
                self.coordPe[coordP] = (450,posicao_mouse_now[1])
                self.coordPe['tw1'] = (375, posicao_mouse_now[1])

            if ((coordP == 'kb0' and posicao_mouse_now[0] == 0) or (coordP == 'kb0' and posicao_mouse_now[0] == 150)) and kb !=1 and tb0 != 1:
                self.coordPe[coordP] = (150,posicao_mouse_now[1])
                self.coordPe['tb0'] = (225, posicao_mouse_now[1])

            elif ((coordP == 'kb0' and posicao_mouse_now[0] == 525) or (coordP == 'kb0' and posicao_mouse_now[0] == 450)) and kb !=1 and tb1 != 1:
                self.coordPe[coordP] = (450,posicao_mouse_now[1])
                self.coordPe['tb1'] = (375, posicao_mouse_now[1])

            else:
                self.coordPe[coordP] = (posicao_mouse_now)
            
        if coordP[1:2] == 'w':
            #print(self.coordPc)
            if (elPWe == 1 or elPWr == 1) and coordP == elP:
                #print((posicao_mouse_now[0],posicao_mouse_now[1]+75),'----', b.coordPc)
                if (posicao_mouse_now[0],posicao_mouse_now[1]+75) in b.coordPc.values():
                    posicao_mouse_now = (posicao_mouse_now[0],posicao_mouse_now[1]+75)
                    pc = (get_key_by_value(b.coordPc,posicao_mouse_now))
                    capeaceCb[pc] = (pc[2:3])
                    del b.coordPc[pc]

            if posicao_mouse_now in b.coordPc.values():
                
                pc = (get_key_by_value(b.coordPc,posicao_mouse_now))
                capeaceCb[pc] = (pc[2:3])
                del b.coordPc[pc]
            if posicao_mouse_now in b.coordPe.values():
                pc = (get_key_by_value(b.coordPe,posicao_mouse_now))
                a=0
                if pc[0:1] == 'b':
                    #print(pc[0:1])
                    a=2
                elif pc[0:1] ==  't':
                    a=4
                elif pc[0:1] == 'q' and pc[2:3] == '0':
                    a = 6
                elif pc[0:1] == 'q' and pc[2:3] == '1':
                    a = 7
                elif pc[0:1] == 'q' and pc[2:3] == '2':
                    a = 7
                elif pc[0:1] == 'q' and pc[2:3] == '3':
                    a = 7
                elif pc[0:1] == 'q' and pc[2:3] == '4':
                    a = 7
                #print(pc)
                capeaceEb[pc] = str(int(pc[2:3])+a)
                #print(str(int(pc[2:3])+a))
                #print(pc)
                del b.coordPe[pc]
            #print(qw)
            if posicao_mouse_now[1] == 0:
                del self.coordPc[coordP]
                self.peacesE[8+qw] = self.queen
                self.coordPe['qw'+str(qw+1)] = posicao_mouse_now
                qw += 1
                #print(self.peacesE)
                #print(self.coordPe)

                
        if coordP[1:2] == 'b':
            #print(self.coordPc)
            if (elPBe ==1 or elPBr ==1) and coordP == elP:
                if (posicao_mouse_now[0],posicao_mouse_now[1]-75) in w.coordPc.values():
                    posicao_mouse_now = (posicao_mouse_now[0],posicao_mouse_now[1]-75)
                    pc = (get_key_by_value(w.coordPc,posicao_mouse_now))
                    capeaceCw[pc] = (pc[2:3])
                    del w.coordPc[pc]

            if posicao_mouse_now in w.coordPc.values():
                pc = (get_key_by_value(w.coordPc,posicao_mouse_now))
                #print(pc)
                capeaceCw[pc] = (pc[2:3])
                del w.coordPc[pc]
            elif posicao_mouse_now in w.coordPe.values():
                pc = (get_key_by_value(w.coordPe,posicao_mouse_now))
                a = 0
                if pc[0:1] == 'b':
                    #print(pc[0:1])
                    a=2
                elif pc[0:1] ==  't':
                    a=4
                elif pc[0:1] == 'q' and pc[2:3] == '0':
                    a = 6
                elif pc[0:1] == 'q' and pc[2:3] == '1':
                    a = 7
                elif pc[0:1] == 'q' and pc[2:3] == '2':
                    a = 7
                elif pc[0:1] == 'q' and pc[2:3] == '3':
                    a = 7
                elif pc[0:1] == 'q' and pc[2:3] == '4':
                    a = 7
                #print(pc[0:1],'--',pc[2:3])
                capeaceEw[pc] = str(int(pc[2:3])+a)
                
                del w.coordPe[pc]
            
            if posicao_mouse_now[1] == 525:
                del b.coordPc[coordP]
                self.peacesE[8+qb] = self.queen
                self.coordPe['qb'+str(qb+1)] = posicao_mouse_now
                qb += 1

        global selected
        selected = 0
        global upd
        upd = 1
        global check_w
        check_w =0
        global check_b
        check_b = 0
        chenge_turn(confs)


movePc = None
movePe = None
selected = 0
pe = 3
XcoordsPc_copy = {}
XcoordsPe_copy = {}
draw_d =0 # Limitir a repetição do desenho da bolas, para que não se desenhe infinitamente
def select(screeni,confs,dictP,w,b):# dictP  w,b
    global movePc,movePe, selected,pe
    global XcoordsPc_copy,XcoordsPe_copy
    global draw_d
    #print(selected)
    if selected == 0: #Se não tiver nada selecionado, pass um vez pelo updateT depois só ae executar os if pe ...
        for event in pygame.event.get(): #espera um evento
            if event.type == pygame.QUIT:# para fechar a janela
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:#envento de click
                posicao_mouse = pygame.mouse.get_pos()#gurda posição do mouse
                posicao_mouse_ant= (get_prev_mullti(posicao_mouse[0]-201),get_prev_mullti(posicao_mouse[1]-51))
                #print(posicao_mouse_ant,'---')

                #print(color ,'-------', confs.t)
                #print(dictP.coordPc) # w.coordPc ou b.coordPc
                for cood in dictP.coordPc.values():
                    if (posicao_mouse_ant) == cood: # Se a posição do mouse _ant for igual a cood em coodPc
                        movePc = cood
                        selected = 1 # Para ir para o outro for
                        pe = 0

                        XcoordsPc_copy = dictP.coordPc.copy()
                        
                for cood in dictP.coordPe.values(): # Se a posição do mouse _ant for igual a cood em coodPe
                    if (posicao_mouse_ant) == cood:
                        #print(coordPe)
                        movePe = cood
                        selected = 1
                        pe = 1# Se é uma peça especial

                        XcoordsPe_copy = dictP.coordPe.copy()
                draw_d = 0
      
    if pe == 0:
        move(XcoordsPc_copy,movePc,confs,screeni,pe,dictP,w,b) # MOve peças comuns
    elif pe == 1:
        move(XcoordsPe_copy,movePe,confs,screeni,pe,dictP,w,b) # Moves peças especiais


# Para a regra do elPasant
elPWr,elPWe,elPBr,elPBe = 0,0,0,0
elP = ''
#Posiçoes possiveis
avaible_move = []
#Para roque
kw,tw0,tw1 = 0,0,0
kb,tb0,tb1 = 0,0,0
#tripla repetição do rei e peça
peca_ant = []
pecaK_ant = []
rep = 0
Nrep =5
pe_ant = ''
pecaW_ant = []
pecaKW_ant = []
repW = 0
peW_ant = ''
def move(XcoordsPx,movePx,confs,screeni,pe,dictP,w,b):
    global selected
    global elPWr,elPWe,elPBr,elPBe, elP
    global draw_d
    global avaible_move_dictW,avaible_move_dictB,avaible_move
    global kw,tw0,tw1,kb,tb0,tb1
    global check_w,check_b
    global Nrep
    global peca_ant,pecaK_ant,rep,repW
    global peca,pecaB
    global pecaW_ant, pecaKW_ant,peW_ant

    #guardas posiçoes validas
    peace_cood = get_key_by_value(XcoordsPx,movePx)
    #Para desenhar apenas uma vez
    #print(peace_cood)
    if draw_d == 0:
        if peace_cood[1:2] == 'w':
            #if check == 1:
            #    print(avaible_move_dictW.get(peace_cood))
            draw_check(avaible_move_dictW.get(peace_cood),screeni)
            avaible_move = avaible_move_dictW.get(peace_cood)
            #print(avaible_move_dictW)

        if peace_cood[1:2] == 'b':
            #print(avaible_move_dictB)
            draw_check(avaible_move_dictB.get(peace_cood),screeni)
            avaible_move = avaible_move_dictB.get(peace_cood)
        draw_d = 1
    
    #Se tripla repetição então empata

    #Captura a poscição ant do rei para uma lista 2 valores
    if peace_cood[1:2] == 'b':
        if b.coordPe.get('kb0') not in pecaK_ant:
            pecaK_ant.append(b.coordPe.get('kb0'))

        if len(pecaK_ant) ==3:
            pecaK_ant.pop(0)
    
    #Captura a poscição ant da peça que deu check para uma lista 2 valores
    if pecaB[1:2] == 'w':
        if w.coordPe.get(pecaB) not in peca_ant:
            peca_ant.append(w.coordPe.get(pecaB))
        if len(peca_ant) ==3:
            peca_ant.pop(0)

    ################### Falta isso
    
    if peace_cood[1:2] == 'w':
        if w.coordPe.get('kw0') not in pecaKW_ant:
            pecaKW_ant.append(w.coordPe.get('kw0'))

        if len(pecaKW_ant) ==3:
            pecaKW_ant.pop(0)

    if peca[1:2] == 'b':
        if b.coordPe.get(peca) not in pecaW_ant:
            pecaW_ant.append(b.coordPe.get(peca))
        if len(pecaW_ant) ==3:
            pecaW_ant.pop(0)
    #print(pecaW_ant)
    ######
    if  rep == Nrep:
        confs.game = 3
    if repW == Nrep:
        confs.game=3

    if avaible_move != None:
        for event in pygame.event.get(): #Se fundo evento
            if event.type == pygame.QUIT:# para fechar a janela
                    pygame.quit()
                    sys.exit()
                    
            if event.type == pygame.MOUSEBUTTONDOWN:# de cliker
                posicao_mouse = pygame.mouse.get_pos()
                posicao_mouse_now = (get_prev_mullti(posicao_mouse[0]-201),get_prev_mullti(posicao_mouse[1]-51))
                #atualizar posiçoes das peças no segundo clique
                try:
                    if posicao_mouse_now in avaible_move or posicao_mouse_now == avaible_move:

                        #### Para Atualizar
                        dictP.updateP(get_key_by_value(XcoordsPx,movePx),screeni,posicao_mouse_now,pe,confs,w,b)   
                        elPWr,elPWe,elPBr,elPBe =0,0,0,0
                        ####


                        #verifica se é o rei preto jogando
                        try:
                            if peace_cood == 'kb0' :
                                if b.coordPe.get('kb0') in pecaK_ant: #se a posição atual existe na posição anterior
                                    rep = rep + 1
                                else:
                                    rep= 0
                            if peace_cood == pecaB:
                                if  w.coordPe.get(pecaB) in peca_ant:
                                    pass
                                else:
                                    rep =0    
                            #se eu jogar com uma peça que não seja o rei eu reseto o rep
                            if peace_cood[1:2] == 'b' and peace_cood != 'kb0':
                                rep = 0
                                pecaK_ant = []
                                peca_ant = []
                                #peca_ant = peace_cood
                            elif (peace_cood[1:2] == 'w' and peace_cood != pe_ant):
                                rep = 0
                                pecaK_ant = []
                                peca_ant = []
                            pe_ant = pecaB
                        except:
                            pass
                        ######################
                        try:
                            #print(peca)
                            if peace_cood == 'kw0' :
                                if w.coordPe.get('kw0') in pecaKW_ant: #se a posição atual existe na posição anterior
                                    repW = repW + 1
                                else:#
                                    repW= 0
                            if peace_cood == peca:
                                if  b.coordPe.get(peca) in pecaW_ant:
                                    pass
                                else:
                                    repW =0    
                            #se eu jogar com uma peça que não seja o rei eu reseto o rep
                            
                            if peace_cood[1:2] == 'w' and peace_cood != 'kw0':
                                repW = 0
                                pecaKW_ant = []
                                #pecaW_ant = []
                                #peca_ant = peace_cood
                            elif (peace_cood[1:2] == 'b' and peace_cood != peW_ant):
                                repW = 0
                                pecaKW_ant = []
                                pecaW_ant = []
                            peW_ant = peca
                        except:
                            pass
                        #
                        #print(repW)                

                        check_w = 0
                        check_b = 0

                        if peace_cood[0:2] == 'kw':
                            kw = 1
                        if peace_cood == 'tw0':
                            tw0 =1
                        if peace_cood == 'tw1':
                            tw1 =1
                        if peace_cood[0:2] == 'kb':
                            kb = 1
                        if peace_cood == 'tb0':
                            tb0 =1
                        if peace_cood == 'tb1':
                            tb1 =1
                        
                    else:
                        selected = 0
                        
                        #elPWr,elPWe,elPBr,elPBe =0,0,0,0
                        create_tabu(screeni,confs)

                except:
                    pass
                
                

                # Para a regra do elPasant
                yw = [lista[1] for lista in w.coordPc.values()]
                yb = [lista[1] for lista in b.coordPc.values()]

                if (movePx[1] == 75 and posicao_mouse_now[1] == 225 and posicao_mouse_now[1] in yw):
                    #print(posicao_mouse_now, '', w.coordPc.values())
                    if (posicao_mouse_now[0]+75, posicao_mouse_now[1]) in w.coordPc.values():
                        elPWe = 1
                        elP = get_key_by_value(w.coordPc,(posicao_mouse_now[0]+75,posicao_mouse_now[1]))
                    if (posicao_mouse_now[0]-75, posicao_mouse_now[1]) in w.coordPc.values():
                        elPWr = 1
                        elP = get_key_by_value(w.coordPc,(posicao_mouse_now[0]-75,posicao_mouse_now[1]))
                    
                if (movePx[1] == 450 and posicao_mouse_now[1] ==300 and posicao_mouse_now[1] in yb):
                    if (posicao_mouse_now[0]+75, posicao_mouse_now[1]) in b.coordPc.values():
                        elPBe = 1
                        elP = get_key_by_value(b.coordPc,(posicao_mouse_now[0]+75,posicao_mouse_now[1]))
                    if (posicao_mouse_now[0]-75, posicao_mouse_now[1]) in b.coordPc.values():
                        elPBr = 1
                        elP = get_key_by_value(b.coordPc,(posicao_mouse_now[0]-75,posicao_mouse_now[1]))
                
                # atualizar tabuleiro
                
                create_tabu(screeni,confs)
                
    else:
        selected = 0


bw = 0
bp = 0    
defense_pw = []
defense_pb = []
def check_mov(movePx,ho,w,b,screeni):
    reiw = w.coordPe.get('kw0')
    reib = b.coordPe.get('kb0')
    #bw=0
    try:
        avaible_move = []
        #print(XcoordsPx)
        global elPWr,elPWe,elPBe,elPBr 
        global kw,tw0,tw1,kb,tb0,tb1
        global defense_pw
        
        #Movimento Peão
        ##
        try:
            #print(bw)
            if ho[0:2] == 'pw':
                check_pos_moveDW(ho,reiw,w,b)
                #print(bw)
                if bw == 1:
                    pass
                else:
                    #print(ho)
                    #para movimentação
                    if movePx[1] == 450:
                        if ((movePx[0],movePx[1]-75)  not in w.coordPc.values() and (movePx[0],movePx[1]-75) not in b.coordPc.values()) and ((movePx[0],movePx[1]-75)  not in w.coordPe.values() and (movePx[0],movePx[1]-75) not in b.coordPe.values()):
                            avaible_move.append((movePx[0],movePx[1]-75))   
                        if ((movePx[0],movePx[1]-75)  not in w.coordPc.values() and (movePx[0],movePx[1]-75) not in b.coordPc.values()) and ((movePx[0],movePx[1]-75)  not in w.coordPe.values() and (movePx[0],movePx[1]-75) not in b.coordPe.values()) and ((movePx[0],movePx[1]-150)  not in w.coordPc.values() and (movePx[0],movePx[1]-150) not in b.coordPc.values()) and ((movePx[0],movePx[1]-150)  not in w.coordPe.values() and (movePx[0],movePx[1]-150) not in b.coordPe.values()):
                            avaible_move.append((movePx[0],movePx[1]-150))
                    else:
                        if ((movePx[0],movePx[1]-75)  not in w.coordPc.values() and (movePx[0],movePx[1]-75) not in b.coordPc.values()) and ((movePx[0],movePx[1]-75)  not in w.coordPe.values() and (movePx[0],movePx[1]-75) not in b.coordPe.values()):
                            avaible_move.append((movePx[0],movePx[1]-75))
                    #print(ho)
                
                if check_w != 1 and bw !=1:
                    ###########
                    

                #Para captura diagonal
                    if (movePx[0]+75,movePx[1]-75) in b.coordPc.values() or (movePx[0]+75,movePx[1]-75) in b.coordPe.values():
                        avaible_move.append((movePx[0]+75,movePx[1]-75))
                    if (movePx[0]-75,movePx[1]-75) in b.coordPc.values() or (movePx[0]-75,movePx[1]-75) in b.coordPe.values():
                        avaible_move.append((movePx[0]-75,movePx[1]-75))

                    if elPWe == 1 and ho == elP:
                        avaible_move.append((movePx[0]-75,movePx[1]-75))
                        #print(elP)
                    elif elPWr == 1 and ho == elP:
                        avaible_move.append((movePx[0]+75,movePx[1]-75))
                        #print(elP)
                
                else:
                    #print(((movePx[0]-75,movePx[1]-75) == (b.coordPe.get('tb0'))))
                    if ((movePx[0]+75,movePx[1]-75) == (b.coordPe.get('qb0'))) or ((movePx[0]+75,movePx[1]-75) == (b.coordPe.get('tb0'))) or ((movePx[0]+75,movePx[1]-75) == (b.coordPe.get('bb0'))) or ((movePx[0]+75,movePx[1]-75) == (b.coordPe.get('tb1'))) or ((movePx[0]+75,movePx[1]-75) == (b.coordPe.get('bb1'))):
                        avaible_move.append((movePx[0]+75,movePx[1]-75))
                        peao =1
                    elif ((movePx[0]+75,movePx[1]-75) in (b.coordPc.values())) and peao ==0:
                        avaible_move.append((movePx[0]+75,movePx[1]-75))
                    
                    if ((movePx[0]-75,movePx[1]-75) == (b.coordPe.get('qb0'))) or ((movePx[0]-75,movePx[1]-75) == (b.coordPe.get('tb0'))) or ((movePx[0]-75,movePx[1]-75) == (b.coordPe.get('bb0'))) or ((movePx[0]-75,movePx[1]-75) == (b.coordPe.get('tb1'))) or ((movePx[0]-75,movePx[1]-75) == (b.coordPe.get('bb1'))):
                        avaible_move.append((movePx[0]-75,movePx[1]-75))
                        peao =1
                    elif ((movePx[0]-75,movePx[1]-75) in (b.coordPc.values()))  and peao ==0:
                        avaible_move.append((movePx[0]-75,movePx[1]-75))

                #print(avaible_move)
               
            elif ho[0:2] == 'pb':
                check_pos_moveDB(ho,reib,b,w)
                #print(bw)
                if  bp == 1:
                    #print('a')
                    pass
                else:
                #para movimentação
                    if movePx[1] == 75:
                        if (movePx[0],movePx[1]+75)  not in w.coordPc.values() and (movePx[0],movePx[1]+75) not in b.coordPc.values() and ((movePx[0],movePx[1]+75)  not in w.coordPe.values() and (movePx[0],movePx[1]+75) not in b.coordPe.values()):
                            avaible_move.append((movePx[0],movePx[1]+75))
                        if (movePx[0],movePx[1]+75)  not in w.coordPc.values() and (movePx[0],movePx[1]+150) not in b.coordPc.values() and ((movePx[0],movePx[1]+75)  not in w.coordPe.values() and (movePx[0],movePx[1]+75) not in b.coordPe.values()) and ((movePx[0],movePx[1]+150)  not in w.coordPc.values() and (movePx[0],movePx[1]+150) not in b.coordPc.values()) and ((movePx[0],movePx[1]+150)  not in w.coordPe.values() and (movePx[0],movePx[1]+150) not in b.coordPe.values()):
                            avaible_move.append((movePx[0],movePx[1]+150))
                    else:
                        if (movePx[0],movePx[1]+75)  not in w.coordPc.values() and (movePx[0],movePx[1]+75) not in b.coordPc.values() and ((movePx[0],movePx[1]+75)  not in w.coordPe.values() and (movePx[0],movePx[1]+75) not in b.coordPe.values()):
                            avaible_move.append((movePx[0],movePx[1]+75))

                #Para captura diagonal
                #print(check)
                if check_b != 1 and bp !=1:#and ((b.coordPc.get(ho)) not in list(avaible_move_dictW.get('qw0')) and (b.coordPc.get(ho))[1] != reib[1] and (b.coordPc.get(ho))[1] != list(w.coordPe.get('qw0'))[1] or ((b.coordPc.get(ho)) not in list(avaible_move_dictW.get('tw0'))) and (b.coordPc.get(ho))[1] != reib[1] and (b.coordPc.get(ho))[1] != list(w.coordPe.get('tw0'))[1]):
                    #if ((((b.coordPc.get(ho))[1] != list(w.coordPe.get('qw0'))[1]) or reib[1] != (b.coordPc.get(ho))[1]) and (((b.coordPc.get(ho))[0] != list(w.coordPe.get('qw0'))[0]) or reib[0] != (b.coordPc.get(ho))[0])) and ((((b.coordPc.get(ho))[1] != list(w.coordPe.get('tw0'))[1]) or reib[1] != (b.coordPc.get(ho))[1]) and  (((b.coordPc.get(ho))[0] != list(w.coordPe.get('tw0'))[0]) or reib[0] != (b.coordPc.get(ho))[0])):
                    if (movePx[0]+75,movePx[1]+75) in w.coordPc.values() or (movePx[0]+75,movePx[1]+75) in w.coordPe.values():
                        avaible_move.append((movePx[0]+75,movePx[1]+75))
                    if (movePx[0]-75,movePx[1]+75) in w.coordPc.values() or (movePx[0]-75,movePx[1]+75) in w.coordPe.values():
                        avaible_move.append((movePx[0]-75,movePx[1]+75))
                    
                    


                    if elPBe == 1 and ho == elP:
                        avaible_move.append((movePx[0]-75,movePx[1]+75))
                    elif elPBr == 1 and ho == elP:
                        avaible_move.append((movePx[0]+75,movePx[1]+75))
                
                else:
                    if ((movePx[0]+75,movePx[1]+75) == (w.coordPe.get('qw0')))  or ((movePx[0]+75,movePx[1]+75) == (w.coordPe.get('tw0'))) or ((movePx[0]+75,movePx[1]+75) == (w.coordPe.get('bw0'))) or ((movePx[0]+75,movePx[1]+75) == (w.coordPe.get('tw1'))) or ((movePx[0]+75,movePx[1]+75) == (w.coordPe.get('bw1'))) or ((movePx[0]+75,movePx[1]+75) in (w.coordPc.values())):
                        avaible_move.append((movePx[0]+75,movePx[1]+75))
                    elif ((movePx[0]-75,movePx[1]+75) == (w.coordPe.get('qw0'))) or ((movePx[0]-75,movePx[1]+75) == (w.coordPe.get('tw0'))) or ((movePx[0]-75,movePx[1]+75) == (w.coordPe.get('bw0'))) or ((movePx[0]-75,movePx[1]+75) == (w.coordPe.get('tw1'))) or ((movePx[0]-75,movePx[1]+75) == (w.coordPe.get('bw1'))) or ((movePx[0]-75,movePx[1]+75) in (w.coordPc.values())):
                        avaible_move.append((movePx[0]-75,movePx[1]+75))
                
        ###########################
            if ho[0:2] == 'hw':
                #print(ho)
                check_pos_moveDW(ho,reiw,w,b)
                #print(bw)
                if bw == 1:# or ((w.coordPe.get(ho)) in list(avaible_move_dictB.get('qb0')) and (w.coordPe.get(ho))[1] == reiw[1] and (w.coordPe.get(ho))[1] == list(b.coordPe.get('qb0'))[1]) or ((w.coordPe.get(ho)) in list(avaible_move_dictB.get('tb0'))) and (w.coordPe.get(ho))[1] == reiw[1] and (w.coordPe.get(ho))[1] == list(b.coordPe.get('tb0'))[1] or ((w.coordPe.get(ho)) in list(avaible_move_dictB.get('tb1'))) and (w.coordPe.get(ho))[1] == reiw[1] and (w.coordPe.get(ho))[1] == list(b.coordPe.get('tb1'))[1]:
                    pass
                    """ elif bw == 1:# or ((w.coordPe.get(ho)) in list(avaible_move_dictB.get('qb0')) and (w.coordPe.get(ho))[0] == reiw[0] and (w.coordPe.get(ho))[0] == list(b.coordPe.get('qb0'))[0]) or ((w.coordPe.get(ho)) in list(avaible_move_dictB.get('tb0'))) and (w.coordPe.get(ho))[0] == reiw[0] and (w.coordPe.get(ho))[0] == list(b.coordPe.get('tb0'))[0] or ((w.coordPe.get(ho)) in list(avaible_move_dictB.get('tb1'))) and (w.coordPe.get(ho))[0] == reiw[0] and (w.coordPe.get(ho))[0] == list(b.coordPe.get('tb1'))[0]:
                    pass
                #Frente e tras """
                else:
                    if(movePx[0]+75,movePx[1]-150) not in w.coordPc.values() and (movePx[0]+75,movePx[1]-150) not in w.coordPe.values():
                        avaible_move.append((movePx[0]+75,movePx[1]-150))
                    else:
                        if get_key_by_value(w.coordPc,(movePx[0]+75,movePx[1]-150)) not in defense_pw and get_key_by_value(w.coordPc,(movePx[0]+75,movePx[1]-150)) != None:
                            defense_pw.append(get_key_by_value(w.coordPc,(movePx[0]+75,movePx[1]-150)))
                        if get_key_by_value(w.coordPe,(movePx[0]+75,movePx[1]-150)) not in defense_pw and get_key_by_value(w.coordPe,(movePx[0]+75,movePx[1]-150)) != None:
                            defense_pw.append(get_key_by_value(w.coordPe,(movePx[0]+75,movePx[1]-150)))

                    if(movePx[0]-75,movePx[1]-150) not in w.coordPc.values() and (movePx[0]-75,movePx[1]-150) not in w.coordPe.values():
                        avaible_move.append((movePx[0]-75,movePx[1]-150))
                    else:
                        if get_key_by_value(w.coordPc,(movePx[0]-75,movePx[1]-150)) not in defense_pw and get_key_by_value(w.coordPc,(movePx[0]-75,movePx[1]-150)) != None:
                            defense_pw.append(get_key_by_value(w.coordPc,(movePx[0]-75,movePx[1]-150)))
                        if get_key_by_value(w.coordPe,(movePx[0]-75,movePx[1]-150)) not in defense_pw and get_key_by_value(w.coordPe,(movePx[0]-75,movePx[1]-150)) != None:
                            defense_pw.append(get_key_by_value(w.coordPe,(movePx[0]-75,movePx[1]-150)))


                    if(movePx[0]+75,movePx[1]+150) not in w.coordPc.values() and (movePx[0]+75,movePx[1]+150) not in w.coordPe.values():
                        avaible_move.append((movePx[0]+75,movePx[1]+150))
                    else:
                        ###########clear
                        if get_key_by_value(w.coordPc,(movePx[0]+75,movePx[1]+150)) not in defense_pw and get_key_by_value(w.coordPc,(movePx[0]+75,movePx[1]+150)) != None:
                            defense_pw.append(get_key_by_value(w.coordPc,(movePx[0]+75,movePx[1]+150)))
                        if get_key_by_value(w.coordPe,(movePx[0]+75,movePx[1]+150)) not in defense_pw and get_key_by_value(w.coordPe,(movePx[0]+75,movePx[1]+150)) != None:
                            defense_pw.append(get_key_by_value(w.coordPe,(movePx[0]+75,movePx[1]+150)))
                            

                    if(movePx[0]-75,movePx[1]+150) not in w.coordPc.values() and (movePx[0]-75,movePx[1]+150) not in w.coordPe.values():
                        avaible_move.append((movePx[0]-75,movePx[1]+150))
                    else:
                        if get_key_by_value(w.coordPc,(movePx[0]-75,movePx[1]+150)) not in defense_pw and get_key_by_value(w.coordPc,(movePx[0]-75,movePx[1]+150)) != None:
                            defense_pw.append(get_key_by_value(w.coordPc,(movePx[0]-75,movePx[1]+150)))
                        if get_key_by_value(w.coordPe,(movePx[0]-75,movePx[1]+150)) not in defense_pw and get_key_by_value(w.coordPe,(movePx[0]-75,movePx[1]+150)) != None:
                            defense_pw.append(get_key_by_value(w.coordPe,(movePx[0]-75,movePx[1]+150)))

                    #Diagonais
                    if(movePx[0]-150,movePx[1]-75) not in w.coordPc.values() and (movePx[0]-150,movePx[1]-75) not in w.coordPe.values():
                        avaible_move.append((movePx[0]-150,movePx[1]-75))
                    else:
                        if get_key_by_value(w.coordPc,(movePx[0]-150,movePx[1]-75)) not in defense_pw and get_key_by_value(w.coordPc,(movePx[0]-150,movePx[1]-75)) != None:
                            defense_pw.append(get_key_by_value(w.coordPc,(movePx[0]-150,movePx[1]-75)))
                        if get_key_by_value(w.coordPe,(movePx[0]-150,movePx[1]-75)) not in defense_pw and get_key_by_value(w.coordPe,(movePx[0]-150,movePx[1]-75)) != None:
                            defense_pw.append(get_key_by_value(w.coordPe,(movePx[0]-150,movePx[1]-75)))
                    
                    if(movePx[0]+150,movePx[1]-75) not in w.coordPc.values() and (movePx[0]+150,movePx[1]-75) not in w.coordPe.values():
                        avaible_move.append((movePx[0]+150,movePx[1]-75))
                    else:
                        if get_key_by_value(w.coordPc,(movePx[0]+150,movePx[1]-75)) not in defense_pw and get_key_by_value(w.coordPc,(movePx[0]+150,movePx[1]-75)) != None:
                            defense_pw.append(get_key_by_value(w.coordPc,(movePx[0]+150,movePx[1]-75)))
                        if get_key_by_value(w.coordPe,(movePx[0]+150,movePx[1]-75)) not in defense_pw and get_key_by_value(w.coordPe,(movePx[0]+150,movePx[1]-75)) != None:
                            defense_pw.append(get_key_by_value(w.coordPe,(movePx[0]+150,movePx[1]-75)))

                    if(movePx[0]-150,movePx[1]+75) not in w.coordPc.values() and (movePx[0]-150,movePx[1]+75) not in w.coordPe.values():
                        avaible_move.append((movePx[0]-150,movePx[1]+75))
                    else:
                        if get_key_by_value(w.coordPc,(movePx[0]-150,movePx[1]+75)) not in defense_pw and get_key_by_value(w.coordPc,(movePx[0]-150,movePx[1]+75)) != None:
                            defense_pw.append(get_key_by_value(w.coordPc,(movePx[0]-150,movePx[1]+75)))
                        if get_key_by_value(w.coordPe,(movePx[0]-150,movePx[1]+75)) not in defense_pw and get_key_by_value(w.coordPe,(movePx[0]-150,movePx[1]+75)) != None:
                            defense_pw.append(get_key_by_value(w.coordPe,(movePx[0]-150,movePx[1]+75)))

                    if(movePx[0]+150,movePx[1]+75) not in w.coordPc.values() and (movePx[0]+150,movePx[1]+75) not in w.coordPe.values():
                        avaible_move.append((movePx[0]+150,movePx[1]+75))
                    else:
                        if get_key_by_value(w.coordPc,(movePx[0]+150,movePx[1]+75)) not in defense_pw and get_key_by_value(w.coordPc,(movePx[0]+150,movePx[1]+75)) != None:
                            defense_pw.append(get_key_by_value(w.coordPc,(movePx[0]+150,movePx[1]+75)))
        
            if ho[0:2] == 'hb':
                check_pos_moveDB(ho,reib,b,w)
                if bp == 1 :#or ((b.coordPe.get(ho)) in list(avaible_move_dictW.get('qw0')) and (b.coordPe.get(ho))[1] == reib[1] and (b.coordPe.get(ho))[1] == list(w.coordPe.get('qw0'))[1]) or ((b.coordPe.get(ho)) in list(avaible_move_dictW.get('tw0'))) and (b.coordPe.get(ho))[1] == reib[1] and (b.coordPe.get(ho))[1] == list(w.coordPe.get('tw0'))[1] and (b.coordPe.get(ho))[1] == reib[1] and (b.coordPe.get(ho))[1] == list(w.coordPe.get('tw1'))[1]:
                    pass
                    """ elif bp == 1 or ((b.coordPe.get(ho)) in list(avaible_move_dictW.get('qw0')) and (b.coordPe.get(ho))[0] == reib[0] and (b.coordPe.get(ho))[0] == list(w.coordPe.get('qw0'))[0]) or ((b.coordPe.get(ho)) in list(avaible_move_dictW.get('tw0'))) and (b.coordPe.get(ho))[0] == reib[0] and (b.coordPe.get(ho))[0] == list(w.coordPe.get('tw0'))[0] and (b.coordPe.get(ho))[0] == reib[0] and (b.coordPe.get(ho))[0] == list(w.coordPe.get('tw1'))[0]:
                    pass """
                else:
                #Diagonais
                    if(movePx[0]-150,movePx[1]+75) not in b.coordPc.values() and (movePx[0]-150,movePx[1]+75) not in b.coordPe.values():
                        avaible_move.append((movePx[0]-150,movePx[1]+75))
                    else:
                        if get_key_by_value(b.coordPc,(movePx[0]-150,movePx[1]+75)) not in defense_pb and get_key_by_value(b.coordPc,(movePx[0]-150,movePx[1]+75)) != None:
                            defense_pb.append(get_key_by_value(b.coordPc,(movePx[0]-150,movePx[1]+75)))
                        if get_key_by_value(b.coordPe,(movePx[0]-150,movePx[1]+75)) not in defense_pb and get_key_by_value(b.coordPe,(movePx[0]-150,movePx[1]+75)) != None:
                            defense_pb.append(get_key_by_value(b.coordPe,(movePx[0]-150,movePx[1]+75)))

                    if(movePx[0]+150,movePx[1]+75) not in b.coordPc.values() and (movePx[0]+150,movePx[1]+75) not in b.coordPe.values():
                        avaible_move.append((movePx[0]+150,movePx[1]+75))
                    else:
                        if get_key_by_value(b.coordPc,(movePx[0]+150,movePx[1]+75)) not in defense_pb and get_key_by_value(b.coordPc,(movePx[0]+150,movePx[1]+75)) != None:
                            defense_pb.append(get_key_by_value(b.coordPc,(movePx[0]+150,movePx[1]+75)))
                        if get_key_by_value(b.coordPe,(movePx[0]+150,movePx[1]+75)) not in defense_pb and get_key_by_value(b.coordPe,(movePx[0]+150,movePx[1]+75)) != None:
                            defense_pb.append(get_key_by_value(b.coordPe,(movePx[0]+150,movePx[1]+75)))

                    if(movePx[0]-150,movePx[1]-75)  not in b.coordPc.values() and (movePx[0]-150,movePx[1]-75) not in b.coordPe.values():
                        avaible_move.append((movePx[0]-150,movePx[1]-75))
                    else:
                        if get_key_by_value(b.coordPc,(movePx[0]-150,movePx[1]-75)) not in defense_pb and get_key_by_value(b.coordPc,(movePx[0]-150,movePx[1]-75)) != None:
                            defense_pb.append(get_key_by_value(b.coordPc,(movePx[0]-150,movePx[1]-75)))
                        if get_key_by_value(b.coordPe,(movePx[0]-150,movePx[1]-75)) not in defense_pb and get_key_by_value(b.coordPe,(movePx[0]-150,movePx[1]-75)) != None:
                            defense_pb.append(get_key_by_value(b.coordPe,(movePx[0]-150,movePx[1]-75)))

                    if(movePx[0]+150,movePx[1]-75) not in b.coordPc.values() and (movePx[0]+150,movePx[1]-75) not in b.coordPe.values():
                        avaible_move.append((movePx[0]+150,movePx[1]-75))
                    else:
                        if get_key_by_value(b.coordPc,(movePx[0]+150,movePx[1]-75)) not in defense_pb and get_key_by_value(b.coordPc,(movePx[0]+150,movePx[1]-75)) != None:
                            defense_pb.append(get_key_by_value(b.coordPc,(movePx[0]+150,movePx[1]-75)))
                        if get_key_by_value(b.coordPe,(movePx[0]+150,movePx[1]-75)) not in defense_pb and get_key_by_value(b.coordPe,(movePx[0]+150,movePx[1]-75)) != None:
                            defense_pb.append(get_key_by_value(b.coordPe,(movePx[0]+150,movePx[1]-75)))
                    
                    #Frente e tras
                    if(movePx[0]+75,movePx[1]+150) not in b.coordPc.values() and (movePx[0]+75,movePx[1]+150) not in b.coordPe.values():
                        avaible_move.append((movePx[0]+75,movePx[1]+150))
                    else:
                        if get_key_by_value(b.coordPc,(movePx[0]+75,movePx[1]+150)) not in defense_pb and get_key_by_value(b.coordPc,(movePx[0]+75,movePx[1]+150)) != None:
                            defense_pb.append(get_key_by_value(b.coordPc,(movePx[0]+75,movePx[1]+150)))
                        if get_key_by_value(b.coordPe,(movePx[0]+75,movePx[1]+150)) not in defense_pb and get_key_by_value(b.coordPe,(movePx[0]+75,movePx[1]+150)) != None:
                            defense_pb.append(get_key_by_value(b.coordPe,(movePx[0]+75,movePx[1]+150)))

                    if(movePx[0]-75,movePx[1]+150) not in b.coordPc.values() and (movePx[0]-75,movePx[1]+150) not in b.coordPe.values():
                        avaible_move.append((movePx[0]-75,movePx[1]+150))
                    else:
                        if get_key_by_value(b.coordPc,(movePx[0]-75,movePx[1]+150)) not in defense_pb and get_key_by_value(b.coordPc,(movePx[0]-75,movePx[1]+150)) != None:
                            defense_pb.append(get_key_by_value(b.coordPc,(movePx[0]-75,movePx[1]+150)))
                        if get_key_by_value(b.coordPe,(movePx[0]-75,movePx[1]+150)) not in defense_pb and get_key_by_value(b.coordPe,(movePx[0]-75,movePx[1]+150)) != None:
                            defense_pb.append(get_key_by_value(b.coordPe,(movePx[0]-75,movePx[1]+150)))

                    if(movePx[0]+75,movePx[1]-150) not in b.coordPc.values() and (movePx[0]+75,movePx[1]-150) not in b.coordPe.values():
                        avaible_move.append((movePx[0]+75,movePx[1]-150))
                    else:
                        if get_key_by_value(b.coordPc,(movePx[0]+75,movePx[1]-150)) not in defense_pb and get_key_by_value(b.coordPc,(movePx[0]+75,movePx[1]-150)) != None:
                            defense_pb.append(get_key_by_value(b.coordPc,(movePx[0]+75,movePx[1]-150)))
                        if get_key_by_value(b.coordPe,(movePx[0]+75,movePx[1]-150)) not in defense_pb and get_key_by_value(b.coordPe,(movePx[0]+75,movePx[1]-150)) != None:
                            defense_pb.append(get_key_by_value(b.coordPe,(movePx[0]+75,movePx[1]-150)))

                    if(movePx[0]-75,movePx[1]-150) not in b.coordPc.values() and (movePx[0]-75,movePx[1]-150) not in b.coordPe.values():
                        avaible_move.append((movePx[0]-75,movePx[1]-150))
                    else:
                        if get_key_by_value(b.coordPc,(movePx[0]-75,movePx[1]-150)) not in defense_pb and get_key_by_value(b.coordPc,(movePx[0]-75,movePx[1]-150)) != None:
                            defense_pb.append(get_key_by_value(b.coordPc,(movePx[0]-75,movePx[1]-150)))
                        if get_key_by_value(b.coordPe,(movePx[0]-75,movePx[1]-150)) not in defense_pb and get_key_by_value(b.coordPe,(movePx[0]-75,movePx[1]-150)) != None:
                            defense_pb.append(get_key_by_value(b.coordPe,(movePx[0]-75,movePx[1]-150)))
        
            if ho[0:2] == 'bw':
                peca = check_pos_moveDW(ho,reiw,w,b)
                #print(peca)
                pd =0
                
                if bw == 1:
                    for i in range(75,600,75):
                        if (list(b.coordPe.get(peca))[0] < movePx[0] and list(b.coordPe.get(peca))[1] < movePx[1]):
                            if ((movePx[0]-i,movePx[1]-i)) != (b.coordPe.get(peca)[0]-75,b.coordPe.get(peca)[1]-75):
                                avaible_move.append((movePx[0]-i,movePx[1]-i))
                            
                            if ((movePx[0]+i,movePx[1]+i)) != (reiw[0],reiw[1]):
                                if pd ==0:
                                    avaible_move.append((movePx[0]+i,movePx[1]+i))
                            else:
                                pd = 1

                        if (list(b.coordPe.get(peca))[0] > movePx[0] and list(b.coordPe.get(peca))[1] < movePx[1]):
                            if ((movePx[0]+i,movePx[1]-i)) != (b.coordPe.get(peca)[0]+75,b.coordPe.get(peca)[1]-75):
                                avaible_move.append((movePx[0]+i,movePx[1]-i))
                            
                            if ((movePx[0]-i,movePx[1]+i)) != (reiw[0],reiw[1]):
                                if pd ==0:
                                    avaible_move.append((movePx[0]-i,movePx[1]+i))
                                else:
                                    pd = 1

                        if (list(b.coordPe.get(peca))[0] < movePx[0] and list(b.coordPe.get(peca))[1] > movePx[1]):
                            if ((movePx[0]-i,movePx[1]+i)) != (b.coordPe.get(peca)[0]-75,b.coordPe.get(peca)[1]+75):
                                avaible_move.append((movePx[0]-i,movePx[1]+i))
                            
                            if ((movePx[0]+i,movePx[1]-i)) != (reiw[0],reiw[1]):
                                if pd ==0:
                                    avaible_move.append((movePx[0]+i,movePx[1]-i))
                            else:
                                pd = 1
                        
                        if (list(b.coordPe.get(peca))[0] > movePx[0] and list(b.coordPe.get(peca))[1] > movePx[1]):
                            if ((movePx[0]+i,movePx[1]+i)) != (b.coordPe.get(peca)[0]+75,b.coordPe.get(peca)[1]+75):
                                avaible_move.append((movePx[0]+i,movePx[1]+i))
                            
                            if ((movePx[0]-i,movePx[1]-i)) != (reiw[0],reiw[1]):
                                if pd ==0:
                                    avaible_move.append((movePx[0]-i,movePx[1]-i))
                            else:
                                pd = 1
                    
                else:
                    for i in range(75,600,75):
                        if (movePx[0]-i,movePx[1]-i) not in w.coordPc.values() and (movePx[0]-i,movePx[1]-i) not in w.coordPe.values():
                            avaible_move.append((movePx[0]-i,movePx[1]-i))
                            if (movePx[0]-i,movePx[1]-i) in b.coordPc.values() or (movePx[0]-i,movePx[1]-i) in b.coordPe.values():
                                
                                break
                        else:
                            if (movePx[0]-i,movePx[1]-i) in w.coordPc.values():
                                defense_pw.append(get_key_by_value(w.coordPc,(movePx[0]-i,movePx[1]-i)))
                            if (movePx[0]-i,movePx[1]-i) in w.coordPe.values():
                                defense_pw.append(get_key_by_value(w.coordPe,(movePx[0]-i,movePx[1]-i)))
                            break

                    for i in range(75,600,75):
                        if (movePx[0]+i,movePx[1]-i)  not in w.coordPc.values() and (movePx[0]+i,movePx[1]-i) not in w.coordPe.values():
                            avaible_move.append((movePx[0]+i,movePx[1]-i))
                            if (movePx[0]+i,movePx[1]-i) in b.coordPc.values() or (movePx[0]+i,movePx[1]-i) in b.coordPe.values():
                                break
                        else:
                            if (movePx[0]+i,movePx[1]-i) in w.coordPc.values():
                                defense_pw.append(get_key_by_value(w.coordPc,(movePx[0]+i,movePx[1]-i)))
                            if (movePx[0]+i,movePx[1]-i) in w.coordPe.values():
                                defense_pw.append(get_key_by_value(w.coordPe,(movePx[0]+i,movePx[1]-i)))
                            break

                    for i in range(75,600,75):
                        if (movePx[0]-i,movePx[1]+i)  not in w.coordPc.values() and (movePx[0]-i,movePx[1]+i) not in w.coordPe.values():
                            avaible_move.append((movePx[0]-i,movePx[1]+i))
                            if (movePx[0]-i,movePx[1]+i) in b.coordPc.values() or (movePx[0]-i,movePx[1]+i) in b.coordPe.values():
                                break
                        else:
                            if (movePx[0]-i,movePx[1]+i) in w.coordPc.values():
                                defense_pw.append(get_key_by_value(w.coordPc,(movePx[0]-i,movePx[1]+i)))
                            if (movePx[0]-i,movePx[1]+i) in w.coordPe.values():
                                defense_pw.append(get_key_by_value(w.coordPe,(movePx[0]-i,movePx[1]+i)))
                            break
                    
                    for i in range(75,600,75):
                        if (movePx[0]+i,movePx[1]+i)  not in w.coordPc.values() and (movePx[0]+i,movePx[1]+i) not in w.coordPe.values():
                            avaible_move.append((movePx[0]+i,movePx[1]+i))
                            if (movePx[0]+i,movePx[1]+i) in b.coordPc.values() or (movePx[0]+i,movePx[1]+i) in b.coordPe.values():
                                break
                        else:
                            if (movePx[0]+i,movePx[1]+i) in w.coordPc.values():
                                defense_pw.append(get_key_by_value(w.coordPc,(movePx[0]+i,movePx[1]+i)))
                            if (movePx[0]+i,movePx[1]+i) in w.coordPe.values():
                                defense_pw.append(get_key_by_value(w.coordPe,(movePx[0]+i,movePx[1]+i)))
                            break
                        
            elif ho[0:2] == 'bb':
                peca = check_pos_moveDB(ho,reib,b,w)
                pd = 0
                #print(peca)
                if bp == 1:
                    for i in range(75,600,75):
                        if (list(w.coordPe.get(peca))[0] < movePx[0] and list(w.coordPe.get(peca))[1] < movePx[1]):

                            if ((movePx[0]-i,movePx[1]-i)) != (w.coordPe.get(peca)[0]-75,w.coordPe.get(peca)[1]-75):
                                avaible_move.append((movePx[0]-i,movePx[1]-i))
                            
                            if ((movePx[0]+i,movePx[1]+i)) != (reib[0],reib[1]):
                                if pd ==0:
                                    avaible_move.append((movePx[0]+i,movePx[1]+i))
                            else:
                                pd = 1

                        if (list(w.coordPe.get(peca))[0] > movePx[0] and list(w.coordPe.get(peca))[1] < movePx[1]):

                            if ((movePx[0]+i,movePx[1]-i)) != (w.coordPe.get(peca)[0]+75,w.coordPe.get(peca)[1]-75):
                                avaible_move.append((movePx[0]+i,movePx[1]-i))
                            
                            if ((movePx[0]-i,movePx[1]+i)) != (reib[0],reib[1]):
                                if pd ==0:
                                    avaible_move.append((movePx[0]-i,movePx[1]+i))
                            else:
                                pd =1

                        if (list(w.coordPe.get(peca))[0] < movePx[0] and list(w.coordPe.get(peca))[1] > movePx[1]):
                           
                            if ((movePx[0]-i,movePx[1]+i)) != (w.coordPe.get(peca)[0]-75,w.coordPe.get(peca)[1]+75):
                                avaible_move.append((movePx[0]-i,movePx[1]+i))
                            
                            if ((movePx[0]+i,movePx[1]-i)) != (reib[0],reib[1]):
                                if pd ==0:
                                    avaible_move.append((movePx[0]+i,movePx[1]-i))
                            else:
                                pd =1

                        if (list(w.coordPe.get(peca))[0] > movePx[0] and list(w.coordPe.get(peca))[1] > movePx[1]):

                            if ((movePx[0]+i,movePx[1]+i)) != (w.coordPe.get(peca)[0]+75,w.coordPe.get(peca)[1]+75):
                                avaible_move.append((movePx[0]+i,movePx[1]+i))
                            
                            if ((movePx[0]-i,movePx[1]-i)) != (reib[0],reib[1]):
                                if pd ==0:
                                    avaible_move.append((movePx[0]-i,movePx[1]-i))
                            else:
                                pd =1

                        
                else:
                    for i in range(75,600,75):
                        if (movePx[0]-i,movePx[1]-i) not in b.coordPc.values() and (movePx[0]-i,movePx[1]-i) not in b.coordPe.values():
                            avaible_move.append((movePx[0]-i,movePx[1]-i))
                            if (movePx[0]-i,movePx[1]-i) in w.coordPc.values() or (movePx[0]-i,movePx[1]-i) in w.coordPe.values():
                                break
                        else:
                            if (movePx[0]-i,movePx[1]-i) in b.coordPc.values():
                                defense_pb.append(get_key_by_value(b.coordPc,(movePx[0]-i,movePx[1]-i)))
                            if (movePx[0]-i,movePx[1]-i) in b.coordPe.values():
                                defense_pb.append(get_key_by_value(b.coordPe,(movePx[0]-i,movePx[1]-i)))
                            break

                    for i in range(75,600,75):
                        if (movePx[0]+i,movePx[1]-i)  not in b.coordPc.values() and (movePx[0]+i,movePx[1]-i) not in b.coordPe.values():
                            avaible_move.append((movePx[0]+i,movePx[1]-i))
                            if (movePx[0]+i,movePx[1]-i) in w.coordPc.values() or (movePx[0]+i,movePx[1]-i) in w.coordPe.values():
                                break
                        else:
                            if (movePx[0]+i,movePx[1]-i) in b.coordPc.values():
                                defense_pb.append(get_key_by_value(b.coordPc,(movePx[0]+i,movePx[1]-i)))
                            if (movePx[0]+i,movePx[1]-i) in b.coordPe.values():
                                defense_pb.append(get_key_by_value(b.coordPe,(movePx[0]+i,movePx[1]-i)))
                            break

                    for i in range(75,600,75):
                        if (movePx[0]-i,movePx[1]+i)  not in b.coordPc.values() and (movePx[0]-i,movePx[1]+i) not in b.coordPe.values():
                            avaible_move.append((movePx[0]-i,movePx[1]+i))
                            if (movePx[0]-i,movePx[1]+i) in w.coordPc.values() or (movePx[0]-i,movePx[1]+i) in w.coordPe.values():
                                break
                        else:
                            if (movePx[0]-i,movePx[1]+i) in b.coordPc.values():
                                defense_pb.append(get_key_by_value(b.coordPc,(movePx[0]-i,movePx[1]+i)))
                            if (movePx[0]-i,movePx[1]+i) in b.coordPe.values():
                                defense_pb.append(get_key_by_value(b.coordPe,(movePx[0]-i,movePx[1]+i)))
                            break
                    
                    for i in range(75,600,75):
                        if (movePx[0]+i,movePx[1]+i)  not in b.coordPc.values() and (movePx[0]+i,movePx[1]+i) not in b.coordPe.values():
                            avaible_move.append((movePx[0]+i,movePx[1]+i))
                            if (movePx[0]+i,movePx[1]+i) in w.coordPc.values() or (movePx[0]+i,movePx[1]+i) in w.coordPe.values():
                                break
                        else:
                            if (movePx[0]+i,movePx[1]+i) in b.coordPc.values():
                                defense_pb.append(get_key_by_value(b.coordPc,(movePx[0]+i,movePx[1]+i)))
                            if (movePx[0]+i,movePx[1]+i) in b.coordPe.values():
                                defense_pb.append(get_key_by_value(b.coordPe,(movePx[0]+i,movePx[1]+i)))
                            break

            elif ho[0:2] == 'tw':
                peca =check_pos_moveDW(ho,reiw,w,b)
                
                pd,pdw,ed,edw =0,0,0,0
                td,tdw,rd,rdw =0,0,0,0
                #print(peca)
                if bw == 1:
                    for i in range(75,600,75):
                        if list(b.coordPe.get(peca))[0] == movePx[0] and edw ==0 and ed ==0 and list(b.coordPe.get(peca))[1] < reiw[1]:# and list(b.coordPe.get(peca))[1] < movePx[1]:
                            
                            if ((movePx[0],movePx[1]-i)) != (b.coordPe.get(peca)[0],b.coordPe.get(peca)[1]-75):# and pd ==0:# or ((movePx[0],movePx[1]-i)) == (reiw[0],reiw[1]-75):
                                #print((b.coordPe.get(peca)))
                                if pd == 0:
                                    avaible_move.append((movePx[0],movePx[1]-i))
                            else:
                                pd =1
                            if (movePx[0],movePx[1]+i) != (reiw[0],reiw[1]):
                                if pdw == 0:
                                    avaible_move.append((movePx[0],movePx[1]+i))
                            else:
                                pdw =1

                        if list(b.coordPe.get(peca))[0] == movePx[0] and pdw ==0 and pd ==0 and list(b.coordPe.get(peca))[1] > reiw[1]:# and list(b.coordPe.get(peca))[1] > movePx[1]:
                            if ((movePx[0],movePx[1]+i)) != (b.coordPe.get(peca)[0],b.coordPe.get(peca)[1]+75):# or ((movePx[0],movePx[1]-i)) == (reiw[0],reiw[1]-75):
                                #print((b.coordPe.get(peca)))
                                if ed == 0:
                                    avaible_move.append((movePx[0],movePx[1]+i))
                            else:
                                ed =1
                            if (movePx[0],movePx[1]-i) != (reiw[0],reiw[1]):
                                if edw == 0:
                                    avaible_move.append((movePx[0],movePx[1]-i))
                            else:
                                edw =1

                        if list(b.coordPe.get(peca))[1] == movePx[1] and rd==0 and rdw==0 and list(b.coordPe.get(peca))[0] < reib[0]:#list(b.coordPe.get(peca))[0] < movePx[0] and 
                            
                            if ((movePx[0]-i,movePx[1])) != (b.coordPe.get(peca)[0]-75,b.coordPe.get(peca)[1]):# or ((movePx[0],movePx[1]-i)) == (reiw[0],reiw[1]-75):
                                #print((b.coordPe.get(peca)))
                                if td == 0:
                                    avaible_move.append((movePx[0]-i,movePx[1]))
                            else:
                                td =1
                            if (movePx[0]+i,movePx[1]) != (reiw[0],reiw[1]):
                                if tdw == 0:
                                    avaible_move.append((movePx[0]+i,movePx[1]))
                            else:
                                tdw =1

                        if list(b.coordPe.get(peca))[1] == movePx[1] and td ==0 and tdw ==0 and list(b.coordPe.get(peca))[0] > reib[0]:# and  list(b.coordPe.get(peca))[0] > movePx[0] 
                            if ((movePx[0]+i,movePx[1])) != (b.coordPe.get(peca)[0]+75,b.coordPe.get(peca)[1]):# or ((movePx[0],movePx[1]-i)) == (reiw[0],reiw[1]-75):
                                #print((b.coordPe.get(peca)))
                                if rd == 0:
                                    avaible_move.append((movePx[0]+i,movePx[1]))
                            else:
                                rd =1
                            if (movePx[0]-i,movePx[1]) != (reiw[0],reiw[1]):
                                if rdw == 0:
                                    avaible_move.append((movePx[0]-i,movePx[1]))
                            else:
                                rdw =1
                        

                else:
                    for i in range(75,600,75):
                        if (movePx[0],movePx[1]-i) not in w.coordPc.values() and (movePx[0],movePx[1]-i) not in w.coordPe.values():
                            avaible_move.append((movePx[0],movePx[1]-i))
                            if (movePx[0],movePx[1]-i) in b.coordPc.values() or (movePx[0],movePx[1]-i) in b.coordPe.values():
                                break
                        else:
                            if (movePx[0],movePx[1]-i) in w.coordPc.values():
                                defense_pw.append(get_key_by_value(w.coordPc,(movePx[0],movePx[1]-i)))
                            if (movePx[0],movePx[1]-i) in w.coordPe.values():
                                defense_pw.append(get_key_by_value(w.coordPe,(movePx[0],movePx[1]-i)))
                            break

                    for i in range(75,600,75):
                        if (movePx[0],movePx[1]+i)  not in w.coordPc.values() and (movePx[0],movePx[1]+i) not in w.coordPe.values():
                            avaible_move.append((movePx[0],movePx[1]+i))
                            if (movePx[0],movePx[1]+i) in b.coordPc.values() or (movePx[0],movePx[1]+i) in b.coordPe.values():
                                break
                        else:
                            if (movePx[0],movePx[1]+i) in w.coordPc.values():
                                defense_pw.append(get_key_by_value(w.coordPc,(movePx[0],movePx[1]+i)))
                            if (movePx[0],movePx[1]+i) in w.coordPe.values():
                                defense_pw.append(get_key_by_value(w.coordPe,(movePx[0],movePx[1]+i)))
                            break

                    for i in range(75,600,75):
                        if (movePx[0]-i,movePx[1])  not in w.coordPc.values() and (movePx[0]-i,movePx[1]) not in w.coordPe.values():
                            avaible_move.append((movePx[0]-i,movePx[1]))
                            if (movePx[0]-i,movePx[1]) in b.coordPc.values() or (movePx[0]-i,movePx[1]) in b.coordPe.values():
                                break
                        else:
                            if (movePx[0]-i,movePx[1]) in w.coordPc.values():
                                defense_pw.append(get_key_by_value(w.coordPc,(movePx[0]-i,movePx[1])))
                            if (movePx[0]-i,movePx[1]) in w.coordPe.values():
                                defense_pw.append(get_key_by_value(w.coordPe,(movePx[0]-i,movePx[1])))
                            break
                    
                    for i in range(75,600,75):
                        if (movePx[0]+i,movePx[1])  not in w.coordPc.values() and (movePx[0]+i,movePx[1]) not in w.coordPe.values():
                            avaible_move.append((movePx[0]+i,movePx[1]))
                            if (movePx[0]+i,movePx[1]) in b.coordPc.values() or (movePx[0]+i,movePx[1]) in b.coordPe.values():
                                break
                        else:
                            if (movePx[0]+i,movePx[1]) in w.coordPc.values():
                                defense_pw.append(get_key_by_value(w.coordPc,(movePx[0]+i,movePx[1])))
                            if (movePx[0]+i,movePx[1]) in w.coordPe.values():
                                defense_pw.append(get_key_by_value(w.coordPe,(movePx[0]+i,movePx[1])))
                            break

            elif ho[0:2] == 'tb':
                peca = check_pos_moveDB(ho,reib,b,w)
                pd,pdw,ed,edw =0,0,0,0
                td,tdw,rd,rdw =0,0,0,0
                #print(peca)
                if bp == 1:
                    for i in range(75,600,75):
                        
                        if list(w.coordPe.get(peca))[0] == movePx[0] and edw ==0 and ed ==0 and list(w.coordPe.get(peca))[1] < reib[1]:# and list(b.coordPe.get(peca))[1] < movePx[1]:
                            
                            if ((movePx[0],movePx[1]-i)) != (w.coordPe.get(peca)[0],w.coordPe.get(peca)[1]-75):# and pd ==0:# or ((movePx[0],movePx[1]-i)) == (reiw[0],reiw[1]-75):
                                #print((b.coordPe.get(peca)))
                                if pd == 0:
                                    avaible_move.append((movePx[0],movePx[1]-i))
                            else:
                                pd =1
                            if (movePx[0],movePx[1]+i) != (reib[0],reib[1]):
                                if pdw == 0:
                                    avaible_move.append((movePx[0],movePx[1]+i))
                            else:
                                pdw =1

                        if list(w.coordPe.get(peca))[0] == movePx[0] and pdw ==0 and pd ==0 and list(w.coordPe.get(peca))[1] > reib[1]:# and list(b.coordPe.get(peca))[1] > movePx[1]:
                            if ((movePx[0],movePx[1]+i)) != (w.coordPe.get(peca)[0],w.coordPe.get(peca)[1]+75):# or ((movePx[0],movePx[1]-i)) == (reiw[0],reiw[1]-75):
                                #print((b.coordPe.get(peca)))
                                if ed == 0:
                                    avaible_move.append((movePx[0],movePx[1]+i))
                            else:
                                ed =1
                            if (movePx[0],movePx[1]-i) != (reib[0],reib[1]):
                                if edw == 0:
                                    avaible_move.append((movePx[0],movePx[1]-i))
                            else:
                                edw =1

                        if list(w.coordPe.get(peca))[1] == movePx[1] and rd==0 and rdw==0 and list(w.coordPe.get(peca))[0] < reib[0]:#list(b.coordPe.get(peca))[0] < movePx[0] and 
                            
                            if ((movePx[0]-i,movePx[1])) != (w.coordPe.get(peca)[0]-75,w.coordPe.get(peca)[1]) :# or ((movePx[0],movePx[1]-i)) == (reiw[0],reiw[1]-75):
                                #print((b.coordPe.get(peca)))
                                if td == 0:
                                    avaible_move.append((movePx[0]-i,movePx[1]))
                            else:
                                td =1
                            if (movePx[0]+i,movePx[1]) != (reib[0],reib[1]):
                                if tdw == 0:
                                    avaible_move.append((movePx[0]+i,movePx[1]))
                            else:
                                tdw =1

                        if list(w.coordPe.get(peca))[1] == movePx[1] and td ==0 and tdw ==0  and list(w.coordPe.get(peca))[0] > reib[0]:# and  list(b.coordPe.get(peca))[0] > movePx[0] 
                            if ((movePx[0]+i,movePx[1])) != (w.coordPe.get(peca)[0]+75,w.coordPe.get(peca)[1]):# or ((movePx[0],movePx[1]-i)) == (reiw[0],reiw[1]-75):
                                #print((b.coordPe.get(peca)))
                                if rd == 0:
                                    avaible_move.append((movePx[0]+i,movePx[1]))
                            else:
                                rd =1
                            if (movePx[0]-i,movePx[1]) != (reib[0],reib[1]):
                                if rdw == 0:
                                    avaible_move.append((movePx[0]-i,movePx[1]))
                            else:
                                rdw =1

                else:
                    for i in range(75,600,75):
                        if (movePx[0],movePx[1]-i) not in b.coordPc.values() and (movePx[0],movePx[1]-i) not in b.coordPe.values():
                            avaible_move.append((movePx[0],movePx[1]-i))
                            if (movePx[0],movePx[1]-i) in w.coordPc.values() or (movePx[0],movePx[1]-i) in w.coordPe.values():
                                break
                        else:
                            if (movePx[0],movePx[1]-i) in b.coordPc.values():
                                defense_pb.append(get_key_by_value(b.coordPc,(movePx[0],movePx[1]-i)))
                            if (movePx[0],movePx[1]-i) in b.coordPe.values():
                                defense_pb.append(get_key_by_value(b.coordPe,(movePx[0],movePx[1]-i)))
                            break

                    for i in range(75,600,75):
                        if (movePx[0],movePx[1]+i)  not in b.coordPc.values() and (movePx[0],movePx[1]+i) not in b.coordPe.values():
                            avaible_move.append((movePx[0],movePx[1]+i))
                            if (movePx[0],movePx[1]+i) in w.coordPc.values() or (movePx[0],movePx[1]+i) in w.coordPe.values():
                                break
                        else:
                            if (movePx[0],movePx[1]+i) in b.coordPc.values():
                                defense_pb.append(get_key_by_value(b.coordPc,(movePx[0],movePx[1]+i)))
                            if (movePx[0],movePx[1]+i) in b.coordPe.values():
                                defense_pb.append(get_key_by_value(b.coordPe,(movePx[0],movePx[1]+i)))
                            break

                    for i in range(75,600,75):
                        if (movePx[0]-i,movePx[1])  not in b.coordPc.values() and (movePx[0]-i,movePx[1]) not in b.coordPe.values():
                            avaible_move.append((movePx[0]-i,movePx[1]))
                            if (movePx[0]-i,movePx[1]) in w.coordPc.values() or (movePx[0]-i,movePx[1]) in w.coordPe.values():
                                break
                        else:
                            if (movePx[0]-i,movePx[1]) in b.coordPc.values():
                                defense_pb.append(get_key_by_value(b.coordPc,(movePx[0]-i,movePx[1])))
                            if (movePx[0]-i,movePx[1]) in b.coordPe.values():
                                defense_pb.append(get_key_by_value(b.coordPe,(movePx[0]-i,movePx[1])))
                            break

                    for i in range(75,600,75):
                        if (movePx[0]+i,movePx[1])  not in b.coordPc.values() and (movePx[0]+i,movePx[1]) not in b.coordPe.values():
                            avaible_move.append((movePx[0]+i,movePx[1]))
                            if (movePx[0]+i,movePx[1]) in w.coordPc.values() or (movePx[0]+i,movePx[1]) in w.coordPe.values():
                                break
                        else:
                            if (movePx[0]+i,movePx[1]) in b.coordPc.values():
                                defense_pb.append(get_key_by_value(b.coordPc,(movePx[0]+i,movePx[1])))
                            if (movePx[0]+i,movePx[1]) in b.coordPe.values():
                                defense_pb.append(get_key_by_value(b.coordPe,(movePx[0]+i,movePx[1])))
                            break

            elif ho[0:2] == 'qw':
                peca = check_pos_moveDW(ho,reiw,w,b)
                pd,pdw,ed,edw =0,0,0,0
                td,tdw,rd,rdw =0,0,0,0
                cd =0
                #print(peca)
                if bw == 1:
                    for i in range(75,600,75):
                        if (list(b.coordPe.get(peca))[0] < movePx[0] and list(b.coordPe.get(peca))[1] < movePx[1]):
                            if ((movePx[0]-i,movePx[1]-i)) != (b.coordPe.get(peca)[0]-75,b.coordPe.get(peca)[1]-75):
                                avaible_move.append((movePx[0]-i,movePx[1]-i))
                            
                            if ((movePx[0]+i,movePx[1]+i)) != (reiw[0],reiw[1]):
                                if cd ==0:
                                    avaible_move.append((movePx[0]+i,movePx[1]+i))
                            else:
                                cd = 1

                        if (list(b.coordPe.get(peca))[0] > movePx[0] and list(b.coordPe.get(peca))[1] < movePx[1]):
                            if ((movePx[0]+i,movePx[1]-i)) != (b.coordPe.get(peca)[0]+75,b.coordPe.get(peca)[1]-75):
                                avaible_move.append((movePx[0]+i,movePx[1]-i))
                            
                            if ((movePx[0]-i,movePx[1]+i)) != (reiw[0],reiw[1]):
                                if cd ==0:
                                    avaible_move.append((movePx[0]-i,movePx[1]+i))
                                else:
                                    cd = 1

                        if (list(b.coordPe.get(peca))[0] < movePx[0] and list(b.coordPe.get(peca))[1] > movePx[1]):
                            if ((movePx[0]-i,movePx[1]+i)) != (b.coordPe.get(peca)[0]-75,b.coordPe.get(peca)[1]+75):
                                avaible_move.append((movePx[0]-i,movePx[1]+i))
                            
                            if ((movePx[0]+i,movePx[1]-i)) != (reiw[0],reiw[1]):
                                if cd ==0:
                                    avaible_move.append((movePx[0]+i,movePx[1]-i))
                            else:
                                cd = 1
                        
                        if (list(b.coordPe.get(peca))[0] > movePx[0] and list(b.coordPe.get(peca))[1] > movePx[1]):
                            if ((movePx[0]+i,movePx[1]+i)) != (b.coordPe.get(peca)[0]+75,b.coordPe.get(peca)[1]+75):
                                avaible_move.append((movePx[0]+i,movePx[1]+i))
                            
                            if ((movePx[0]-i,movePx[1]-i)) != (reiw[0],reiw[1]):
                                if cd ==0:
                                    avaible_move.append((movePx[0]-i,movePx[1]-i))
                            else:
                                cd = 1

                    #for i in range(75,600,75):
                        if list(b.coordPe.get(peca))[0] == movePx[0] and edw ==0 and ed ==0 and list(b.coordPe.get(peca))[1] < reiw[1]:# and list(b.coordPe.get(peca))[1] < movePx[1]:
                            
                            if ((movePx[0],movePx[1]-i)) != (b.coordPe.get(peca)[0],b.coordPe.get(peca)[1]-75):# and pd ==0:# or ((movePx[0],movePx[1]-i)) == (reiw[0],reiw[1]-75):
                                #print((b.coordPe.get(peca)))
                                if pd == 0:
                                    avaible_move.append((movePx[0],movePx[1]-i))
                            else:
                                pd =1
                            if (movePx[0],movePx[1]+i) != (reiw[0],reiw[1]):
                                if pdw == 0:
                                    avaible_move.append((movePx[0],movePx[1]+i))
                            else:
                                pdw =1

                        if list(b.coordPe.get(peca))[0] == movePx[0] and pdw ==0 and pd ==0 and list(b.coordPe.get(peca))[1] > reiw[1]:# and list(b.coordPe.get(peca))[1] > movePx[1]:
                            if ((movePx[0],movePx[1]+i)) != (b.coordPe.get(peca)[0],b.coordPe.get(peca)[1]+75):# or ((movePx[0],movePx[1]-i)) == (reiw[0],reiw[1]-75):
                                #print((b.coordPe.get(peca)))
                                if ed == 0:
                                    avaible_move.append((movePx[0],movePx[1]+i))
                            else:
                                ed =1
                            if (movePx[0],movePx[1]-i) != (reiw[0],reiw[1]):
                                if edw == 0:
                                    avaible_move.append((movePx[0],movePx[1]-i))
                            else:
                                edw =1

                        if list(b.coordPe.get(peca))[1] == movePx[1] and rd==0 and rdw==0 and list(b.coordPe.get(peca))[0] < reiw[0]:#list(b.coordPe.get(peca))[0] < movePx[0] and 
                            
                            if ((movePx[0]-i,movePx[1])) != (b.coordPe.get(peca)[0]-75,b.coordPe.get(peca)[1]):# or ((movePx[0],movePx[1]-i)) == (reiw[0],reiw[1]-75):
                                #print((b.coordPe.get(peca)))
                                if td == 0:
                                    avaible_move.append((movePx[0]-i,movePx[1]))
                            else:
                                td =1
                            if (movePx[0]+i,movePx[1]) != (reiw[0],reiw[1]):
                                if tdw == 0:
                                    avaible_move.append((movePx[0]+i,movePx[1]))
                            else:
                                tdw =1

                        if list(b.coordPe.get(peca))[1] == movePx[1] and td ==0 and tdw ==0 and list(b.coordPe.get(peca))[0] > reiw[0]:# and  list(b.coordPe.get(peca))[0] > movePx[0] 
                            if ((movePx[0]+i,movePx[1])) != (b.coordPe.get(peca)[0]+75,b.coordPe.get(peca)[1]):# or ((movePx[0],movePx[1]-i)) == (reiw[0],reiw[1]-75):
                                #print((b.coordPe.get(peca)))
                                if rd == 0:
                                    avaible_move.append((movePx[0]+i,movePx[1]))
                            else:
                                rd =1
                            if (movePx[0]-i,movePx[1]) != (reiw[0],reiw[1]):
                                if rdw == 0:
                                    avaible_move.append((movePx[0]-i,movePx[1]))
                            else:
                                rdw =1
                        
                else:
                #Diagonal
                    for i in range(75,600,75):
                        if (movePx[0]-i,movePx[1]-i) not in w.coordPc.values() and (movePx[0]-i,movePx[1]-i) not in w.coordPe.values():
                            avaible_move.append((movePx[0]-i,movePx[1]-i))
                            if (movePx[0]-i,movePx[1]-i) in b.coordPc.values() or (movePx[0]-i,movePx[1]-i) in b.coordPe.values():
                                
                                break
                        else:
                            if (movePx[0]-i,movePx[1]-i) in w.coordPc.values():
                                defense_pw.append(get_key_by_value(w.coordPc,(movePx[0]-i,movePx[1]-i)))
                            if (movePx[0]-i,movePx[1]-i) in w.coordPe.values():
                                defense_pw.append(get_key_by_value(w.coordPe,(movePx[0]-i,movePx[1]-i)))
                            break

                    for i in range(75,600,75):
                        if (movePx[0]+i,movePx[1]-i)  not in w.coordPc.values() and (movePx[0]+i,movePx[1]-i) not in w.coordPe.values():
                            avaible_move.append((movePx[0]+i,movePx[1]-i))
                            if (movePx[0]+i,movePx[1]-i) in b.coordPc.values() or (movePx[0]+i,movePx[1]-i) in b.coordPe.values():
                                break
                        else:
                            if (movePx[0]+i,movePx[1]-i) in w.coordPc.values():
                                defense_pw.append(get_key_by_value(w.coordPc,(movePx[0]+i,movePx[1]-i)))
                            if (movePx[0]+i,movePx[1]-i) in w.coordPe.values():
                                defense_pw.append(get_key_by_value(w.coordPe,(movePx[0]+i,movePx[1]-i)))
                            break

                    for i in range(75,600,75):
                        if (movePx[0]-i,movePx[1]+i)  not in w.coordPc.values() and (movePx[0]-i,movePx[1]+i) not in w.coordPe.values():
                            avaible_move.append((movePx[0]-i,movePx[1]+i))
                            if (movePx[0]-i,movePx[1]+i) in b.coordPc.values() or (movePx[0]-i,movePx[1]+i) in b.coordPe.values():
                                break
                        else:
                            if (movePx[0]-i,movePx[1]+i) in w.coordPc.values():
                                defense_pw.append(get_key_by_value(w.coordPc,(movePx[0]-i,movePx[1]+i)))
                            if (movePx[0]-i,movePx[1]+i) in w.coordPe.values():
                                defense_pw.append(get_key_by_value(w.coordPe,(movePx[0]-i,movePx[1]+i)))
                            break
                    
                    for i in range(75,600,75):
                        if (movePx[0]+i,movePx[1]+i)  not in w.coordPc.values() and (movePx[0]+i,movePx[1]+i) not in w.coordPe.values():
                            avaible_move.append((movePx[0]+i,movePx[1]+i))
                            if (movePx[0]+i,movePx[1]+i) in b.coordPc.values() or (movePx[0]+i,movePx[1]+i) in b.coordPe.values():
                                break
                        else:
                            if (movePx[0]+i,movePx[1]+i) in w.coordPc.values():
                                defense_pw.append(get_key_by_value(w.coordPc,(movePx[0]+i,movePx[1]+i)))
                            if (movePx[0]+i,movePx[1]+i) in w.coordPe.values():
                                defense_pw.append(get_key_by_value(w.coordPe,(movePx[0]+i,movePx[1]+i)))
                            break
                    ## Lados
                    for i in range(75,600,75):
                        if (movePx[0],movePx[1]-i) not in w.coordPc.values() and (movePx[0],movePx[1]-i) not in w.coordPe.values():
                            avaible_move.append((movePx[0],movePx[1]-i))
                            if (movePx[0],movePx[1]-i) in b.coordPc.values() or (movePx[0],movePx[1]-i) in b.coordPe.values():
                                break
                        else:
                            if (movePx[0],movePx[1]-i) in w.coordPc.values():
                                defense_pw.append(get_key_by_value(w.coordPc,(movePx[0],movePx[1]-i)))
                            if (movePx[0],movePx[1]-i) in w.coordPe.values():
                                defense_pw.append(get_key_by_value(w.coordPe,(movePx[0],movePx[1]-i)))
                            break

                    for i in range(75,600,75):
                        if (movePx[0],movePx[1]+i)  not in w.coordPc.values() and (movePx[0],movePx[1]+i) not in w.coordPe.values():
                            avaible_move.append((movePx[0],movePx[1]+i))
                            if (movePx[0],movePx[1]+i) in b.coordPc.values() or (movePx[0],movePx[1]+i) in b.coordPe.values():
                                break
                        else:
                            if (movePx[0],movePx[1]+i) in w.coordPc.values():
                                defense_pw.append(get_key_by_value(w.coordPc,(movePx[0],movePx[1]+i)))
                            if (movePx[0],movePx[1]+i) in w.coordPe.values():
                                defense_pw.append(get_key_by_value(w.coordPe,(movePx[0],movePx[1]+i)))
                            break

                    for i in range(75,600,75):
                        if (movePx[0]-i,movePx[1])  not in w.coordPc.values() and (movePx[0]-i,movePx[1]) not in w.coordPe.values():
                            avaible_move.append((movePx[0]-i,movePx[1]))
                            if (movePx[0]-i,movePx[1]) in b.coordPc.values() or (movePx[0]-i,movePx[1]) in b.coordPe.values():
                                break
                        else:
                            if (movePx[0]-i,movePx[1]) in w.coordPc.values():
                                defense_pw.append(get_key_by_value(w.coordPc,(movePx[0]-i,movePx[1])))
                            if (movePx[0]-i,movePx[1]) in w.coordPe.values():
                                defense_pw.append(get_key_by_value(w.coordPe,(movePx[0]-i,movePx[1])))
                            break
                    
                    for i in range(75,600,75):
                        if (movePx[0]+i,movePx[1])  not in w.coordPc.values() and (movePx[0]+i,movePx[1]) not in w.coordPe.values():
                            avaible_move.append((movePx[0]+i,movePx[1]))
                            if (movePx[0]+i,movePx[1]) in b.coordPc.values() or (movePx[0]+i,movePx[1]) in b.coordPe.values():
                                break
                        else:
                            if (movePx[0]+i,movePx[1]) in w.coordPc.values():
                                defense_pw.append(get_key_by_value(w.coordPc,(movePx[0]+i,movePx[1])))
                            if (movePx[0]+i,movePx[1]) in w.coordPe.values():
                                defense_pw.append(get_key_by_value(w.coordPe,(movePx[0]+i,movePx[1])))
                            break

            elif ho[0:2] == 'qb':
                peca = check_pos_moveDB(ho,reib,b,w)
                pd,pdw,ed,edw =0,0,0,0
                td,tdw,rd,rdw =0,0,0,0
                cd = 0
                #print(peca)
                if bp == 1:
                    for i in range(75,600,75):
                        if (list(w.coordPe.get(peca))[0] < movePx[0] and list(w.coordPe.get(peca))[1] < movePx[1]):

                            if ((movePx[0]-i,movePx[1]-i)) != (w.coordPe.get(peca)[0]-75,w.coordPe.get(peca)[1]-75):
                                avaible_move.append((movePx[0]-i,movePx[1]-i))
                            
                            if ((movePx[0]+i,movePx[1]+i)) != (reib[0],reib[1]):
                                if cd ==0:
                                    avaible_move.append((movePx[0]+i,movePx[1]+i))
                            else:
                                cd = 1

                        if (list(w.coordPe.get(peca))[0] > movePx[0] and list(w.coordPe.get(peca))[1] < movePx[1]):

                            if ((movePx[0]+i,movePx[1]-i)) != (w.coordPe.get(peca)[0]+75,w.coordPe.get(peca)[1]-75):
                                avaible_move.append((movePx[0]+i,movePx[1]-i))
                            
                            if ((movePx[0]-i,movePx[1]+i)) != (reib[0],reib[1]):
                                if cd ==0:
                                    avaible_move.append((movePx[0]-i,movePx[1]+i))
                            else:
                                cd =1

                        if (list(w.coordPe.get(peca))[0] < movePx[0] and list(w.coordPe.get(peca))[1] > movePx[1]):
                           
                            if ((movePx[0]-i,movePx[1]+i)) != (w.coordPe.get(peca)[0]-75,w.coordPe.get(peca)[1]+75):
                                avaible_move.append((movePx[0]-i,movePx[1]+i))
                            
                            if ((movePx[0]+i,movePx[1]-i)) != (reib[0],reib[1]):
                                if cd ==0:
                                    avaible_move.append((movePx[0]+i,movePx[1]-i))
                            else:
                                cd =1

                        if (list(w.coordPe.get(peca))[0] > movePx[0] and list(w.coordPe.get(peca))[1] > movePx[1]):

                            if ((movePx[0]+i,movePx[1]+i)) != (w.coordPe.get(peca)[0]+75,w.coordPe.get(peca)[1]+75):
                                avaible_move.append((movePx[0]+i,movePx[1]+i))
                            
                            if ((movePx[0]-i,movePx[1]-i)) != (reib[0],reib[1]):
                                if cd ==0:
                                    avaible_move.append((movePx[0]-i,movePx[1]-i))
                            else:
                                cd =1
                        ###

                        if list(w.coordPe.get(peca))[0] == movePx[0] and edw ==0 and ed ==0 and list(w.coordPe.get(peca))[1] < reib[1]:# and list(b.coordPe.get(peca))[1] < movePx[1]:
                            
                            if ((movePx[0],movePx[1]-i)) != (w.coordPe.get(peca)[0],w.coordPe.get(peca)[1]-75):# and pd ==0:# or ((movePx[0],movePx[1]-i)) == (reiw[0],reiw[1]-75):
                                #print((b.coordPe.get(peca)))
                                if pd == 0:
                                    avaible_move.append((movePx[0],movePx[1]-i))
                            else:
                                pd =1
                            if (movePx[0],movePx[1]+i) != (reib[0],reib[1]):
                                if pdw == 0:
                                    avaible_move.append((movePx[0],movePx[1]+i))
                            else:
                                pdw =1

                        if list(w.coordPe.get(peca))[0] == movePx[0] and pdw ==0 and pd ==0 and list(w.coordPe.get(peca))[1] > reib[1]:# and list(b.coordPe.get(peca))[1] > movePx[1]:
                            if ((movePx[0],movePx[1]+i)) != (w.coordPe.get(peca)[0],w.coordPe.get(peca)[1]+75):# or ((movePx[0],movePx[1]-i)) == (reiw[0],reiw[1]-75):
                                #print((b.coordPe.get(peca)))
                                if ed == 0:
                                    avaible_move.append((movePx[0],movePx[1]+i))
                            else:
                                ed =1
                            if (movePx[0],movePx[1]-i) != (reib[0],reib[1]):
                                if edw == 0:
                                    avaible_move.append((movePx[0],movePx[1]-i))
                            else:
                                edw =1

                        if list(w.coordPe.get(peca))[1] == movePx[1] and rd==0 and rdw==0 and list(w.coordPe.get(peca))[0] < reib[0]:#list(b.coordPe.get(peca))[0] < movePx[0] and 
                            
                            if ((movePx[0]-i,movePx[1])) != (w.coordPe.get(peca)[0]-75,w.coordPe.get(peca)[1]) :# or ((movePx[0],movePx[1]-i)) == (reiw[0],reiw[1]-75):
                                #print((b.coordPe.get(peca)))
                                if td == 0:
                                    avaible_move.append((movePx[0]-i,movePx[1]))
                            else:
                                td =1
                            if (movePx[0]+i,movePx[1]) != (reib[0],reib[1]):
                                if tdw == 0:
                                    avaible_move.append((movePx[0]+i,movePx[1]))
                            else:
                                tdw =1

                        if list(w.coordPe.get(peca))[1] == movePx[1] and td ==0 and tdw ==0  and list(w.coordPe.get(peca))[0] > reib[0]:# and  list(b.coordPe.get(peca))[0] > movePx[0] 
                            if ((movePx[0]+i,movePx[1])) != (w.coordPe.get(peca)[0]+75,w.coordPe.get(peca)[1]):# or ((movePx[0],movePx[1]-i)) == (reiw[0],reiw[1]-75):
                                #print((b.coordPe.get(peca)))
                                if rd == 0:
                                    avaible_move.append((movePx[0]+i,movePx[1]))
                            else:
                                rd =1
                            if (movePx[0]-i,movePx[1]) != (reib[0],reib[1]):
                                if rdw == 0:
                                    avaible_move.append((movePx[0]-i,movePx[1]))
                            else:
                                rdw =1
                else:
                #Diagonais
                    for i in range(75,600,75):
                        if (movePx[0]-i,movePx[1]-i) not in b.coordPc.values() and (movePx[0]-i,movePx[1]-i) not in b.coordPe.values():
                            avaible_move.append((movePx[0]-i,movePx[1]-i))
                            if (movePx[0]-i,movePx[1]-i) in w.coordPc.values() or (movePx[0]-i,movePx[1]-i) in w.coordPe.values():
                                break
                        else:
                            if (movePx[0]-i,movePx[1]-i) in b.coordPc.values():
                                defense_pb.append(get_key_by_value(b.coordPc,(movePx[0]-i,movePx[1]-i)))
                            if (movePx[0]-i,movePx[1]-i) in b.coordPe.values():
                                defense_pb.append(get_key_by_value(b.coordPe,(movePx[0]-i,movePx[1]-i)))
                            break

                    for i in range(75,600,75):
                        if (movePx[0]+i,movePx[1]-i)  not in b.coordPc.values() and (movePx[0]+i,movePx[1]-i) not in b.coordPe.values():
                            avaible_move.append((movePx[0]+i,movePx[1]-i))
                            if (movePx[0]+i,movePx[1]-i) in w.coordPc.values() or (movePx[0]+i,movePx[1]-i) in w.coordPe.values():
                                break
                        else:
                            if (movePx[0]+i,movePx[1]-i) in b.coordPc.values():
                                defense_pb.append(get_key_by_value(b.coordPc,(movePx[0]+i,movePx[1]-i)))
                            if (movePx[0]+i,movePx[1]-i) in b.coordPe.values():
                                defense_pb.append(get_key_by_value(b.coordPe,(movePx[0]+i,movePx[1]-i)))
                            break

                    for i in range(75,600,75):
                        if (movePx[0]-i,movePx[1]+i)  not in b.coordPc.values() and (movePx[0]-i,movePx[1]+i) not in b.coordPe.values():
                            avaible_move.append((movePx[0]-i,movePx[1]+i))
                            if (movePx[0]-i,movePx[1]+i) in w.coordPc.values() or (movePx[0]-i,movePx[1]+i) in w.coordPe.values():
                                break
                        else:
                            if (movePx[0]-i,movePx[1]+i) in b.coordPc.values():
                                defense_pb.append(get_key_by_value(b.coordPc,(movePx[0]-i,movePx[1]+i)))
                            if (movePx[0]-i,movePx[1]+i) in b.coordPe.values():
                                defense_pb.append(get_key_by_value(b.coordPe,(movePx[0]-i,movePx[1]+i)))
                            break
                    
                    for i in range(75,600,75):
                        if (movePx[0]+i,movePx[1]+i)  not in b.coordPc.values() and (movePx[0]+i,movePx[1]+i) not in b.coordPe.values():
                            avaible_move.append((movePx[0]+i,movePx[1]+i))
                            if (movePx[0]+i,movePx[1]+i) in w.coordPc.values() or (movePx[0]+i,movePx[1]+i) in w.coordPe.values():
                                break
                        else:
                            if (movePx[0]+i,movePx[1]+i) in b.coordPc.values():
                                defense_pb.append(get_key_by_value(b.coordPc,(movePx[0]+i,movePx[1]+i)))
                            if (movePx[0]+i,movePx[1]+i) in b.coordPe.values():
                                defense_pb.append(get_key_by_value(b.coordPe,(movePx[0]+i,movePx[1]+i)))
                            break

                        #
                    for i in range(75,600,75):
                        if (movePx[0],movePx[1]-i) not in b.coordPc.values() and (movePx[0],movePx[1]-i) not in b.coordPe.values():
                            avaible_move.append((movePx[0],movePx[1]-i))
                            if (movePx[0],movePx[1]-i) in w.coordPc.values() or (movePx[0],movePx[1]-i) in w.coordPe.values():
                                break
                        else:
                            if (movePx[0],movePx[1]-i) in b.coordPc.values():
                                defense_pb.append(get_key_by_value(b.coordPc,(movePx[0],movePx[1]-i)))
                            if (movePx[0],movePx[1]-i) in b.coordPe.values():
                                defense_pb.append(get_key_by_value(b.coordPe,(movePx[0],movePx[1]-i)))
                            break

                    for i in range(75,600,75):
                        if (movePx[0],movePx[1]+i)  not in b.coordPc.values() and (movePx[0],movePx[1]+i) not in b.coordPe.values():
                            avaible_move.append((movePx[0],movePx[1]+i))
                            if (movePx[0],movePx[1]+i) in w.coordPc.values() or (movePx[0],movePx[1]+i) in w.coordPe.values():
                                break
                        else:
                            if (movePx[0],movePx[1]+i) in b.coordPc.values():
                                defense_pb.append(get_key_by_value(b.coordPc,(movePx[0],movePx[1]+i)))
                            if (movePx[0],movePx[1]+i) in b.coordPe.values():
                                defense_pb.append(get_key_by_value(b.coordPe,(movePx[0],movePx[1]+i)))
                            break

                    for i in range(75,600,75):
                        if (movePx[0]-i,movePx[1])  not in b.coordPc.values() and (movePx[0]-i,movePx[1]) not in b.coordPe.values():
                            avaible_move.append((movePx[0]-i,movePx[1]))
                            if (movePx[0]-i,movePx[1]) in w.coordPc.values() or (movePx[0]-i,movePx[1]) in w.coordPe.values():
                                break
                        else:
                            if (movePx[0]-i,movePx[1]) in b.coordPc.values():
                                defense_pb.append(get_key_by_value(b.coordPc,(movePx[0]-i,movePx[1])))
                            if (movePx[0]-i,movePx[1]) in b.coordPe.values():
                                defense_pb.append(get_key_by_value(b.coordPe,(movePx[0]-i,movePx[1])))
                            break

                    for i in range(75,600,75):
                        if (movePx[0]+i,movePx[1])  not in b.coordPc.values() and (movePx[0]+i,movePx[1]) not in b.coordPe.values():
                            avaible_move.append((movePx[0]+i,movePx[1]))
                            if (movePx[0]+i,movePx[1]) in w.coordPc.values() or (movePx[0]+i,movePx[1]) in w.coordPe.values():
                                break
                        else:
                            if (movePx[0]+i,movePx[1]) in b.coordPc.values():
                                defense_pb.append(get_key_by_value(b.coordPc,(movePx[0]+i,movePx[1])))
                            if (movePx[0]+i,movePx[1]) in b.coordPe.values():
                                defense_pb.append(get_key_by_value(b.coordPe,(movePx[0]+i,movePx[1])))
                            break
        
        except:
            pass    

        if ho[0:2] == 'kw':
            #Diagonal
            #print((movePx[0]-75,movePx[1]-75) ,'------',avaible_move_dictB.values())
            
            if ((movePx[0]-75,movePx[1]-75) not in w.coordPc.values() and (movePx[0]-75,movePx[1]-75) not in w.coordPe.values()) and (movePx[0]-75, movePx[1]-75):
                avaible_move.append((movePx[0]-75,movePx[1]-75))
            else:
                if (movePx[0]-75,movePx[1]-75) in w.coordPc.values():
                    defense_pw.append(get_key_by_value(w.coordPc,(movePx[0]-75,movePx[1]-75)))
                if (movePx[0]-75,movePx[1]-75) in w.coordPe.values():
                    defense_pw.append(get_key_by_value(w.coordPe,(movePx[0]-75,movePx[1]-75)))

            if (movePx[0]+75,movePx[1]-75)  not in w.coordPc.values() and (movePx[0]+75,movePx[1]-75) not in w.coordPe.values() and (movePx[0]+75,movePx[1]-75) not in avaible_move_dictB.values():
                avaible_move.append((movePx[0]+75,movePx[1]-75))
            else:
                if (movePx[0]+75,movePx[1]-75) in w.coordPc.values():
                    defense_pw.append(get_key_by_value(w.coordPc,(movePx[0]+75,movePx[1]-75)))
                if (movePx[0]+75,movePx[1]-75) in w.coordPe.values():
                    defense_pw.append(get_key_by_value(w.coordPe,(movePx[0]+75,movePx[1]-75)))
                    
            if (movePx[0]-75,movePx[1]+75)  not in w.coordPc.values() and (movePx[0]-75,movePx[1]+75) not in w.coordPe.values() and (movePx[0]-75,movePx[1]+75) not in avaible_move_dictB.values():
                avaible_move.append((movePx[0]-75,movePx[1]+75))
            else:
                if (movePx[0]-75,movePx[1]+75) in w.coordPc.values():
                    defense_pw.append(get_key_by_value(w.coordPc,(movePx[0]-75,movePx[1]+75)))
                if (movePx[0]-75,movePx[1]+75) in w.coordPe.values():
                    defense_pw.append(get_key_by_value(w.coordPe,(movePx[0]-75,movePx[1]+75)))

            if (movePx[0]+75,movePx[1]+75)  not in w.coordPc.values() and (movePx[0]+75,movePx[1]+75) not in w.coordPe.values() and (movePx[0]+75,movePx[1]+75) not in avaible_move_dictB.values():
                avaible_move.append((movePx[0]+75,movePx[1]+75))
            else:
                if (movePx[0]+75,movePx[1]+75) in w.coordPc.values():
                    defense_pw.append(get_key_by_value(w.coordPc,(movePx[0]+75,movePx[1]+75)))
                if (movePx[0]+75,movePx[1]+75) in w.coordPe.values():
                    defense_pw.append(get_key_by_value(w.coordPe,(movePx[0]+75,movePx[1]+75)))

            ## Lados
            if (movePx[0],movePx[1]-75) not in w.coordPc.values() and (movePx[0],movePx[1]-75) not in w.coordPe.values():
                avaible_move.append((movePx[0],movePx[1]-75))
            else:
                if (movePx[0],movePx[1]-75) in w.coordPc.values():
                    defense_pw.append(get_key_by_value(w.coordPc,(movePx[0],movePx[1]-75)))
                if (movePx[0],movePx[1]-75) in w.coordPe.values():
                    defense_pw.append(get_key_by_value(w.coordPe,(movePx[0],movePx[1]-75)))

            if (movePx[0],movePx[1]+75)  not in w.coordPc.values() and (movePx[0],movePx[1]+75) not in w.coordPe.values():
                avaible_move.append((movePx[0],movePx[1]+75))
            else:
                if (movePx[0],movePx[1]+75) in w.coordPc.values():
                    defense_pw.append(get_key_by_value(w.coordPc,(movePx[0],movePx[1]+75)))
                if (movePx[0],movePx[1]+75) in w.coordPe.values():
                    defense_pw.append(get_key_by_value(w.coordPe,(movePx[0],movePx[1]+75)))

            if (movePx[0]-75,movePx[1])  not in w.coordPc.values() and (movePx[0]-75,movePx[1]) not in w.coordPe.values():
                avaible_move.append((movePx[0]-75,movePx[1]))
            else:
                if (movePx[0]-75,movePx[1]) in w.coordPc.values():
                    defense_pw.append(get_key_by_value(w.coordPc,(movePx[0]-75,movePx[1])))
                if (movePx[0]-75,movePx[1]) in w.coordPe.values():
                    defense_pw.append(get_key_by_value(w.coordPe,(movePx[0]-75,movePx[1])))

            if (movePx[0]+75,movePx[1])  not in w.coordPc.values() and (movePx[0]+75,movePx[1]) not in w.coordPe.values():
                avaible_move.append((movePx[0]+75,movePx[1]))
            else:
                if (movePx[0]+75,movePx[1]) in w.coordPc.values():
                    defense_pw.append(get_key_by_value(w.coordPc,(movePx[0]+75,movePx[1])))
                if (movePx[0]+75,movePx[1]) in w.coordPe.values():
                    defense_pw.append(get_key_by_value(w.coordPe,(movePx[0]+75,movePx[1])))
            #roque
            #print(check_w)
            if ((kw == 0 and tw0 == 0) and ((movePx[0]-225,movePx[1]) not in w.coordPc.values() and (movePx[0]-225,movePx[1]) not in w.coordPe.values()) and 
                ((movePx[0]-150,movePx[1]) not in w.coordPc.values() and (movePx[0]-150,movePx[1]) not in w.coordPe.values()) and 
                ((movePx[0]-75,movePx[1]) not in w.coordPc.values() and (movePx[0]-75,movePx[1]) not in w.coordPe.values()) ):

                avaible_move.append((movePx[0]-150,movePx[1]))
                avaible_move.append((movePx[0]-300,movePx[1]))

            if ((kw == 0 and tw1 == 0) and ((movePx[0]+150,movePx[1]) not in w.coordPc.values() and (movePx[0]+150,movePx[1]) not in w.coordPe.values()) and 
            ((movePx[0]+75,movePx[1]) not in w.coordPc.values() and (movePx[0]+75,movePx[1]) not in w.coordPe.values())): # and ((movePx[0]+150,movePx[1]) not in avaible_move_dictB.values() and (movePx[0]+150,movePx[1]) not in avaible_move_dictB.values()) and ((movePx[0]+75,movePx[1]) not in avaible_move_dictB.values() and (movePx[0]+75,movePx[1]) not in avaible_move_dictB.values())):
                avaible_move.append((movePx[0]+150,movePx[1]))
                avaible_move.append((movePx[0]+225,movePx[1]))
      
        elif ho[0:2] == 'kb':
            #Diagonal
            if (movePx[0]-75,movePx[1]-75) not in b.coordPc.values() and (movePx[0]-75,movePx[1]-75) not in b.coordPe.values():
                avaible_move.append((movePx[0]-75,movePx[1]-75))
            else:
                if (movePx[0]-75,movePx[1]-75) in b.coordPc.values():
                    defense_pb.append(get_key_by_value(b.coordPc,(movePx[0]-75,movePx[1]-75)))
                if (movePx[0]-75,movePx[1]-75) in b.coordPe.values():
                    defense_pb.append(get_key_by_value(b.coordPe,(movePx[0]-75,movePx[1]-75)))
            
            if (movePx[0]+75,movePx[1]-75)  not in b.coordPc.values() and (movePx[0]+75,movePx[1]-75) not in b.coordPe.values():
                avaible_move.append((movePx[0]+75,movePx[1]-75))
            else:
                if (movePx[0]+75,movePx[1]-75) in b.coordPc.values():
                    defense_pb.append(get_key_by_value(b.coordPc,(movePx[0]+75,movePx[1]-75)))
                if (movePx[0]+75,movePx[1]-75) in b.coordPe.values():
                    defense_pb.append(get_key_by_value(b.coordPe,(movePx[0]+75,movePx[1]-75)))
                    
            if (movePx[0]-75,movePx[1]+75)  not in b.coordPc.values() and (movePx[0]-75,movePx[1]+75) not in b.coordPe.values():
                avaible_move.append((movePx[0]-75,movePx[1]+75))
            else:
                if (movePx[0]-75,movePx[1]+75) in b.coordPc.values():
                    defense_pb.append(get_key_by_value(b.coordPc,(movePx[0]-75,movePx[1]+75)))
                if (movePx[0]-75,movePx[1]+75) in b.coordPe.values():
                    defense_pb.append(get_key_by_value(b.coordPe,(movePx[0]-75,movePx[1]+75)))

            if (movePx[0]+75,movePx[1]+75)  not in b.coordPc.values() and (movePx[0]+75,movePx[1]+75) not in b.coordPe.values():
                avaible_move.append((movePx[0]+75,movePx[1]+75))
            else:
                if (movePx[0]+75,movePx[1]+75) in b.coordPc.values():
                    defense_pb.append(get_key_by_value(b.coordPc,(movePx[0]+75,movePx[1]+75)))
                if (movePx[0]+75,movePx[1]+75) in b.coordPe.values():
                    defense_pb.append(get_key_by_value(b.coordPe,(movePx[0]+75,movePx[1]+75)))

            ## Lados
            if (movePx[0],movePx[1]-75) not in b.coordPc.values() and (movePx[0],movePx[1]-75) not in b.coordPe.values():
                avaible_move.append((movePx[0],movePx[1]-75))
            else:
                if (movePx[0],movePx[1]-75) in b.coordPc.values():
                    defense_pb.append(get_key_by_value(b.coordPc,(movePx[0],movePx[1]-75)))
                if (movePx[0],movePx[1]-75) in b.coordPe.values():
                    defense_pb.append(get_key_by_value(b.coordPe,(movePx[0],movePx[1]-75)))

            if (movePx[0],movePx[1]+75)  not in b.coordPc.values() and (movePx[0],movePx[1]+75) not in b.coordPe.values():
                avaible_move.append((movePx[0],movePx[1]+75))
            else:
                if (movePx[0],movePx[1]+75) in b.coordPc.values():
                    defense_pb.append(get_key_by_value(b.coordPc,(movePx[0],movePx[1]+75)))
                if (movePx[0],movePx[1]+75) in b.coordPe.values():
                    defense_pb.append(get_key_by_value(b.coordPe,(movePx[0],movePx[1]+75)))

            if (movePx[0]-75,movePx[1])  not in b.coordPc.values() and (movePx[0]-75,movePx[1]) not in b.coordPe.values():
                avaible_move.append((movePx[0]-75,movePx[1]))
            else:
                if (movePx[0]-75,movePx[1]) in b.coordPc.values():
                    defense_pb.append(get_key_by_value(b.coordPc,(movePx[0]-75,movePx[1])))
                if (movePx[0]-75,movePx[1]) in b.coordPe.values():
                    defense_pb.append(get_key_by_value(b.coordPe,(movePx[0]-75,movePx[1])))

            if (movePx[0]+75,movePx[1])  not in b.coordPc.values() and (movePx[0]+75,movePx[1]) not in b.coordPe.values():
                avaible_move.append((movePx[0]+75,movePx[1]))
            else:
                if (movePx[0]+75,movePx[1]) in b.coordPc.values():
                    defense_pb.append(get_key_by_value(b.coordPc,(movePx[0]+75,movePx[1])))
                if (movePx[0]+75,movePx[1]) in b.coordPe.values():
                    defense_pb.append(get_key_by_value(b.coordPe,(movePx[0]+75,movePx[1])))

            #roques
            if ((kb == 0 and tb0 == 0) and ((movePx[0]-225,movePx[1]) not in b.coordPc.values() and (movePx[0]-225,movePx[1]) not in b.coordPe.values()) and
                ((movePx[0]-150,movePx[1]) not in b.coordPc.values() and (movePx[0]-150,movePx[1]) not in b.coordPe.values()) and
                ((movePx[0]-75,movePx[1]) not in b.coordPc.values() and (movePx[0]-75,movePx[1]) not in b.coordPe.values())):

                avaible_move.append((movePx[0]-150,movePx[1]))
                avaible_move.append((movePx[0]-300,movePx[1]))

            if ((kb == 0 and tb1 == 0) and ((movePx[0]+150,movePx[1]) not in b.coordPc.values() and (movePx[0]+150,movePx[1]) not in b.coordPe.values()) and
            ((movePx[0]+75,movePx[1]) not in b.coordPc.values() and (movePx[0]+75,movePx[1]) not in b.coordPe.values())):
                avaible_move.append((movePx[0]+150,movePx[1]))
                avaible_move.append((movePx[0]+225,movePx[1]))

        #print(ho)
        avaible_move_n = []
        for item in avaible_move:
            if (item[1] < 600 and item[0] < 600) and (item[1] >=0 and item[0] >=0):
                avaible_move_n.append(item)
        peao = 0
        return avaible_move_n
    except:
        pass


def draw_check(avaible_move,screeni):
    move = []
    try:
        #print(avaible_move)
        #print(list(avaible_move[0],avaible_move[1]))
        
        if check_w != 1 and check_b != 1:
            for move in avaible_move:
                #print(move)
                #print(move)
                # Desenhe um círculo vermelho nas posições válidas
                pygame.draw.circle(screeni, (255, 0, 0), (move[0] + 37, move[1] + 37), 25)  # Ajuste as coordenadas e o raio conforme necessário
        else:
            #print(tuple(avaible_move))
            for x in tuple(avaible_move):
                #print(x)
                if type(x) == int:
                    move = (list(avaible_move)[0],list(avaible_move)[1])
                    #print(move)
                else:
                    move = x 
                pygame.draw.circle(screeni, (255, 0, 0), (move[0] + 37, move[1] + 37), 25)
    except:
        pass


def available_po(w,b,screeni,confs):
    #print(check_b)
    if check_w != 1:
        for i in range(0,len(list(w.coordPc.keys()))):
            avaible_move_dictW[list(w.coordPc.keys())[i]] = check_mov(list(w.coordPc.values())[i],list(w.coordPc.keys())[i],w,b,screeni)
        for i in range(0,len(list(w.coordPe.keys()))):
            avaible_move_dictW[list(w.coordPe.keys())[i]] = check_mov(list(w.coordPe.values())[i],list(w.coordPe.keys())[i],w,b,screeni)
        

    if check_b != 1:
        for i in range(0,len(list(b.coordPc.keys()))):
            avaible_move_dictB[list(b.coordPc.keys())[i]] = check_mov(list(b.coordPc.values())[i],list(b.coordPc.keys())[i],w,b,screeni)
        for i in range(0,len(list(b.coordPe.keys()))):
            avaible_move_dictB[list(b.coordPe.keys())[i]] = check_mov(list(b.coordPe.values())[i],list(b.coordPe.keys())[i],w,b,screeni)
    
    #Material insuficiente = empate
    if (len(avaible_move_dictW.keys()) == 1 and 'kw0' in avaible_move_dictW.keys() and len(avaible_move_dictB.keys()) == 1 and 'kb0' in avaible_move_dictB.keys()):
        confs.game = 3
    
    if (len(avaible_move_dictW.keys()) == 2 and 'kw0' in avaible_move_dictW.keys() and 'hw0' in avaible_move_dictW.keys() and len(avaible_move_dictB.keys()) == 1 and 'kb0' in avaible_move_dictB.keys()):
        confs.game = 3
    if (len(avaible_move_dictW.keys()) == 2 and 'kw0' in avaible_move_dictW.keys() and 'hw1' in avaible_move_dictW.keys() and len(avaible_move_dictB.keys()) == 1 and 'kb0' in avaible_move_dictB.keys()):
        confs.game = 3

    if (len(avaible_move_dictB.keys()) == 2 and 'kb0' in avaible_move_dictB.keys() and 'hb0' in avaible_move_dictB.keys() and len(avaible_move_dictW.keys()) == 1 and 'kw0' in avaible_move_dictW.keys()):
        confs.game = 3
    if (len(avaible_move_dictB.keys()) == 2 and 'kb0' in avaible_move_dictB.keys() and 'hb1' in avaible_move_dictB.keys() and len(avaible_move_dictW.keys()) == 1 and 'kw0' in avaible_move_dictW.keys()):
        confs.game = 3 

    if (len(avaible_move_dictW.keys()) == 2 and 'kw0' in avaible_move_dictW.keys() and 'bw0' in avaible_move_dictW.keys() and len(avaible_move_dictB.keys()) == 1 and 'kb0' in avaible_move_dictB.keys()):
        confs.game = 3
    if (len(avaible_move_dictW.keys()) == 2 and 'kw0' in avaible_move_dictW.keys() and 'bw1' in avaible_move_dictW.keys() and len(avaible_move_dictB.keys()) == 1 and 'kb0' in avaible_move_dictB.keys()):
        confs.game = 3

    if (len(avaible_move_dictB.keys()) == 2 and 'kb0' in avaible_move_dictB.keys() and 'bb0' in avaible_move_dictB.keys() and len(avaible_move_dictW.keys()) == 1 and 'kw0' in avaible_move_dictW.keys()):
        confs.game = 3
    if (len(avaible_move_dictB.keys()) == 2 and 'kb0' in avaible_move_dictB.keys() and 'bb1' in avaible_move_dictB.keys() and len(avaible_move_dictW.keys()) == 1 and 'kw0' in avaible_move_dictW.keys()):
        confs.game = 3 

    if (len(avaible_move_dictW.keys()) == 2 and 'kw0' in avaible_move_dictW.keys() and 'bw0' in avaible_move_dictW.keys() and len(avaible_move_dictB.keys()) == 2 and 'kb0' in avaible_move_dictB.keys()) and 'bb1' in avaible_move_dictB.keys():
        confs.game = 3
    if (len(avaible_move_dictW.keys()) == 2 and 'kw0' in avaible_move_dictW.keys() and 'bw1' in avaible_move_dictW.keys() and len(avaible_move_dictB.keys()) == 2 and 'kb0' in avaible_move_dictB.keys()) and 'bb0' in avaible_move_dictB.keys():
        confs.game = 3
    

new_coords = {}
upd = 1 
pec = []
pu = {}
ap = 0
tiW = 0
def checkW(w,b,screeni,confs):
    #print(list(w.coordPc.key())[0])
    global avaible_move_dictW
    global avaible_move_dictB

    global check_w, check_b
    global upd
    global pec
    global pu
    global defense_pb
    global ap
    global peca

    global tiW
    global ti
    upd = 1

    
    for x in range(0,8):
        try:
            if  w.coordPe.get('kw0') in avaible_move_dictB[list(b.coordPe.keys())[x]]:
                
                cbp = b.coordPe.get(list(b.coordPe.keys())[x])
                #print(avaible_move_dictB[list(b.coordPe.keys())[x]])
                bp = avaible_move_dictB[list(b.coordPe.keys())[x]]
                peca = (list(b.coordPe.keys())[x])
                
                check_w = 1
                #print('a')
                #print('a')
        except:
            pass
        
        try:
            if  w.coordPe.get('kw0') in avaible_move_dictB[list(b.coordPe.keys())[8+x]] and check_w != 1:
                
                cbp = b.coordPe.get(list(b.coordPe.keys())[8+x])
                #print(avaible_move_dictB[list(b.coordPe.keys())[x]])
                bp = avaible_move_dictB[list(b.coordPe.keys())[8+x]]
                peca = (list(b.coordPe.keys())[8+x])
                check_w = 1
        except:
            pass
        
        try:
            if w.coordPe.get('kw0') in avaible_move_dictB[list(b.coordPc.keys())[x]]:
                
                cbp = b.coordPc.get(list(b.coordPc.keys())[x])
                #print(avaible_move_dictB[list(b.coordPe.keys())[x]])
                bp = avaible_move_dictB[list(b.coordPc.keys())[x]]
                peca = (list(b.coordPc.keys())[x])

                check_w = 1
        except:
            pass
    
    
    
    reiw = []
    
    #pec = []
    #print(avaible_move_dictW)
    k = avaible_move_dictW.get('kw0')
    #k = check_mov(list(w.coordPe.get('kw0')),'kw0',w,b,screeni)
    pk = list(w.coordPe.get('kw0'))
    #print(k)
    pt = []
    no_can = []
    
    pec = []
    try:
        for x in range(14):
            for j in k:
                #print(avaible_move_dictB[list(b.coordPe.keys())[x]])
                if (j in avaible_move_dictB[list(b.coordPe.keys())[x]] or tuple(pk) in avaible_move_dictB[list(b.coordPe.keys())[x]]):#or j == b.coordPe.get([list(b.coordPe.keys())[x]]):
                    #print(list(b.coordPe.keys())[x])
                    pu[list(b.coordPe.keys())[x]] = (avaible_move_dictB[list(b.coordPe.keys())[x]])
                    if list(b.coordPe.keys())[x] not in pec:
                        pec.append(list(b.coordPe.keys())[x])
                              
    except:
        pass

    pecaa = []
    #print(avaible_move_dictB)
    try:
        if check_b != 1:
            for ll in range(8):
                #print((pk),'---',avaible_move_dictB.get(list(b.coordPe.keys())[ll]))         
                if tuple(pk) in avaible_move_dictB.get(list(b.coordPe.keys())[ll]):
                    #print(ll)
                    xy = list(b.coordPe.get(list(b.coordPe.keys())[ll]))
                    #print(xy)
                    #print(list(b.coordPe.keys())[x])
                    if xy[0] == pk[0] and xy[1] <pk[1]:
                        ap = (pk[0],pk[1]+75)
                    if xy[0] == pk[0] and xy[1] >pk[1]:
                        ap = (pk[0],pk[1]-75)

                    if xy[0] < pk[0] and xy[1] == pk[1]:
                        ap = (pk[0]+75,pk[1])
                    if xy[0] > pk[0] and xy[1] == pk[1]:
                        ap = (pk[0]-75,pk[1])
                    
                    if xy[0] < pk[0] and xy[1] < pk[1]:
                        ap = (pk[0]+75,pk[1]+75)
                        
                    if xy[0] > pk[0] and xy[1] < pk[1]:
                        ap = (pk[0]-75,pk[1]+75)
                        
                    if xy[0] < pk[0] and xy[1] > pk[1]:
                        ap = (pk[0]+75,pk[1]-75)
                        
                    if xy[0] > pk[0] and xy[1] > pk[1]:
                        ap = (pk[0]-75,pk[1]-75)

                    pecaa.append(ap)
    except:
        pass

    if pec != []:
        
        for atk_path in pec:
            #print(atk_path)
            if k != None:
                for item in k:
                    if item in pu.get(atk_path):
                        no_can.append(item)

            if ((375,525) in no_can or (450,525) in no_can or (525,525) in no_can  or check_w == 1) and kw==0:
                no_can.append((375,525))
                no_can.append((450,525))
                no_can.append((525,525))

            if ((225,525) in no_can or (150,525) in no_can or (75,525) in no_can or (0,525) in no_can or check_w == 1) and kw==0:
                no_can.append((225,525))
                no_can.append((150,525))
                no_can.append((75,525))
                no_can.append((0,525))
            
        
        #print(no_can)
        if k != None:
            pt = [item for item in k if item not in no_can]# and item != ap]

    ##
    try:              
        pe = {}
        for c in k:
            for pc in range(8):
                pq = b.coordPc.get(list(b.coordPc.keys())[pc])
                pe[list(b.coordPc.keys())[pc]] = ((pq[0]+75,pq[1]+75),(pq[0]-75,pq[1]+75))
    except:
        pass
    try:

        # Iterate over all of the possible moves and populate the `pp` list.
        pp = []
        #funciona
        for kk in k:
            for te in pe.keys():
                #print(list(pe.get(te))[0])
                if kk == list(pe.get(te))[0]:
                    #print(te,'--', pe.get(te))
                    #print(te)
                    pp.append(list(pe.get(te))[0])
                elif kk == list(pe.get(te))[1]:
                    #print(te)
                    pp.append(list(pe.get(te))[1])
        
        no_canc = pp
        no_mb = []
        
        for yy in defense_pb:
            #print(yy[0:1])
            if yy[0:1] == 'p':
                no_mb.append(b.coordPc.get(yy))
            else:
                #print(yy)
                no_mb.append(b.coordPe.get(yy))

        #print(no_canc)
        if (no_can !=[] or no_canc!=[] and ( no_can != None and no_canc  != None)) or no_mb != []:
            #print(no_can,'----',no_canc)
            # print(no_canc+no_can+ pecaa)
            j = no_can + no_canc + pecaa # + no_mb
            #print(j)
            jj = [item for item in k if item not in j and item not in no_mb]
            #print(jj)
            reiw = jj
            #print(reiw)
    except:
        pass

    #print(pe)
    testW = 0
    tiW = 0
    if len(avaible_move_dictB.keys()) == 7:
        for ch in pe.keys():
            if ch in avaible_move_dictB.keys() and testW != -1:
                testW =1
            else:
                testW = -1
        
        if testW == 1:
            for ts in pe.values():
                for ss in avaible_move_dictB.values():
                    if ts[0][0] == ss[0][0] and tiW !=-1:
                        tiW = 1
                    if ts[0][1] == ss[0][1] and tiW !=-1:
                        tiW = 1
                    else:
                        if get_key_by_value(avaible_move_dictB,ss) != 'kb0':
                            tiW = -1

            if  tiW == 1 and ti == 1:
                confs.game = 3
    
    p = []
    
    try:
        
        for x in range(0,16):
            #print(check_w,'----',upd)
            if check_w == 1 and upd ==1:
#                print(cbp)
                try :
                    if b.coordPe.get(peca)[0] !=  w.coordPe.get('kw0')[0]:
                        if peca[0:2] == 'bb' or peca[0:2] == 'qb':
                            if w.coordPe.get('kw0')[0] < cbp[0] and w.coordPe.get('kw0')[1] > cbp[1]:# x maior ,y menor
                                for i in bp:
                                    if (w.coordPe.get('kw0')[0] < i[0] and cbp[0] > i[0]) and (w.coordPe.get('kw0')[1] > i[1] and cbp[1] < i[1]):
                                        #print(b.coordPe.get(list(b.coordPe.keys())[x]),i,w.coordPe.get('kw0'))
                                        p.append(i)
                                        

                                avaible_move_dictW[list(b.coordPe.keys())[x]] = (cbp,p,w.coordPe.get('kw0'))
                                bp = avaible_move_dictW[list(b.coordPe.keys())[x]]
                                #print(bp)
                            #print(bp)
                            if w.coordPe.get('kw0')[0] > cbp[0] and w.coordPe.get('kw0')[1] > cbp[1]:# x menor ,y menor
                                for i in bp:
                                    #print(w.coordPe.get('kw0')[0] > i[0] and cbp[0] < i[0] and (w.coordPe.get('kw0')[1] > i[1] and i[1] < cbp[1]))
                                    if (w.coordPe.get('kw0')[0] > i[0] and cbp[0] < i[0]) and (w.coordPe.get('kw0')[1] > i[1] and  cbp[1] < i[1]):
                                        p.append(i)
                                        

                                avaible_move_dictW[list(b.coordPe.keys())[x]] = (cbp,p,w.coordPe.get('kw0'))
                                bp = avaible_move_dictW[list(b.coordPe.keys())[x]]
                            
                            if w.coordPe.get('kw0')[0] < cbp[0] and w.coordPe.get('kw0')[1] < cbp[1]:# x maior ,y maior
                                for i in bp:
                                    if (w.coordPe.get('kw0')[0] < i[0] and cbp[0] > i[0]) and (w.coordPe.get('kw0')[1] < i[1] and cbp[1] > i[1]):
                                        p.append(i)
                                        

                                avaible_move_dictW[list(b.coordPe.keys())[x]] = (cbp,p,w.coordPe.get('kw0'))
                                bp = avaible_move_dictW[list(b.coordPe.keys())[x]]

                            if w.coordPe.get('kw0')[0] > cbp[0] and w.coordPe.get('kw0')[1] < cbp[1]:# x menor ,y maior
                                for i in bp:
                                    if (w.coordPe.get('kw0')[0] > i[0] and cbp[0] < i[0]) and (w.coordPe.get('kw0')[1] < i[1] and cbp[1] > i[1]):
                                        p.append(i)
                                        

                                avaible_move_dictW[list(b.coordPe.keys())[x]] = (cbp,p,w.coordPe.get('kw0'))
                                bp = avaible_move_dictW[list(b.coordPe.keys())[x]]
                except:
                    pass
                
                try:
                    if (peca[0:2] == 'tb' or peca[0:2] == 'qb'):
                            #print(bp)
                            for i in bp:
                                if (w.coordPe.get('kw0')[1] == i[1]): # mesma linha
                                    #print(i)
                                    if (w.coordPe.get('kw0')[0] > i[0] and cbp[0] < i[0]): # x menor
                                        p.append(i)
                                    if (w.coordPe.get('kw0')[0] < i[0] and cbp[0] > i[0]): #x maior
                                        p.append(i)

                                if (w.coordPe.get('kw0')[0] == i[0]): # mesma linha
                                    if (w.coordPe.get('kw0')[1] > i[1] and cbp[1] < i[1]): # y menor
                                        #print(i)
                                        p.append(i)
                                    if (w.coordPe.get('kw0')[1] < i[1] and cbp[1] > i[1]): #y maior
                                        p.append(i)
                            #print(p)
                            avaible_move_dictW[list(b.coordPe.keys())[x]] = (cbp,p,w.coordPe.get('kw0'))
                            bp = avaible_move_dictW[list(b.coordPe.keys())[x]]
                        #print(bp)
                except:
                    pass
                
                if (peca[0:2] == 'hb'):
                    for i in bp:
                        if w.coordPe.get('kw0') == i:
                            p = i
                    
                    avaible_move_dictW[list(b.coordPe.keys())[x]] = (cbp,p,w.coordPe.get('kw0'))
                    bp = avaible_move_dictW[list(b.coordPe.keys())[x]]
                
                if (peca[0:2] == 'pb'):
                    
                    for i in bp:
                        if w.coordPe.get('kw0') == i:
                                p = i
                    
                    avaible_move_dictW[list(b.coordPc.keys())[x]] = (cbp,p,w.coordPe.get('kw0'))
                    bp = avaible_move_dictW[list(b.coordPc.keys())[x]]
                upd = 2
                
                hw1=avaible_move_dictW.get('hw1')
                hw0=avaible_move_dictW.get('hw0')
                bw1=avaible_move_dictW.get('bw1')
                bw0=avaible_move_dictW.get('bw0')
                tw1 = avaible_move_dictW.get('tw1')
                tw0 = avaible_move_dictW.get('tw0')
                qw0=avaible_move_dictW.get('qw0')
                try:
                    qw1=avaible_move_dictW.get('qw1')
                    qw2=avaible_move_dictW.get('qw2')
                    qw3=avaible_move_dictW.get('qw3')
                    qw4=avaible_move_dictW.get('qw4')
                except:
                    pass
                wp = {}
                bp = bp
                #print(bp)
            #Depois fazer  para a outra cor e pronto
                for ii in range(0,8):
                    #print(b.coordPe)
                    try:
                        wp[list(w.coordPc.keys())[ii]]=  check_mov(list(w.coordPc.values())[ii],list(w.coordPc.keys())[ii],w,b,screeni)
                        
                    except:
                        pass

                    #print(bpp,'----' , bp)
                    #print(bpp,'---',be
                    #print(wp)
                    #print(avaible_move_dictW)

                pc = {}
                h0 = []
                h1 = []
                b0 = []
                b1 = []
                t0 = []
                t1 = []
                q = []
                q1 = []
                q2= []
                q3 = []
                q4 = []
                #qxW ={}
                #qwx = {}
                #li = []
                global new_coords
                new_coords = {}
                #print(bp)
                #for xx in range(0,8):
                for oo in range(0,8):
                    try:
                        #ppara peôes
                        #print(wp)
                        for xx,yy in wp.items():
                            #print(xx, yy)
                            for peao in yy:
                                #print(peao,'---',bp)
                                if peao in bp[oo] or peao == bp[oo]:
                                    #print(peao)
                                    if peao not in pc:
                                        if xx in pc.keys():
                                            pc[xx] = [pc.get(xx),peao]
                                            #print(xx)
                                        else:
                                            pc[xx]=(peao)
                                            #print(xx)
                                        
                                        #x=xx
                                        #print(x)
                        if pc !={}:
                            #print(pc)
                            new_coords = pc 
                    except:
                        pass

                    try:

                        #torres
                        for ttw0 in tw0:
                            if ttw0 in bp[oo] or ttw0 == bp[oo]:
                                if ttw0 not in t0:
                                    t0.append(ttw0)
                        if t0 != []:
                            new_coords['tw0'] =t0
                    except:
                        pass
                    try:
                        for ttw1 in tw1:
                            if ttw1 in bp[oo] or ttw1 == bp[oo]:
                                if ttw1 not in t1:
                                    t1.append(ttw1)
                        if t1 != []:
                            new_coords['tw1'] =t1 
                        #para bispo
                    except:
                        pass
                    try:
                        for wbb0 in bw0:
                            if wbb0 in bp[oo] or wbb0 == bp[oo]:
                                if wbb0 not in b0:
                                    b0.append(wbb0)
                        if b0 != []:
                            new_coords['bw0'] = b0 
                    except:
                        pass
                    try:
                        for wbb1 in bw1:
                            if wbb1 in bp[oo] or wbb1 == bp[oo]:
                                if wbb1 not in b1:
                                    b1.append(wbb1)
                        if b1 != []:
                            new_coords['bw1'] = b1 
                        
                    except:
                        pass
                    try:  
                        #para rainha e cavalo
                        for qq in qw0:
                            if qq in bp[oo] or qq== bp[oo]:
                                if qq not in q:
                                    q.append(qq)
                        if q !=[]:
                            new_coords['qw0'] = q
                        #print(new_coords)
                    except:
                        pass
                    try:
                        """ for aaw in range(0,8):
                            qwx[list(w.coordPe.keys())[8+aaw]] = avaible_move_dictW.get(list(w.coordPe.keys())[8+aaw])
                            #qwxP = list(w.coordPe.keys())[8+aaw]
                            #li = []
                            for keyw in qwx.keys():
                                Lqwx = (qwx.get(keyw))
                                #li = []
                                for qxw in Lqwx:
                                    if qxw in bp[oo] or qxw == bp[oo]:
                                        if qxw not in qxW:
                                            if qxw not in li:
                                                li.append(qxw)
                                            #indi.append(qbxP)
                                        if  li not in qxW.values():
                                            qxW[keyw]=(li)
                                #print(indi,'--',qxB)
                                print(qxW)
                                try:
                                    for wkq in range(0,len(qxW.keys())):
                                        new_coords[list(qxW.keys())[wkq]] = qxW.get(list(qxW.keys())[wkq])
                                except:
                                    pass """
                        for qq1 in qw1:
                            if qq1 in bp[oo] or qq1== bp[oo]:
                                if qq1 not in q1:
                                    q1.append(qq1)
                        if q1 !=[]:
                            new_coords['qw1'] = q1

                    except:
                        pass
                    try:
                        for qq2 in qw2:
                            if qq2 in bp[oo] or qq2== bp[oo]:
                                if qq2 not in q2:
                                    q2.append(qq2)
                        if q2 !=[]:
                            new_coords['qw2'] = q2
                    except:
                        pass
                    try:
                        for qq3 in qw3:
                            if qq3 in bp[oo] or qq3== bp[oo]:
                                if qq3 not in q3:
                                    q3.append(qq3)
                        if q3 !=[]:
                            new_coords['qw3'] = q3
                    except:
                        pass
                    try:
                        for qq4 in qw4:
                            if qq4 in bp[oo] or qq4== bp[oo]:
                                if qq4 not in q4:
                                    q4.append(qq4)
                        if q4 !=[]:
                            new_coords['qw4'] = q4
                    except:
                        pass
                    try:
                        for hh0 in hw0:
                            #print(bp[oo])
                            if hh0 in bp[oo] or hh0 == bp[oo]:
                                #print(bp[oo])
                                if hh0 not in h0:
                                    h0.append(hh0)
                            #print(h)
                        if h0 != []:
                            new_coords['hw0'] = h0
                    except:
                        pass
                    try:
                        for hh1 in hw1:
                            if hh1 in bp[oo] or hh1 == bp[oo]:
                                if hh1 not in h1:
                                    h1.append(hh1)
                        if h1 != []:
                            new_coords['hw1'] = h1 
                    except:
                        pass
            
                #print(check)          
    except:
        pass
    
    if check_w == 1:
        avaible_move_dictW = new_coords
        #print(new_coords) 
        #print(avaible_move_dictB)
        if avaible_move_dictW == {} and reiw == []:
            #check_mate('Black',screeni,confs)      
            confs.game = 1
    #if reiw != []:
        #print(reiw)
    avaible_move_dictW['kw0'] = reiw          
    
    defense_pb = []              


new_coordsB = {}
ap =0
updB =1
pecB = []
puB = {}
ti =0
def checkB(w,b,screeni,confs):
    global avaible_move_dictW
    global avaible_move_dictB
    global check_w, check_b
    global updB
    global pecB, puB
    global defense_pw
    global ap
    global pecaB
    global ti, tiW
    global kb,tb0,tb1
    updB = 1

    
    for x in range(0,8):
        
        try:
            if  b.coordPe.get('kb0') in avaible_move_dictW[list(w.coordPe.keys())[x]]:
                
                cbpB = w.coordPe.get(list(w.coordPe.keys())[x])

                bpB = avaible_move_dictW[list(w.coordPe.keys())[x]]
                pecaB = (list(w.coordPe.keys())[x])
                check_b = 1
        except:
            pass
    
        try:

            if b.coordPe.get('kb0') in avaible_move_dictW[list(w.coordPe.keys())[8+x]] and check_b == 0:
                
                cbpB = w.coordPe.get(list(w.coordPe.keys())[8+x])

                bpB = avaible_move_dictW[list(w.coordPe.keys())[8+x]]
                pecaB = (list(w.coordPe.keys())[8+x])
                check_b = 1
        except:
            pass
    
        try:
            if b.coordPe.get('kb0') in avaible_move_dictW[list(w.coordPc.keys())[x]]:
                
                cbpB = w.coordPc.get(list(w.coordPc.keys())[x])

                bpB = avaible_move_dictW[list(w.coordPc.keys())[x]]
                pecaB = (list(w.coordPc.keys())[x])

                check_b = 1
        except:
            pass
    
    
    reiB = []

    kB = avaible_move_dictB.get('kb0')
    pkB = list(b.coordPe.get('kb0'))
    #print(kb)
    
    ptB = []
    no_canB = []
    pecB = []
    try:
        for x in range(0,14):
            for j in kB:
                
                if (j in avaible_move_dictW[list(w.coordPe.keys())[x]] or tuple(pkB) in avaible_move_dictW[list(w.coordPe.keys())[x]]):
                    #print(list(b.coordPe.keys())[x])
                    puB[list(w.coordPe.keys())[x]] = (avaible_move_dictW[list(w.coordPe.keys())[x]])
                    if list(w.coordPe.keys())[x] not in pecB:
                        pecB.append(list(w.coordPe.keys())[x])

                """ if (j in avaible_move_dictW[list(w.coordPe.keys())[8+x]] or tuple(pkB) in avaible_move_dictW[list(w.coordPe.keys())[8+x]]):
                    #print(list(b.coordPe.keys())[x])
                    puB[list(w.coordPe.keys())[8+x]] = (avaible_move_dictW[list(w.coordPe.keys())[8+x]])
                    if list(w.coordPe.keys())[8+x] not in pecB:
                        pecB.append(list(w.coordPe.keys())[x]) """
                    ###
    #####                                  
    except:
        pass
    pecaaB = []
    #print(check_b)
    try: #####
        if check_w != 1:
            for llb in range(8):
                        
                if tuple(pkB) in avaible_move_dictW.get(list(w.coordPe.keys())[llb]):
                    #print(ll)
                    xy = list(w.coordPe.get(list(w.coordPe.keys())[llb]))
                    #print(xy)
                    #print(list(b.coordPe.keys())[x])
                    if xy[0] == pkB[0] and xy[1] <pkB[1]:
                        ap = (pkB[0],pkB[1]+75)
                    if xy[0] == pkB[0] and xy[1] >pkB[1]:
                        ap = (pkB[0],pkB[1]-75)

                    if xy[0] < pkB[0] and xy[1] == pkB[1]:
                        ap = (pkB[0]+75,pkB[1])
                    if xy[0] > pkB[0] and xy[1] == pkB[1]:
                        ap = (pkB[0]-75,pkB[1])
                    
                    if xy[0] < pkB[0] and xy[1] < pkB[1]:
                        ap = (pkB[0]+75,pkB[1]+75)
                    if xy[0] > pkB[0] and xy[1] < pkB[1]:
                        ap = (pkB[0]-75,pkB[1]+75)
                        
                    if xy[0] < pkB[0] and xy[1] > pkB[1]:
                        ap = (pkB[0]+75,pkB[1]-75)
                    if xy[0] > pkB[0] and xy[1] > pkB[1]:
                        ap = (pkB[0]-75,pkB[1]-75)


                    pecaaB.append(ap)
    except:
        pass
    #print(tb1)
    if pecB != []:
        #print(pecB)
        for atk_path in pecB:
            #print(atk_path)
            if kB != None:
                for item in kB:
                    if item in puB.get(atk_path):
                        no_canB.append(item)
        
            if ((375,0) in no_canB or (450,0) in no_canB or (525,0) in no_canB  or check_b == 1) and kb==0:
                no_canB.append((375,0))
                no_canB.append((450,0))
                no_canB.append((525,0))
            
            if ((225,0) in no_canB or (150,0) in no_canB or (75,0) in no_canB or (0,0) in no_canB or check_b == 1) and kb==0:
                no_canB.append((225,0))
                no_canB.append((150,0))
                no_canB.append((75,0))
                no_canB.append((0,0))
   
    ##
    try:              
        peB = {}
        for c in kB:
            for pc in range(8):
                pqB = w.coordPc.get(list(w.coordPc.keys())[pc])
                peB[list(w.coordPc.keys())[pc]] = ((pqB[0]+75,pqB[1]-75),(pqB[0]-75,pqB[1]-75))
    except:
        pass
    try:
        
        # Iterate over all of the possible moves and populate the `pp` list.
        ppB = []
        #funciona
        #print('a')
       
        for kk in kB:
            for te in peB.keys():
                #print(list(pe.get(te))[0])
                if kk == list(peB.get(te))[0]:
                    #print(te,'--', pe.get(te))
                    #print(te)
                    ppB.append(list(peB.get(te))[0])
                elif kk == list(peB.get(te))[1]:
                    #print(te)
                    ppB.append(list(peB.get(te))[1])
        
        no_cancB = ppB
        no_mbB = []
        
        for yy in defense_pw:
            #print(yy[0:1])
            if yy[0:1] == 'p':
                no_mbB.append(w.coordPc.get(yy))
            else:
                #print(yy)
                no_mbB.append(w.coordPe.get(yy))
        
        if (no_canB !=[] or no_cancB !=[] and ( no_canB != None and no_cancB  != None)) or no_mbB != []:
            #print(no_can,'----',no_canc)
            #print(no_cancB,'--',no_canB,'--', pecaaB)
            j = no_canB + no_cancB + pecaaB # + no_mb
            #print(no_canB)
            jj = [item for item in kB if item not in j and item not in no_mbB]
            #print(jj)
            reiB = jj
            #print(reiw)
    except:
        pass
    
    #Empata de só tiver peao e o rei não conseguir passar,
    #print(peB)
    test = 0
    ti = 0
    
    if len(avaible_move_dictW.keys()) == 7:
        for ch in puB.keys():
            if ch in avaible_move_dictW.keys() and test != -1:
                test =1
            else:
                test = -1
        
        if test == 1:
            for ts in puB.values():
                for ss in avaible_move_dictW.values():
                    if ts[0][0] == ss[0][0] and ti !=-1:
                        ti = 1
                    if ts[0][1] == ss[0][1] and ti !=-1:
                        ti = 1
                    else:
                        if get_key_by_value(avaible_move_dictW,ss) != 'kw0':
                            ti = -1

            if  ti == 1 and tiW == 1:
                confs.game = 3


    pB = []
    try:

        for x in range(0,16):
            
            if check_b == 1 and updB ==1:
                try:
                    if w.coordPe.get(pecaB)[0] !=  b.coordPe.get('kb0')[0]:
                        pB = []
                        
                        if pecaB[0:2] == 'bw' or pecaB[0:2] == 'qw':
                            if b.coordPe.get('kb0')[0] < cbpB[0] and b.coordPe.get('kb0')[1] > cbpB[1]:# x maior ,y menor
                                for i in bpB:
                                    if (b.coordPe.get('kb0')[0] < i[0] and cbpB[0] > i[0]) and (b.coordPe.get('kb0')[1] > i[1] and cbpB[1] < i[1]):
                                        #print(b.coordPe.get(list(b.coordPe.keys())[x]),i,w.coordPe.get('kw0'))
                                        pB.append(i)

                                avaible_move_dictB[list(w.coordPe.keys())[x]] = (cbpB,pB,b.coordPe.get('kb0'))
                                bpB = avaible_move_dictB[list(w.coordPe.keys())[x]]
                                
                            if b.coordPe.get('kb0')[0] > cbpB[0] and b.coordPe.get('kb0')[1] > cbpB[1]:# x menor ,y menor
                                for i in bpB:
                                    
                                    if (b.coordPe.get('kb0')[0] > i[0] and cbpB[0] < i[0]) and (b.coordPe.get('kb0')[1] > i[1] and  cbpB[1] < i[1]):
                                        pB.append(i)

                                avaible_move_dictB[list(w.coordPe.keys())[x]] = (cbpB,pB,b.coordPe.get('kb0'))
                                bpB = avaible_move_dictB[list(w.coordPe.keys())[x]]
                            
                            if b.coordPe.get('kb0')[0] < cbpB[0] and b.coordPe.get('kb0')[1] < cbpB[1]:# x maior ,y maior
                                for i in bpB:
                                    if (b.coordPe.get('kb0')[0] < i[0] and cbpB[0] > i[0]) and (b.coordPe.get('kb0')[1] < i[1] and cbpB[1] > i[1]):
                                        pB.append(i)

                                avaible_move_dictB[list(w.coordPe.keys())[x]] = (cbpB,pB,b.coordPe.get('kb0'))
                                bpB = avaible_move_dictB[list(w.coordPe.keys())[x]]

                            if b.coordPe.get('kb0')[0] > cbpB[0] and b.coordPe.get('kb0')[1] < cbpB[1]:# x menor ,y maior
                                for i in bpB:
                                    if (b.coordPe.get('kb0')[0] > i[0] and cbpB[0] < i[0]) and (b.coordPe.get('kb0')[1] < i[1] and cbpB[1] > i[1]):
                                        pB.append(i)

                                avaible_move_dictB[list(w.coordPe.keys())[x]] = (cbpB,pB,b.coordPe.get('kb0'))
                                bpB = avaible_move_dictB[list(w.coordPe.keys())[x]]
                except:
                    pass
                 
                try:
                    if (pecaB[0:2] == 'tw' or pecaB[0:2] == 'qw'):
                        #print(cbpB)
                        for i in bpB:
                            if (b.coordPe.get('kb0')[1] == i[1]): # mesma linha
                                #print(i)
                                if (b.coordPe.get('kb0')[0] > i[0] and cbpB[0] < i[0]): # x menor
                                    pB.append(i)
                                if (b.coordPe.get('kb0')[0] < i[0] and cbpB[0] > i[0]): #x maior
                                    pB.append(i)

                            if (b.coordPe.get('kb0')[0] == i[0]): # mesma linha
                                if (b.coordPe.get('kb0')[1] > i[1] and cbpB[1] < i[1]): # y menor
                                    #print(i)
                                    pB.append(i)
                                if (b.coordPe.get('kb0')[1] < i[1] and cbpB[1] > i[1]): #y maior
                                    print(i)
                                    pB.append(i)
                                    
                            #print(pB)
                        
                        avaible_move_dictB[list(w.coordPe.keys())[x]] = (cbpB,pB,b.coordPe.get('kb0'))
                        bpB = avaible_move_dictB[list(w.coordPe.keys())[x]]
                        
                except:
                    pass
                
                if (pecaB[0:2] == 'hw'):
                    for i in bpB:
                        if b.coordPe.get('kb0') == i:
                            pB = i
                    
                    avaible_move_dictB[list(w.coordPe.keys())[x]] = (cbpB,pB,b.coordPe.get('kb0'))
                    bpB = avaible_move_dictB[list(w.coordPe.keys())[x]]
                
                if (pecaB[0:2] == 'pw'):
                    
                    for i in bpB:
                        if b.coordPe.get('kb0') == i:
                                pB = i
                    
                    avaible_move_dictB[list(w.coordPc.keys())[x]] = (cbpB,pB,b.coordPe.get('kb0'))
                    bpB = avaible_move_dictB[list(w.coordPc.keys())[x]]

                #print(bpB) 
                updB = 2#
                hb1=avaible_move_dictB.get('hb1')
                hb0=avaible_move_dictB.get('hb0')
                bb1=avaible_move_dictB.get('bb1')
                bb0=avaible_move_dictB.get('bb0')
                tb1 = avaible_move_dictB.get('tb1')
                tb0 = avaible_move_dictB.get('tb0')
                qb0=avaible_move_dictB.get('qb0')
                qb1=avaible_move_dictB.get('qb1')
                qb2=avaible_move_dictB.get('qb2')
                qb3=avaible_move_dictB.get('qb3')
                qb4=avaible_move_dictB.get('qb4')
                wpB = {}
                bpB=bpB
                #print(bpB)
            #Depois fazer  para a outra cor e pronto
                for ii in range(0,8):
                    #print(b.coordPe)
                    try:
                        wpB[list(b.coordPc.keys())[ii]]= check_mov(list(b.coordPc.values())[ii],list(b.coordPc.keys())[ii],w,b,screeni)
                        #print(wpB)
                    except:
                        pass

                    #print(bpp,'----' , bp)
                    #print(bpp,'---',be
                    
                    #print(avaible_move_dictW)

                pcB = {}
                h0B = []
                h1B = []
                b0B = []
                b1B = []
                t0B = []
                t1B = []
                qB = []
                qB1 = []
                qB2 = []
                qB3 = []
                qB4 = []
                qxB = {}
                qbx = {}
                global new_coordsB
                new_coordsB = {}
                #for xx in range(0,8):
                for oo in range(0,8):
                    try:
                        #ppara peôes
                        
                        for xx,yy in wpB.items():
                            #print(xx, yy)
                            for peaoB in yy:
                                if peaoB in bpB[oo] or peaoB == bpB[oo]:
                                    if peaoB not in pcB:
                                        if xx in pcB.keys():
                                            pcB[xx] = [pcB.get(xx),peaoB]
                                            #print(xx)
                                        else:
                                            pcB[xx]=(peaoB)
                                            #print(xx)
                                        
                                        #x=xx
                                        #print(x)
                           # print(pcB)
                            if pcB !={}:
                                new_coordsB = pcB 
                    except:
                        pass
                    try:
                        #torres
                        for ttw0 in tb0:
                            if ttw0 in bpB[oo] or ttw0 == bpB[oo]:
                                if ttw0 not in t0B:
                                    t0B.append(ttw0)
                        if t0B != []:
                            new_coordsB['tb0'] =t0B
                    except:
                        pass
                    try:
                        for ttw1 in tb1:
                            if ttw1 in bpB[oo] or ttw1 == bpB[oo]:
                                if ttw1 not in t1B:
                                    t1B.append(ttw1)
                        if t1B != []:
                            new_coordsB['tb1'] =t1B
                    except:
                        pass
                    try:
                        #para bispo
                        for wbb0 in bb0:
                            if wbb0 in bpB[oo] or wbb0 == bpB[oo]:
                                if wbb0 not in b0B:
                                    b0B.append(wbb0)
                        if b0B != []:
                            new_coordsB['bb0'] = b0B 
                    except:
                        pass
                    try:
                        for wbb1 in bb1:
                            if wbb1 in bpB[oo] or wbb1 == bpB[oo]:
                                if wbb1 not in b1B:
                                    b1B.append(wbb1)
                        if b1B != []:
                            new_coordsB['bb1'] = b1B 
                    except:
                        pass
                    try:
                            
                        #para rainha e cavalo
                        for qq1 in qb1:
                            if qq1 in bpB[oo] or qq1== bpB[oo]:
                                if qq1 not in qB1:
                                    qB1.append(qq1)
                        if qB1 !=[]:
                            new_coordsB['qb1'] = qB1
                        #print(new_coords)
                    except:
                        pass
                    try:
                            
                        #para rainha e cavalo
                        for qq2 in qb2:
                            if qq2 in bpB[oo] or qq2== bpB[oo]:
                                if qq2 not in qB2:
                                    qB2.append(qq2)
                        if qB2 !=[]:
                            new_coordsB['qb2'] = qB2
                        #print(new_coords)
                    except:
                        pass
                    try:
                            
                        #para rainha e cavalo
                        for qq3 in qb3:
                            if qq3 in bpB[oo] or qq3== bpB[oo]:
                                if qq3 not in qB3:
                                    qB3.append(qq3)
                        if qB3 !=[]:
                            new_coordsB['qb3'] = qB3
                        #print(new_coords)
                    except:
                        pass
                    try:
                            
                        #para rainha e cavalo
                        for qq4 in qb4:
                            if qq4 in bpB[oo] or qq4== bpB[oo]:
                                if qq4 not in qB4:
                                    qB4.append(qq4)
                        if qB4 !=[]:
                            new_coordsB['qb4'] = qB4
                        #print(new_coords)
                    except:
                        pass
                    try:
                        """ for aa in range(0,8):
                            qbx[list(b.coordPe.keys())[8+aa]] = avaible_move_dictB.get(list(b.coordPe.keys())[8+aa])
                            #qbxP = list(b.coordPe.keys())[8+aa]
                        
                            
                            #print(Lqbx)
                            for key in qbx.keys():
                                Lqbx =  (qbx.get(key))
                                for qx in Lqbx:
                                    #print(qx)
                                    if qx in bpB[oo] or qx == bpB[oo]:
                                        if qx not in qxB:
                                            #print(qx)
                                            #li.append()
                                            
                                            #indi.append(qbxP)
                                            #
                                            #print(indi,'--',qxB)
                                        #print(qxB)
                                            qxB[key] = (qx)
                                        try:
                                            for kq in range(0,len(qxB.keys())):
                                                #print(list(qxB.keys())[kq])
                                                new_coordsB[list(qxB.keys())[kq]] = qxB.get(list(qxB.keys())[kq])
                                            new_coordsB['qb2'] = qxB 
                                            new_coordsB['qb3'] = qxB 
                                        except:
                                            pass """
                        for qq in qb0:
                            if qq in bpB[oo] or qq== bpB[oo]:
                                if qq not in qB:
                                    qB.append(qq)
                        if qB !=[]:
                            new_coordsB['qb0'] = qB
                    except:
                        pass
                    try:
                        for hh0 in hb0:
                            #print(bp[oo])
                            if hh0 in bpB[oo] or hh0 == bpB[oo]:
                                #print(bp[oo])
                                if hh0 not in h0B:
                                    h0B.append(hh0)
                            #print(h)
                        if h0B != []:
                            new_coordsB['hb0'] = h0B
                    except:
                        pass
                    try:
                        for hh1 in hb1:
                            if hh1 in bpB[oo] or hh1 == bpB[oo]:
                                if hh1 not in h1B:
                                    h1B.append(hh1)
                        if h1B != []:
                            new_coordsB['hb1'] = h1B

                        
                                        
                        """ if qxB != []:
                            
                            for i in range(0,8): """
                                
                    except:
                        pass
            
                #print(check)          
    except:
        pass
    if check_b == 1:
        #print(new_coordsB) 
        avaible_move_dictB = new_coordsB
        
        #print(avaible_move_dictB)
        if avaible_move_dictB == {} and reiB == []:
            #check_mate('white',screeni,confs)      
            confs.game = 2
    #if reiB != []:
        #print(reiw)
    
    avaible_move_dictB['kb0'] = reiB    
    
                       
    defense_pw = []
    # Se o jogo esta afogado
    if avaible_move_dictB == {}:
        confs.game = 3

    #Se teve tripla repetição
   
    #print(pecaB)
    
        
def check_mate(cp,screeni,confs):
    if cp == 1:
       cp = 'Black Peaces Won'
    if cp == 2:
       cp = 'White Peaces Won'
    if cp == 3:
        cp = 'The Game Tie!'
    
    cp =  cp
    colorR = (50, 55, 0)
    ret = pygame.Rect(0,225,600,150)
    retD = pygame.draw.rect(screeni,colorR, ret)
    textW = confs.font.render(str(cp),True,confs.color)
    textP = (210,290)
    screeni.blit(textW,textP)
    
    textS = confs.font.render(str('Press Space for play other match'),True,confs.color)
    textPs = (140,310)
    screeni.blit(textS,textPs)

    

    for eventT in pygame.event.get(): #espera um evento
        if eventT.type == pygame.QUIT:# para fechar a janela
            pygame.quit()
            sys.exit()
        
        if eventT.type == pygame.KEYDOWN:
            if eventT.key == pygame.K_SPACE:
                global capeaceCb
                capeaceCb = {}
                global capeaceEb
                capeaceEb = {}
                ###
                global capeaceCw
                capeaceCw = {}
                global capeaceEw
                capeaceEw = {}
                global check_b,check_w
                check_w =0
                check_b = 0
                global rep,repW
                rep,repW = 0,0
                
                return 1
    
