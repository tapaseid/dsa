# Calculate minimum no of platform required

def minPlatformRequired(a, d):
	a.sort()
	d.sort()
	n = len(a)

	platform_needed = 1; result = 1

	i = 1
	j = 0
	while i < n and j < n:
		if a[i] < d[j]:
			platform_needed += 1
			i += 1
			if platform_needed > result:
				result = platform_needed
		else:
			platform_needed -= 1
			j += 1
	return result

if __name__ == '__main__':
	arrival = [900, 940, 950, 1100, 1500, 1800]
	departure = [910, 1200, 1120, 1130, 1900, 2000]
	print minPlatformRequired(arrival, departure)
