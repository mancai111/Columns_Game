import pygame
from Game import Game
import random
#Version Updated (Pygame Implemented)
char = ['A','B','C','D','E','F','G']
def randomGenerateFaller(matrix):
    faller = {}
    str = []
    str.append("")
    rand =random.randint(0,5)
    str.append(rand)
    rand =random.randint(0,5)
    str.append(char[rand])
    rand =random.randint(0,5)
    str.append(char[rand])
    rand =random.randint(0,5)
    str.append(char[rand])

    faller['start'] = -2
    faller['is_land'] = 0
    faller['column'] =int(str[1])
    if matrix[0][faller['column']] != 0:
        print("GAME OVER")
        exit(0)
    if matrix[1][faller['column']] != 0:
        faller['is_land'] =1
    faller['content'] = []
    faller['is_delete'] = 0
    faller['content'].append(str[2])
    faller['content'].append(str[3])
    faller['content'].append(str[4])
    return faller

def run() ->None:
    pygame.init()
    surface = pygame.display.set_mode((700,600))
    clock = pygame.time.Clock()
    rows = 13
    columns = 6
    rows =int(rows)
    columns =int(columns)
    faller = None
    matrix = [[0 for j in range(columns)] for i in range(rows) ]
    game = Game(matrix)

    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = 0
    game.is_freeze = True
    game.freeze(matrix,faller)
    game.printMatrix(matrix,faller,surface)
    running =True
    while running:
        clock.tick(10)
        flag =False
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.VIDEORESIZE:
                Game.resize_surface((700,700),event.size)
               
            if event.type == pygame.KEYDOWN:
                key = event.key
                print(key)
                if key == 276:
                    game.moveLeft(matrix,faller)
                elif key == 275:
                    game.moveRight(matrix,faller)
                elif key == 113:
                    exit(0)
                elif key == 32:
                    if faller is not None:
                        faller['content'].insert(0,faller['content'].pop())

        flag =game.nexttick(matrix,faller)

        if game.is_freeze == False and faller is not None and faller['is_delete'] == 1:
            faller = None

        pygame.display.flip()
        print("paint")
        game.printMatrix(matrix,faller,surface)
        if flag:
            print("GAME OVER")
            exit(0)
        if faller is None:
            faller = randomGenerateFaller(matrix)
    pygame.quit()

if __name__ == '__main__':
    run()
