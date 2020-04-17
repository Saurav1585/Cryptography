def ex_gcd(a, b):
	r1 = a
	r2 = b
	t1 = 0
	t2 = 1
	while r2 > 0:
		q = r1 // r2
		r = r = r1 - q * r2
		r1 = r2
		r2 = r
		t = t1 - q * t2
		t1 = t2
		t2 = t

	if r1 == 1:
		b_inv = t1
		return (r1, b_inv)

	return r1
x, y = map(int, input().split())
print ("extended euclidean gcd:", ex_gcd(x,y))


