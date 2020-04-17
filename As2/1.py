# a1 x+a2 = a3(mod a4)
def gcd(x,y):
	if y == 0:
		return x
	return gcd(y,x%y)

def additive_inverse(n, b):
	if n-b < n:
		return n-b


def multiplicative_inverse(n, b):
	if gcd(n,b) !=1:
		return
	for i in range(1, n):
		if (i * b) % n == 1:
			return i	
			
def ciper(a,b,c,d):
	x=gcd(a,d)
	c1=(c + d-b)%d
	#c1=c
	if c1%x !=0:
		return
	ans=[]
	a=a/x
	c1=(c1/x * multiplicative_inverse(d, a))%d
	ans.append(c1)
	i=0
	for i in range(1,x):
		ans.append(c1+i*(d/x))
	return ans
		



a1, a2, a3, a4 = map(int, input().split())
print(ciper(a1,a2,a3,a4))
