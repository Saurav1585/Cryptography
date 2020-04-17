def gcd(x,y):
	if y == 0:
		return x
	return gcd(y,x%y)
	
def extended_additive_inverse(n, b):
	if n-b < n:
		return n-b


def extended_multiplicative_inverse(n, b):
	if gcd(n,b) !=1:
		return
	for i in range(1, n):
		if (i * b) % n == 1:
			return i

n, b = map(int, input().split())
print ("extended additive inverse:", extended_additive_inverse(n, b))
print ("extended multiplicative inverse:", extended_multiplicative_inverse(n, b))


