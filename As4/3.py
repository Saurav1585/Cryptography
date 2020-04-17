import numpy as np
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''' '

def create(key_text):
	sor=set(key_text)
	sor=list(sor)
	sor.sort()
	for i in range(len(sor)):
		for j in range(len(key_text)):
			if(sor[i]==key_text[j]):
				#print(key_text)
				key_text[j]=i+1
	#print(key_text)
	return key_text

def new_text(text,row):
    temp=[]               
    for i in range(0,len(text)):
        if text[i] not in punctuations: 
               tex=(ord(text[i])-97)
               temp.append(tex)
               
    text=temp

    while len(text)%row!=0:
        text.append(25)
        
    return text   

def trans_cipher(key,text):
	result=np.dot(text,key)
	#print(result)
	text=[]
	for i in range(7):
		for j in range(len(result)):
			text.append(chr(result[j][i]+97))
	text=(''.join(text)).upper()
	return(text)

key_text="SWINDON"
key_text=list(key_text)
key=create(key_text)
#key=[5,6,2,3,1,4,3]
row=max(key)
col=len(key)
s_key= np.zeros([row,col], dtype = int)
for i in range(col):
	s_key[key[i]-1][i]=1
#print(s_key) 
#text=input("Enter Plain Text:")
text="A Midsummer Night's Dream, which is a comedy written by Shakespeare."
print("Plain Text : ",text)
text=text.lower()
text=new_text(text,row)
length=len(text)//row
text_array=np.array(text).reshape(length,row)
#print("Modified Plain Text :",text)
print("Cipher Text :",trans_cipher(s_key,text_array))
