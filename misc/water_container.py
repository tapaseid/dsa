def amount_of_water(Wtr, R, C):
	arr = []
	for i in range(R+1):
		arr.append([0 for _ in range(i+1)])
	
	print arr
	arr[0][0] = Wtr
	for i in range(R):
		for j in range(i+1):
			if arr[i][j] > 1:
				x = arr[i][j]
				arr[i][j] = 1
				arr[i+1][j] += (x-1)/2.0
				arr[i+1][j+1] += (x-1)/2.0

	print arr
	return arr[R][C]

if __name__ == '__main__':
	print amount_of_water(10, 4, 3)
