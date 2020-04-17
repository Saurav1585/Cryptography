def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

def additive_cipher(text,key):
    string=""
    for element in text:
        if element !=' ':
            ch=chr((ord(element)-97+key)%26+97)
            string+=ch
    return string

def multiplicative_cipher(text,key):
    string=""
    if(gcd(26,key))!=1:
        print("inverse of key is not in Zn")
        return
    for element in text:
        if element !=' ':
                ch=chr(((ord(element)-97)*key)%26+97)
                string+=ch            
    return string

def affine_cipher(text,key1,key2):
    string=""
    if (gcd(26,key2))!=1:
        print("inverse of second key is not in Zn")
        return
    string=multiplicative_cipher(text,key2)
    string=additive_cipher(string,key1)
    #string=multiplicative_cipher(string,key2)
    return string

text=input("Enter Plain Text:")
key1=int(input("Enter key1: "))
key2=int(input("Enter key2: "))
print("Additive Cipher Text: ",additive_cipher(text,key1))
print("Multiplicative Cipher Text: ",multiplicative_cipher(text,key2))
print("Affine Cipher Text: ",affine_cipher(text,key1,key2))
