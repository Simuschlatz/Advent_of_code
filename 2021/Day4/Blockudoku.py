import pygame
import time
from random import randint
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (62, 108, 216)
GHOST = (128, 255, 255)
RED = (255, 0, 0)

block_selected = False

score = 0

clock = pygame.time.Clock()

board = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
]

blocks = [
    [
        [1,1,1],
        [0,0,1],
        [0,0,1]
    ],
    [
        [0,0,1],
        [0,0,1],
        [1,1,1]
    ],
    [
        [1,0,0],
        [1,0,0],
        [1,1,1]
    ],
    [
        [1,1,1],
        [1,0,0],
        [1,0,0]
    ],
    [
        [0,1,0],
        [1,1,1],
        [0,1,0]
    ],
    [
        [0,1,0],
        [1,1,1],
        [0,1,0]
    ],
    [
        [1,1,1]
    ],
    [
        [1],
        [1],
        [1]
    ],
    [
        [0,0,1],
        [1,1,1]
    ],
    [
        [1,0],
        [1,0],
        [1,1]
    ],
    [
        [1,1,1],
        [1,0,0]
    ],
    [
        [1,1],
        [0,1],
        [0,1]
    ],
    [
        [1,1,1],
        [0,1,0],
        [0,1,0]
    ],
    [
        [0,0,1],
        [1,1,1],
        [0,0,1]
    ],
    [
        [0,1,0],
        [0,1,0],
        [1,1,1]
    ],
    [
        [1,0,0],
        [1,1,1],
        [1,0,0]
    ],
    [
        [0,1,0],
        [1,1,1]
    ],
    [
        [1,1,0],
        [0,1,1]
    ],
    [
        [1]
    ],
    [
        [1,1],
        [1,1]
    ],
    [
        [1,1],
        [1,1]
    ],
    [
        [1,1]
    ],
    [
        [1],
        [1]
    ],
    [
        [1,0],
        [0,1]
    ],
    [
        [0,1],
        [1,0]
    ]
]

height = 650
width = 500
gap = width // 11

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Patrickudoku")

class Block():
    def __init__(self, place, num):
        self.place = place
        self.num = num
        self.x = self.place * gap * 4
        self.y = height - gap * 4
        self.change_form = False
        self.clicked = False
        self.show = True

    def draw(self):
        if self.show == False:
            return None
        for row in range(len(blocks[self.num])):
            for col in range(len(blocks[self.num][row])):
                if blocks[self.num][row][col] == 1:
                    pygame.draw.rect(win, BLUE, ((self.x + col * gap, self.y + row * gap), (gap, gap)))


    def check_clicked(self):
        if pygame.mouse.get_pressed()[0]:
            if pygame.mouse.get_pos()[0] >= self.x and pygame.mouse.get_pos()[0] <= self.x + gap * 3:
                if pygame.mouse.get_pos()[1] >= self.y and pygame.mouse.get_pos()[1] <= self.y + gap * 3:
                    self.clicked = True

    def move(self):
        if self.clicked == True:
            self.x = pygame.mouse.get_pos()[0]
            self.y = pygame.mouse.get_pos()[1]
        else:
            self.x = self.place * gap * 4
            self.y = height - gap * 4
            if self.change_form == True:
                self.num = randint(0, int(len(blocks)) - 1)
                self.change_form = False

    def drop(self, boardd):
        score_count = 0
        if pygame.mouse.get_pressed()[2] and self.clicked == True:
            
            place_row = self.y // gap - 1
            place_col = self.x // gap - 1

            if check_space_free(self.num, place_row, place_col):
                for row in range(len(blocks[self.num])):
                    for col in range(len(blocks[self.num][row])):
                        if blocks[self.num][row][col] == 1:
                            score_count += 1
                            board[place_row + row][place_col + col] = 1
                        
                self.clicked = False
                self.change_form = True
        return score_count


def draw_board():
    win.fill((WHITE))
    gap = width // 11
    for row in range(9):
        for col in range(9):
            if board[row][col] == 1:
                pygame.draw.rect(win, BLUE, ((col * gap + gap, row * gap + gap), (gap, gap)))

    for row in range(10):
        pygame.draw.line(win, BLACK, (gap, row * gap + gap), (width - gap - 5, row * gap + gap))
    for col in range(10):
        pygame.draw.line(win, BLACK, (col * gap + gap, gap), (col * gap + gap, width - gap - 5))


def check_space_free(num, row_place, col_place):
    for row in range(len(blocks[num])):
        for col in range(len(blocks[num][row])):
            if blocks[num][row][col] == 1:
                if board[row_place + row][col_place + col] == 1:
                    return False
    return True


def clear_board(boardd):
    score_count = 0
    
    # horizontal
    for row in range(9):
        if boardd[row] == [1,1,1,1,1,1,1,1,1]:
            boardd[row] = [0,0,0,0,0,0,0,0,0]
            score_count += 18

    # vertical
    ver_count = 0
    for col in range(9):
        for row in range(9):
            if boardd[row][col] == 1:
                ver_count += 1
        if ver_count == 9:
            score_count += 18
            for row2 in range(9):
                boardd[row2][col] = 0
        ver_count = 0
        
    # boxes
    for box_ver in range(3):
        for box_hor in range(3):
            box_count = 0
            for row in range(3):
                for col in range(3):
                    if boardd[box_ver * 3 + row][box_hor * 3 + col] == 1:
                        box_count += 1
            if box_count == 9:
                #clear box
                for row in range(3):
                    for col in range(3):
                        boardd[box_ver * 3 + row][box_hor * 3 + col] = 0
                score_count += 18

    return score_count
    



block1 = Block(0, randint(0, int(len(blocks))) - 1)
block2 = Block(1, randint(0, int(len(blocks))) - 1)
block3 = Block(2, randint(0, int(len(blocks))) - 1)
bblocks = [block1, block2, block3]

close = False
# MAINLOOP
run = True
while run:
    clock.tick(50)
    pygame.display.set_caption("Punkte: " + str(score))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close = True
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        run = False

    draw_board()
    for block in bblocks:
        block.move()
        block.draw()
        block.check_clicked()
        score += block.drop(board)
        score += clear_board(board)
    pygame.display.update()

if close == True:
    pygame.quit()
else:
    #win.blit()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

# print("Deine Punkte: " + str(score))
# highscore = open("highscore.txt", "r")
# for line in highscore:
#     print("Dein Highscore: " + line)
#     hisc = int(line)
# highscore.close()

# if score > hisc:
#     print("Neuer Highscore!")
#     highscore = open("highscore.txt", "w")
#     highscore.write(str(score))
#     highscore.close()

time.sleep(3)
pygame.quit()
