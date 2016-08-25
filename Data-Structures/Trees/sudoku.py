'''
Recursive Backtracking - A refined brute force method. This solve a sudoku puzzle using
recursive backtraking algorithm.

'''

from itertools import *
from copy import copy

def distinct_n(l):

	'''
	>>> Board = [[ 0 , 0 , 0 ],[ 1 , 0 , 0 ],[ 0 , 3 , 1 ]]
	>>> sudoku(Board, 6)
	>>> print Board
	[[3 , 1 , 2],[ 1 , 2 , 3 ],[ 2 , 3 , 1 a]]
	
	'''

	'''
	To check all the numbers in the board are distinct. (Ignoring 0's)
	'''

	arr = [] # Stores the distinct numbers

	for i in l:
		if i == 0:
			continue

		if i in arr:
			return False
		
		arr.append(i)

	return True # If numbers are already distincts in the list.


def is_valid(board): 
	'''
	To check whether the board is valid or not.
	'''
	for i in range(3):
		row = [board[i][0], board[i][1], board[i][2]]
		if not distinct_n(row):
			return False
		col = [board[0][i], board[1][i], board[2][i]]
		if not distinct_n(col):
			return False
	return True # If the board is already sorted


def sudoku(board, empty=9):
	'''
	Solve the sudoku board with empty is number of empty cells.
	'''
	if empty == 0:
		return is_valid(board) # Sudoku is already completed 

	for row, col in product(range(3), repeat=2):
		cell = board[row][col]
		if cell != 0:
			continue

		board2 = copy(board)

		for i in [1,2,3]:
			board2[row][col] = i # Check for the all three values in each cell
			if is_valid(board2) and sudoku(board2, empty-1):
				return True

			board2[row][col] = 0 # Start backtrack as soon as zero is encountered

	return False			


if __name__ == '__main__':
	import doctest
	doctest.testmod(verbose=True)










