# Remove duplicates from a given string 
# and return unique charater constructed string

def toMutable(string):
	temp = []
	for i in string:
		temp.append(i)
	return temp

def toString(lst):
	return "".join(lst)

def removeDuplicatesSorted(l):
	i = 1
	j = 1
	while i < len(l):
		if l[i] != l[i-1]:
			l[j] = l[i]
			j += 1
		i += 1
	return toString(l[:j])

def removeDuplicatesInOrderd(l):
	hash_map = [0]*256
	i = 0
	j = 0
	while i < len(l):
		if hash_map[ord(l[i])] == 0:
			hash_map[ord(l[i])] = 1
			l[j] = l[i]
			j += 1
		i += 1
	return toString(l[:j])

def removeDups(string):
	l = toMutable(string)
	# return removeDuplicatesInOrderd(l)

	l.sort()
	return removeDuplicatesSorted(l)

if __name__ == '__main__':
	s = "geeksforgeeks"
	print removeDups(s)
