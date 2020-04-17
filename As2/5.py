def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

def multiplicative_inverse(a, b):
	for i in range(1, a):
		if (i * b) % a == 1:
			return i

def additive_cipher(text,key):
    string=""
    for element in text:
        if element !=' ':
            ch=chr((ord(element)-65-key)%26+65)
            string+=ch
    return string

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

def affine_cipher(text,key1,key2):
    string=""
    str1="AB"
    if (gcd(26,key2))!=1:
        #print("inverse of second key is not in Zn")
        return 0
    string=additive_cipher(text,key1)
    string=multiplicative_cipher(string,key2)
    #string=additive_cipher(string,key1)
    if(string==str1):
    	return 1
    return 0

def affine_cipher1(text,key1,key2):
    string=""
    if (gcd(26,key2))!=1:
        #print("inverse of second key is not in Zn")
        return
    string=additive_cipher(text,key1)
    string=multiplicative_cipher(string,key2)
    #string=additive_cipher(string,key1)
    return string

text=input("Enter cipher text:")
C1=0
text.lower()
for key1 in range(1,26):
	for key2 in range(1,26):
		if((affine_cipher("GL",key1,key2))==1):
			C1=1
			break
	if(C1==1):
		break
print(key1)
print(key2)
print("Affine Plain Text: ",affine_cipher1(text,key1,key2).lower())


#XPALASXYFGFUKPXUSOGEUTKCDGFXANMGNVS



