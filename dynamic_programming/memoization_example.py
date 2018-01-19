#compute factorial

#staright forward approach for memoization

# fact_memo = {}
# def factorial(n):
# 	if n<0:
# 		print "invalid!"
# 		return
# 	if n<2:
# 		return 1
# 	if n not in fact_memo:
# 		fact_memo[n] = n*factorial(n-1)
# 	return fact_memo[n]
# print factorial(10)
# print fact_memo


# #using decorator

# class Memoize:
# 	def __init__(self, f):
# 		self.f = f
# 		self.memo = {}
# 	def __call__(self, *args):
# 		if not args in self.memo:
# 			self.memo[args] = self.f(*args)
# 		return self.memo[args]
# @Memoize
# def fact(k):
# 	if k < 2: return 1
# 	return k*fact(k-1)

# print fact(3)




#fibonacci like series

ft_mem = {}

def ft(n1, n2, k):
	if k < 1:
		print "Invalid input!"
		return
	if k == 1:
		return n1
	if k == 2:
		return n2
	if k not in ft_mem:
		ft_mem[k] = ft(n1, n2, k-1)*ft(n1, n2, k-1) + ft(n1, n2, k-2)
	return ft_mem[k]

n1, n2, k = [int(i) for i in raw_input("Give input of 3 numbers: ").split(' ')]
print ft(n1, n2, k)
