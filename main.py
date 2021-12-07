import pygame
from random import shuffle

SCREEN_SIZE = (1200, 700)
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)

wait_unit_pause = 500
wait_unit_show = 250
pygame.init()


def init_display():
    global screen,  background,  matryca
    matryca = matrix()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    background = pygame.Surface(screen.get_size())
    clear()


class matrix:

    def __init__(self):
        self.matrix_num = [[j+i*6+65 for j in range(6)] for i in range(5)]
        self.matrix_bin = [[binarny(x) for x in rows] for rows in self.matrix_num]
        self.matrix_chr = [[chr(x) for x in rows] for rows in self.matrix_num]
        self.matrix_chr[4][2:] = ['?', '!', '.', 'spc']
        self.matrix_map = [[[int(x[map_count]) for x in rows] for rows in self.matrix_bin] for map_count in range(5)]

    ######### _all returns  2d (or 3d in map) matrix

    def numeric_all(self):
        return self.matrix_num
    
    def binary_all(self):
        return self.matrix_bin
    
    def character_all(self):
        return self.matrix_chr
    
    def map_all(self):
        return self.matrix_map

    ######## _one_list returns 1d list

    def numeric_one_list(self):
        temp = []
        for element in self.numeric_all():
            temp.extend(element)
        return temp

    def binary_one_list(self):
        temp = []
        for element in self.binary_all():
            temp.extend(element)
        return temp

    def character_one_list(self):
        temp = []
        for element in self.character_all():
            temp.extend(element)
        return temp

    def let_chaos_reign(self):
        ### shuffles only binary matrix
        temp = self.binary_one_list()
        shuffle(temp)
        end = []
        for x in range(5):
            end.append(temp[x*6:x*6+6])
        self.matrix_bin = end
        self.matrix_map = [[[int(x[map_count]) for x in rows] for rows in self.matrix_bin] for map_count in range(5)]

    def return_to_monke(self):
        self.matrix_bin = [[binarny(x) for x in rows] for rows in self.matrix_num]
        self.matrix_map = [[[int(x[map_count]) for x in rows] for rows in self.matrix_bin] for map_count in range(5)]


def binarny(liczba):
    return bin(liczba)[4:]


def clear():
    global background, screen
    background.fill(BLACK)
    screen.blit(background, (0, 0))
    font = pygame.font.SysFont("Times",  50)
    for row,  line in enumerate(matryca.character_all()):
        for column,  element in enumerate(line):
            text1 = font.render(element,  True,  WHITE)
            screen.blit(text1,  (column * 200 + 75,  row * 140 + 45))


def bordering(c, d, a, b):
    pygame.draw.line(screen, WHITE, (a, c), (a, d), 3)
    pygame.draw.line(screen, WHITE, (a, c), (b, c), 3)
    pygame.draw.line(screen, WHITE, (b, c), (b, d), 3)
    pygame.draw.line(screen, WHITE, (b, d), (a, d), 3)


def webbing(nr):
    global screen
    for row,  line in enumerate(matryca.map_all()[nr]):
        for column,  element in enumerate(line):
            if element == 1:
                bordering(row*140+10, row*140+130, column*200+10, column*200+190)


def deciphering(signal, kod):
    #####################
    # Syganł powinien być podany jako albo ciąg znaków albo lista pojedynczych znaków
    #####################
    letter = ""
    if isinstance(signal, list):
        for element in signal:
            letter += str(element)
    else:
        letter = str(signal)

    return matryca.character_one_list()[kod.index(letter)]


def go():
    nr = 5
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        if nr > 4:
            nr = 0
            bordering(30, SCREEN_SIZE[1]-30, 30, SCREEN_SIZE[0]-30)
            pygame.display.update()
            pygame.time.wait(wait_unit_pause)
            clear()
            pygame.display.update()
            pygame.time.wait(2*wait_unit_pause)
            bordering(30, SCREEN_SIZE[1]-30, 30, SCREEN_SIZE[0]-30)
            pygame.display.update()
            pygame.time.wait(wait_unit_pause)
            clear()
            pygame.display.update()
            pygame.time.wait(wait_unit_pause)
        else:
            webbing(nr)
            pygame.display.update()
            pygame.time.wait(3*wait_unit_show)
            clear()
            pygame.display.update()
            pygame.time.wait(wait_unit_show)
            nr += 1

def print_lol():
    print("lol")


init_display()
go()

pygame.quit()
