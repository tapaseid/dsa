
class Queue_Entry:
	def __init__(self, v=0, dist=0):
		self.v = v
		self.dist = dist

def get_min_dice_throw(moves, n):
	visited = [False]*n
	queue = []

	visited[0] = True
	queue.append(Queue_Entry(0, 0))

	qe = Queue_Entry()
	while queue:
		qe = queue.pop(0)
		v = qe.v

		if v == n-1:
			break
		j = v+1
		while j <= v+6 and j < n:
			if visited[j] == False:
				a = Queue_Entry()
				a.dist = qe.dist + 1
				visited[j] = True
				a.v = moves[j] if moves[j] != -1 else j
				queue.append(a)
			j += 1
	return qe.dist


def main():
	n = 30
	moves = [-1]*n

	# Ladder
	moves[2] = 21
	moves[4] = 7
	moves[10] = 25
	moves[19] = 28

	# Snakes
	moves[26] = 0
	moves[20] = 8
	moves[16] = 3
	moves[18] = 6

	print get_min_dice_throw(moves, n)

if __name__ == '__main__':
	main()
