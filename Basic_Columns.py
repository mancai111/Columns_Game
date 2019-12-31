from Game import Game
#Basic Frame of Columns Game
if __name__ == "__main__":
    rows = input()
    columns = input()
    rows =int(rows)
    columns =int(columns)
    faller = None
    matrix = [[0 for j in range(columns)] for i in range(rows) ]
    game = Game(matrix)
    emptyOrContents = input()
    if emptyOrContents == "EMPTY":
        game.printMatrix(matrix,faller)
    elif emptyOrContents == "CONTENTS":
        for i in range(rows):
            line = input()
            for j in range(columns):
                if line[j] == ' ':
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = line[j]
        game.is_freeze = True
        game.freeze(matrix,faller)
        game.printMatrix(matrix,faller)


    while True:
        command = input()
        flag =False;
        if command == '':
            flag = game.nexttick(matrix,faller)

        elif command.startswith("F"):
            faller = {}
            str = command.split(' ')
            faller['start'] = -2
            faller['is_land'] = 0
            faller['column'] =int(str[1]) -1
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

        elif command == '<':
            game.moveLeft(matrix,faller)
        elif command == '>':
            game.moveRight(matrix,faller)
        elif command == 'Q':
            exit(0)
        elif command == 'R':
            if faller is not None:
                faller['content'].insert(0,faller['content'].pop())

        if faller is not None and faller['is_delete'] == 1:
            faller = None
        game.printMatrix(matrix, faller)
        if flag:
            print("GAME OVER")
            exit(0)
