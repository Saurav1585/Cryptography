def gcd(x,y):
	if y == 0:
		return x
	return gcd(y,x%y)

x, y = map(int, input().split())
print ("euclidean gcd:", gcd(x,y))


