# Activity selection problem to select the no of activities

def printMaxActivities(jobs):
	n = len(jobs)
	jobs = sorted(jobs, key=lambda item: item[2])
	# print jobs
	i = 0
	print "First job: {}".format(jobs[i][0])
	for j in range(1, n):
		if jobs[j][1] >= jobs[i][2]:
			print "Next job: {}".format(jobs[j][0])
			i = j

if __name__ == '__main__':
	jobs = [['A1', 0, 6], ['A2', 3, 4], ['A3', 1, 2], ['A4', 5, 9], ['A5', 5, 7], ['A6', 8, 9]]
	printMaxActivities(jobs)

