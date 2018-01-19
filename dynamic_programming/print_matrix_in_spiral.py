# The idea is to print matrix in spiral form

def print_matrix_in_spirla(matrix, m, n):
	# Time complexity O(mn)
	
	r = c = 0

	while r < m and c < n:
		
		for i in range(c, n):
			print matrix[r][i],
		r += 1
		
		for i in range(r, m):
			print matrix[i][n-1],
		n -= 1

		if r < m:
			for i in range(n-1, c-1, -1):
				print matrix[m-1][i],
			m -= 1

		if c < n:
			for i in range(m-1, r-1, -1):
				print matrix[i][c],
			c += 1


if __name__ == '__main__':
	matrix = [[1, 2, 3, 4, 5],
			 [6, 7, 8, 9, 10],
			 [11, 12, 13, 14, 15]]
	print_matrix_in_spirla(matrix, 3, 5)
