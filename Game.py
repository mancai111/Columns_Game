import pygame
#Game Mechanics
class Game:
    is_freeze = False
    black    = (   0,   0,   0)
    white    = ( 255, 255, 255)
    green    = (   0, 255,   0)
    red      = ( 255,   0,   0)
    blue     = ( 0, 0, 255)
    purple     = ( 0, 255, 255)
    yellow    = (255,255, 0)
    yellow2 = (255,0,255)
    color_list= [black,green,red,blue,purple,yellow]
    char_dict = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5}
    w = 700
    h = 600
    cell_w = 0
    cell_h = 0
    
    def __init__(self,matrix):
        rows = len(matrix)
        columns = len(matrix[0])

        self.status  = [[0 for j in range(columns)] for i in range(rows) ]
        
    def resize_surface(self,size:(int,int)) -> None:
        pygame.display.set_mode(size , pygame.RESIZABLE)
        
    def printMatrix(self,matrix,faller,surface):
        rows = len(matrix)
        columns = len(matrix[0])
        self.cell_w = self.w/columns
        self.cell_h = self.h/rows

        for i in range(rows):

            print("|",end='')
            for j in range(columns):

                if faller is not None and j == faller['column'] and i >= faller['start'] and i< faller['start'] + 3:
                    pygame.draw.rect(surface, self.color_list[self.char_dict[faller['content'][i -faller['start']]]],
                                     [j*self.cell_w,i*self.cell_h,self.cell_w,self.cell_h])
                    print(('|' if faller['is_land'] == 1 else "[")+ faller['content'][i - faller['start']] +('|' if faller['is_land'] == 1 else "]"),end='')
                elif matrix[i][j] == 0:
                    pygame.draw.rect(surface, self.white,
                                     [j*self.cell_w,i*self.cell_h,self.cell_w,self.cell_h])
                    print("   ",end='')
                else:
                    if self.status[i][j] ==1:
                        print("*"+matrix[i][j]+"*",end='')
                    else:
                        print(" "+matrix[i][j]+" ",end='')
                    pygame.draw.rect(surface, self.color_list[self.char_dict[matrix[i][j]]],
                                    [j*self.cell_w,i*self.cell_h,self.cell_w,self.cell_h])
            print("|")

        print(" ", end='')
        for j in range(columns):
            print("---",end='')
        print(" ")


    def judgeLand(self,matrix,faller):
        if faller['start']+3 == len(matrix) or matrix[faller['start']+3][faller['column']] != 0:
            faller['is_land'] = 1
        else:
            faller['is_land'] = 0

    def moveLeft(self,matrix, faller):
        if faller['column'] -1 >= 0 and matrix[max(faller['start'],0)][faller['column']- 1] == 0 and matrix[max(faller['start']+1,0)][faller['column']- 1] == 0 and matrix[max(faller['start']+2,0)][faller['column']- 1] == 0:
            faller['column'] =faller['column'] -1
            self.judgeLand(matrix,faller)


    def moveRight(self,matrix, faller):
        if faller['column'] + 1 < len(matrix[0]) and matrix[max(faller['start'],0)][faller['column'] + 1] == 0 and matrix[max(faller['start']+1,0)][faller['column'] + 1] == 0 and matrix[max(faller['start']+2,0)][faller['column'] + 1] == 0:
            faller['column'] = faller['column'] + 1
            self.judgeLand(matrix,faller)

    def freeze(self,matrix, faller):
        rows = len(matrix)
        columns = len(matrix[0])
        flag =False
        if faller is not None:
            if faller['start'] < 0:
                flag =True
            matrix[max(faller['start']+ 0,0)][faller['column']] = faller['content'][0]
            matrix[max(faller['start']+ 1,0)][faller['column']] = faller['content'][1]
            matrix[max(faller['start']+ 2,0)][faller['column']] = faller['content'][2]
            faller['is_delete'] = 1
        if self.is_freeze:
            self.clearMatch(matrix)
        self.is_freeze = self.findMatch(matrix)
        return flag
    def clearMatch(self,matrix):
        rows = len(matrix)
        columns = len(matrix[0])
        for j in range(columns):
            start =rows-1
            i = rows-1
            while i >= 0:
                if start>= 0 and (self.status[start][j] ==1 or matrix[start][j] == 0):
                    start -=1
                else:
                    matrix[i][j] = 0 if start < 0 else matrix[start][j]
                    i -=1
                    start -=1
        return
    def findMatch(self,matrix):
        rows = len(matrix)
        columns = len(matrix[0])
        self.status  = [[0 for j in range(columns)] for i in range(rows) ]
        flag =False
        for i in range(rows):
            start = 0
            for j in range(columns+1):
                if j< columns and matrix[i][j]!=0  and matrix[i][j] == matrix[i][start]:
                    continue
                else:
                    if j - start >= 3:
                        flag = True
                        for k in range(start,j):
                            self.status[i][k]=1
                    start = j
        return flag
    def nexttick(self,matrix, faller):
        rows =len(matrix)
        columns = len(matrix[0])

        if self.is_freeze:
            return self.freeze(matrix,faller)
        if faller is not None:
            if faller['is_land'] == 1:
                return self.freeze(matrix,faller)
            else:
                faller['start'] += 1
                self.judgeLand(matrix,faller)

        return
