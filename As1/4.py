def additive_inverse(n):
	ans = [(0,0)]
	for i in range(1, n//2+1):
		ans.append((i, n-i))
	return ans


def multiplicative_inverse(n):
	ans = []
	for i in range(1, n):
		for j in range(i, n):
			if (i * j) % n == 1:
				ans.append((i, j))

	return ans

n=int(input("Enter n: "))
print ("additive inverse:", additive_inverse(n))
print ("multiplicative inverse:", multiplicative_inverse(n))


