# The N Queen problem is the problem of placing n chess queens on an n*n
# chess-board so that no two queens attack each other.

def _is_safe(board, n, row, col):

	# check this row left side
	for i in range(col):
		if board[row][i] == 1:
			return False

	# check upper diagonal on left side
	for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
		if board[i][j] == 1:
			return False

	# check lower diagonal on left side
	for i, j in zip(range(row, n, 1), range(col, -1, -1)):
		if board[i][j] == 1:
			return False

	return True


def _solveNQueen(board, n, col):
	if col >= n:
		return True

	for i in range(n):
		if _is_safe(board, n, i, col):
			board[i][col] = 1

			if _solveNQueen(board, n, col+1) == True:
				return True

			board[i][col] = 0

	return False

def main():
	board = [
			 [0, 0, 0, 0],
			 [0, 0, 0, 0],
			 [0, 0, 0, 0],
			 [0, 0, 0, 0]
			]

	n = len(board)
	if _solveNQueen(board, n, 0) == False:
		print"Solution does not exist!"
		return False

	_printSolution(board, n)
	return True

def _printSolution(board, n):
	for i in range(n):
		for j in range(n):
			print board[i][j],
		print

if __name__ == '__main__':
	main()
