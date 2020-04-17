def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
def multiplicative_inverse(a, b):
	for i in range(1, a):
		if (i * b) % a == 1:
			return i

def multiplicative_cipher(text,key1):
    string=""
    if(gcd(26,key1))!=1:
        #print("inverse of key is not in Zn")
        return
    key=multiplicative_inverse(26,key1)
    for element in text:
        if element !=' ':
                ch=chr(((ord(element)-65)*key)%26+65)
                string+=ch            
    return string

text=input("Enter cipher text:")
text.upper()
for key in range(1,26):
	print("Key = ",key,"  Plain Text =  ",multiplicative_cipher(text,key))
