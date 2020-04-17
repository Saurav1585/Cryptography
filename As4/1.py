import numpy as np
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''' '

def new_text(text):
    temp=[]               
    for i in range(0,len(text)):
        if text[i] not in punctuations: 
               tex=(ord(text[i])-97)
               temp.append(tex)
               
    text=temp

    while len(text)%5!=0:
        text.append(25)
        
    return text   

def double_cipher(key,text):
	result=np.dot(text,key)
	text=[]
	#print(result)
	for i in range(5):
		for j in range(len(result)):
			text.append(result[j][i])
	#print("Middle Text : ",text)
	length=len(text)//5
	text_array=np.array(text).reshape(length,5)
	result=np.dot(text_array,key)
	text=[]
	for i in range(5):
		for j in range(len(result)):
			text.append(chr(result[j][i]+97))
	text=(''.join(text)).upper()
	return text

key=[3,1,4,5,2]
s_key= np.zeros([5, 5], dtype = int)
for i in range(5):
	s_key[key[i]-1][i]=1
#print(s_key) 
#text=input("Enter Plain Text:")
text="Enemy attacks tonight"
print("Plain Text : ",text)
text=text.lower()
text=new_text(text)
length=len(text)//5
text_array=np.array(text).reshape(length,5)
#print("Modified Plain Text :",text)
print("Cipher Text :",double_cipher(s_key,text_array))
