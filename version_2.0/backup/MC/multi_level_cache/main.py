import sys, random

def shift(l):
	i = l
	while i > 0:
		if len(cache[i-1]) == capacity:
			r = random.randint(0, capacity)
			k = cache[i-1].keys()[r-1]
			v = cache[i-1][k]				
			del cache[i-1][k]
			cache[i][k] = v
		i -= 1

def _read(key):
	print "#### READ OPERATION #####"

	for i in range(max_level):
		if cache[i].get(key):
			v = cache[i].get(key)
			if i > 0:
				del cache[i][key]
				shift(i)
				cache[0][key] = v
			print "Key {} found at level {}, value is {}".format(key, i+1, v)
			print cache
			return
	print "Key {} not found!".format(key)
	print "cache: ", cache
	return


def _write(key, val):
	print "#### WRITE OPERATION #####"
	
	if len(cache[0]) < capacity:
		cache[0][key] = val
	else:
		if len(cache[-1]) == capacity:
			print "Oops, cache is full!"
		else:
			shift(max_level-1)
			cache[0][key] = val

	print "cache: ", cache
	return


def main():
	with open('sample_data') as fh:
		data = fh.readlines()
	for d in data:
		d = d.strip('\n').split(' ')
		print 'DATA -----> ', d
		if d[0] == 'w':
			_write(d[1], d[2])
		elif d[0] == 'r':
			_read(d[1])
		else:
			print "Invalid operation!"

		print 

if __name__ == '__main__':
	with open('config') as fh:
		config = fh.readlines()
	max_level = int((config[0].strip('\n').split('='))[-1])
	capacity = int((config[1].strip('\n').split('='))[-1])

	print "Max level = {}, capacity = {}".format(max_level, capacity)
	cache = [dict() for _ in range(max_level)]
	print "cache: ", cache
	main()

