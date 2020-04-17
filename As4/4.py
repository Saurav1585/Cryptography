print("(P2(010011110) X P1(100110))mod(100011011)")
#p2="010011110"
#p1="100110"
#mod="100011011"
p1=input("Enter P1:")
p2=input("Enter P2:")
mod=input("Enter Modulus:")

l=len(mod)
while(len(p2)!=l):
	p2="0"+p2

result="000000000"
p1= "".join(reversed(p1))
#print(p1)
if(p1[0]=="1"):
	result=p2

for i in range(1,len(p1)):
	#Left Shift
	p2=p2[1:]+"0"
	
	if(p2[0]=="1"):
		#Reduction
		p2 = int(p2,2) ^ int(mod,2)
		p2=('{0:b}'.format(p2))
	#Bit Padding
	while(len(p2)!=l):
		p2="0"+p2
	#XOR with Result
	if(p1[i]=="1"):
		result=int(p2,2) ^ int(result,2)
		result=('{0:b}'.format(result))
	while(len(result)!=8):
		result="0"+result
print("(P1("+p1+") X P2("+p2+")) Modulus("+mod+") = ",result)
