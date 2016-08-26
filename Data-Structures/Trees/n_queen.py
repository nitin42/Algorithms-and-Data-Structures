from itertools import *
import copy

class Board:
    ''' A class to represent the checker board'''
    def __init__(self , n): #Initializes the class
        self.board = [ [ None  for i in range(8) ] for i in range(8) ] 
        self.pieces = set()

    def PlaceQueen(self,row,column):
        '''Places a queen at row,column'''
        self.pieces.add( (row , column) )
        self.board[row][column] = 'Q'

    def RemoveQueen(self,row,column): 
        '''Removes a queen from a given 'row' and 'column' '''
        self.board[row][column] = None
        self.pieces.remove( ( row , column ) )

    def isAttacking( self,  piece1 , piece2  ):
        '''Checks if piece1 attacks piece2'''
        if piece1[0] == piece2[0] or piece1[1] == piece2[1]: #Check if they are in same row or col
            return True
        '''Time to check if they are attacking diagonally
         This can be done efficiently via simple algebra
         The two pices are on the same diagonal if they
         satisfy an equation of a line containing the two points'''
        x1 , y1 , x2 , y2 = piece1[1] , piece1[0] ,piece2[1] ,piece2[0]
        m = float(y2 - y1) / (x2 - x1)
        if abs(m) != 1.0:
            return False
        else:
            b = y2 - m * x2
            return y1 == m * x1 + b

    def isAttackingAny( self , piece ):
        '''Checks if piece is being atacked by
           any other piece in the board'''
        for piece1 in self.pieces:
            if self.isAttacking(piece,piece1):
                return True
        return False


def NQueens( board , n ):
    if n == 0:
        return [board]
    solutions = []
    i = 0
    for piece1 in product(range(8),repeat=2):
        if piece1 in board.pieces:
            continue
        if not board.isAttackingAny(piece1):
            i += 1
            fresh = copy.deepcopy(board)
            fresh.PlaceQueen(piece1[0] , piece1[1] )
            solutions += NQueens( fresh , n - 1 ) 
    return solutions