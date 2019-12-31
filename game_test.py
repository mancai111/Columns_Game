import unittest
from Game import Game

#unittest

class TestGame(unittest.TestCase):

    def test_init(self):
        faller = None
        matrix = [[0 for j in range(3)] for i in range(4) ]
        game = Game(matrix)
        self.assertEqual(len(game.status), 4)
        self.assertEqual(len(game.status[0]), 3)

    def test_judgeland(self):
        faller = {}
        faller['start'] = -2
        faller['is_land'] = 0
        faller['column'] = 2

        matrix = [[0 for j in range(3)] for i in range(4) ]
        game = Game(matrix)
        game.judgeLand(matrix,faller)
        self.assertEqual(faller['is_land'], 0)

    def test_moveleft(self):
        faller = {}
        faller['start'] = -2
        faller['is_land'] = 0
        faller['column'] = 2

        matrix = [[0 for j in range(3)] for i in range(4) ]
        game = Game(matrix)
        game.moveLeft(matrix,faller)
        self.assertEqual(faller['column'], 1)

    def test_moveright(self):
        faller = {}
        faller['start'] = -2
        faller['is_land'] = 0
        faller['column'] = 1

        matrix = [[0 for j in range(3)] for i in range(4) ]
        game = Game(matrix)
        game.moveRight(matrix,faller)
        self.assertEqual(faller['column'], 2)

    def test_findmatch(self):
        faller = {}
        faller['start'] = -2
        faller['is_land'] = 0
        faller['column'] = 1

        matrix = [[0 for j in range(3)] for i in range(4) ]
        matrix[3][0] = 'X'
        matrix[3][1] = 'X'
        matrix[3][2] = 'X'
        game = Game(matrix)
        game.findMatch(matrix)
        self.assertEqual(game.status[3][0], 1)
        self.assertEqual(game.status[3][1], 1)
        self.assertEqual(game.status[3][2], 1)
