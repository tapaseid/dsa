# Rat in a maze problem.

def _solveMazeUtil(maze, n, x, y, sol):

	# if x, y is destination, return true
	if x == n-1 and y == n-1:
		sol[x][y] = 'M'
		return True

	# check if maze[x][y] is valid
	if isSafe(maze, n, x, y):
		# mark x, y as a solution path
		sol[x][y] = 'M'

		# Move down in x direction
		if _solveMazeUtil(maze, n, x+1, y, sol):
			return True

		# if moving in x direction does not give solution,
		# then move forward in y direction
		if _solveMazeUtil(maze, n, x, y+1, sol):
			return True

		# if none of the above movements work, then
		# BACKTRACK: unmark x, y as a part of solution path
		sol[x][y] = '-'
		return False

def isSafe(maze, n, x, y):
	if x >= 0 and x < n and y >= 0 and y < n and maze[x][y] == 0:
		return True
	return False

def ratMaze(maze):
	n = len(maze)
	sol = [['-' for i in range(n)] for _ in range(n)]

	if _solveMazeUtil(maze, n, 0, 0, sol) == False:
		print "Solution does not exist!"
		return False

	printSolution(sol, n)
	return True

def countPaths(maze, r, c):
	# Time complexity O(r*c)
	
	if maze[0][0] == -1:
		return 0

	for i in range(r):
		if maze[i][0] == 0:
			maze[i][0] = 1
		else:
			break

	for i in range(1, c):
		if maze[0][i] == 0:
			maze[0][i] = 1
		else:
			break

	for i in range(1, r):
		for j in range(1, c):
			if maze[i][j] == -1:
				continue
			if maze[i-1][j] > 0:
				maze[i][j] += maze[i-1][j]
			if maze[i][j-1] > 0:
				maze[i][j] += maze[i][j-1]

	return maze[r-1][c-1]


def main():

	# 0: empty, -1: blocked
	# maze = [
	# 		[0, -1, -1, -1], 
	# 		[0, 0, -1, -1],
	# 		[-1, 0, -1, -1],
	# 		[0, 0, 0, 0]
	# 	   ]

	# ratMaze(maze)

	maze = [
			[0, 0, 0, 0],
			[0, -1, 0, 0],
			[-1, 0, 0, 0],
			[0, 0, 0, 0]
		   ]

	ratMaze(maze)
	r, c = 4, 4
	print countPaths(maze, r, c)
	

def printSolution(b, n):
	for i in range(n):
		for j in range(n):
			print b[i][j],
		print 

if __name__ == '__main__':
	main()
