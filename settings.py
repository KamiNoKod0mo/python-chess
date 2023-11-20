import pygame
from abc import ABC, abstractclassmethod


class Confs():
    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 700
        self.color = (230, 230, 230)

        self.screeni_width = 600
        self.screeni_height = 600
        self.colori = (0,0,0)

        self.bg = pygame.image.load("/home/carlos_/Desktop/Projects/Python/Games/xadrez/imagens/bg2.png")
        self.bg = pygame.transform.scale(self.bg, (self.screen_width,self.screen_height))

        self.button = pygame.image.load("/home/carlos_/Desktop/Projects/Python/Games/xadrez/imagens/playbutton.jpeg")
        self.button = pygame.transform.scale(self.button, (self.screen_width-700,self.screen_height-500))

        self.font = pygame.font.Font("freesansbold.ttf",20)
        self.colorT = (255,255,255)

        self.creation = 0
        self.creaT = 0

        self.t = 1

        self.game = 0


class  Parts(ABC):
    @abstractclassmethod
    def __init__(self):
        self.widht = 70
        self.height = 70
        id = 'x'
    @abstractclassmethod
    def horse(self):
        horse =  []
        for i in range(0,2):
            ho = pygame.image.load("x")
            #print(ho)
            ho = pygame.transform.scale(ho,(self.widht,self.height))
            horse.append(ho)
        return horse
    @abstractclassmethod
    def pawn(self):
        pawn = []
        for i in range(0,8):
            pw = pygame.image.load("x")
            pw = pygame.transform.scale(pw,(self.widht,self.height))
            pawn.append(pw)
        #print(pawn)
        return pawn
    @abstractclassmethod
    def bishop(self):
        bishop = []
        for i in range(0,2):
            bp = pygame.image.load("x")
            bp = pygame.transform.scale(bp,(self.widht,self.height))
            bishop.append(bp)
        return bishop
    @abstractclassmethod
    def queen(self):
        qn = pygame.image.load("x")
        qn = pygame.transform.scale(qn,(self.widht,self.height))
        return qn
    @abstractclassmethod
    def king(self):
        kg = pygame.image.load("x")
        kg = pygame.transform.scale(kg,(self.widht,self.height))
        return kg
    @abstractclassmethod
    def tower(self):
        tower = []
        for i in range(0,2):
            tw = pygame.image.load("x")
            tw = pygame.transform.scale(tw,(self.widht,self.height))
            tower.append(tw)
        return tower


class PartsW(Parts):
    def __init__(self):
        self.widht = 70
        self.height = 70
        id = 'w'
    def horse(self):
        horse =  []
        for i in range(0,2):
            ho = pygame.image.load("/home/carlos_/Desktop/Projects/Python/Games/xadrez/imagens/horseW.png")
            #print(ho)
            ho = pygame.transform.scale(ho,(self.widht,self.height))
            horse.append(ho)
        return horse
    def pawn(self):
        pawn = []
        for i in range(0,8):
            pw = pygame.image.load("/home/carlos_/Desktop/Projects/Python/Games/xadrez/imagens/pawnW.png")
            pw = pygame.transform.scale(pw,(self.widht,self.height))
            pawn.append(pw)
        #print(pawn)
        return pawn
    def bishop(self):
        bishop = []
        for i in range(0,2):
            bp = pygame.image.load("/home/carlos_/Desktop/Projects/Python/Games/xadrez/imagens/bishopW.png")
            bp = pygame.transform.scale(bp,(self.widht,self.height))
            bishop.append(bp)
        return bishop
    def queen(self):
        qn = pygame.image.load("/home/carlos_/Desktop/Projects/Python/Games/xadrez/imagens/queenW.png")
        qn = pygame.transform.scale(qn,(self.widht,self.height))
        return qn
    def king(self):
        kg = pygame.image.load("/home/carlos_/Desktop/Projects/Python/Games/xadrez/imagens/kingW.png")
        kg = pygame.transform.scale(kg,(self.widht,self.height))
        return kg
    def tower(self):
        tower = []
        for i in range(0,2):
            tw = pygame.image.load("/home/carlos_/Desktop/Projects/Python/Games/xadrez/imagens/towerW.png")
            tw = pygame.transform.scale(tw,(self.widht,self.height))
            tower.append(tw)
        return tower


class PartsB(Parts):
    def __init__(self):
        self.widht = 70
        self.height = 70
        id = 'b'
    def horse(self):
        horse =  []
        for i in range(0,2):
            ho = pygame.image.load("/home/carlos_/Desktop/Projects/Python/Games/xadrez/imagens/horseB.png")
            #print(ho)
            ho = pygame.transform.scale(ho,(self.widht,self.height))
            horse.append(ho)
        return horse
    def pawn(self):
        pawn = []
        for i in range(0,8):
            pw = pygame.image.load("/home/carlos_/Desktop/Projects/Python/Games/xadrez/imagens/pawnB.png")
            pw = pygame.transform.scale(pw,(self.widht,self.height))
            pawn.append(pw)
        #print(pawn)
        return pawn
    def bishop(self):
        bishop = []
        for i in range(0,2):
            bp = pygame.image.load("/home/carlos_/Desktop/Projects/Python/Games/xadrez/imagens/bishopB.png")
            bp = pygame.transform.scale(bp,(self.widht,self.height))
            bishop.append(bp)
        return bishop
    def queen(self):
        qn = pygame.image.load("/home/carlos_/Desktop/Projects/Python/Games/xadrez/imagens/queenB.png")
        qn = pygame.transform.scale(qn,(self.widht,self.height))
        return qn
    def king(self):
        kg = pygame.image.load("/home/carlos_/Desktop/Projects/Python/Games/xadrez/imagens/kingB.png")
        kg = pygame.transform.scale(kg,(self.widht,self.height))
        return kg
    def tower(self):
        tower = []
        for i in range(0,2):
            tw = pygame.image.load("/home/carlos_/Desktop/Projects/Python/Games/xadrez/imagens/towerB.png")
            tw = pygame.transform.scale(tw,(self.widht,self.height))
            tower.append(tw)
        return tower


