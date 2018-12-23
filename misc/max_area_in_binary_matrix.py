def hist_area(hist, n):
	s = []
	max_area = 0
	i = 0
	while i<n:
		if not s:
			s.append(i)
			i += 1
		else:
			if hist[s[-1]] <= hist[i]:
				s.append(i)
				i += 1
			else:
				tp = s.pop()
				curr_area = hist[tp]*(i-s[-1]-1 if s else i)
				max_area = max(max_area, curr_area)

	while s:
		tp = s.pop()
		curr_area = hist[tp]*(i-s[-1]-1 if s else i)
		max_area = max(max_area, curr_area)
	return max_area

def find_max_rect_area(matrix, r, c):
	lst = [0 for _ in range(c)]
	result_area = 0
	for i in range(r):
		for j in range(c):
			if matrix[i][j] == 0:
				lst[j] = 0
			else:
				lst[j] += 1
		tmp_area = hist_area(lst, len(lst))
		result_area = max(result_area, tmp_area)
	return result_area

if __name__ == '__main__':
	matrix = [[1, 0, 0, 1, 1, 1],
			  [1, 0, 1, 1, 0, 1],
			  [0, 1, 1, 1, 1, 1],
			  [0, 0, 1, 1, 1, 1]
			 ]
	r = len(matrix)
	c = len(matrix[0])
	print find_max_rect_area(matrix, r, c)
