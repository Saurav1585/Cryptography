b=[0,0,0,1]
print("Initial\t b4\t List b\t	 Key")
key="blank"
for i in range(21):
	b4=b[-2]^b[-1]
	print(i,"\t",b4,"\t",b,"\t",key)
	key=b[-1]
	for j in range(1,len(b)):
		b[-j]=b[-j-1]
	b[0]=b4
