import numpy as np
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~''''" '

def search(element,key):
    temp=np.where(key==element)
    pos=list(zip(temp[0],temp[1]))
    return pos

def mod(n):
    return n%5

def new_text(text):
    temp=""                
    for i in range(0,len(text)):
        if text[i] == 'j':
        	text[i] = 'i'
        if text[i] not in punctuations: 
               temp=temp+text[i]
               
    text=temp
    for i in range(0,len(text)-1):
        if text[i]==text[i+1]:
            if text[i]!='x':
                text=text[:i+1]+'z'+text[i+1:]
            else:
                text=text[:i+1]+'y'+text[i+1:]            
    
    if len(text)%2!=0:
        text=text+'z'
        
    return text   

def playfair_cipher(key,text):
    list_ = [(text[i:i+2]) for i in range(0, len(text), 2)]
    print(list_)
    
    new_text=""
    
    for element in list_:
        temp1=search(element[0],key)
        x1,y1=temp1[0][0],temp1[0][1]
        
        temp2=search(element[1],key)
        x2,y2=temp2[0][0],temp2[0][1]
        
        if y1==y2:
            new_text+=key[mod(x1+1)][y1]+key[mod(x2+1)][y2]            
        elif x1==x2:
            new_text+=key[x1][mod(y1+1)]+key[x2][mod(y2+1)]
        else:
            new_text+=key[x1][y2]+key[x2][y1]
    
    return new_text
#“COMMONLOUNGE”

def create_key(string):
    secret_key=['l','g','d','b','a','q','m','h','e','c','u','r','n','i','f','x','v','s','o','k','z','y','w','t','p']
    update_key=[string[0]]
    for ch in string[1:]:
        if ch not in update_key:
            update_key.append(ch)
    for ch in secret_key:
        if ch not in update_key:
            update_key.append(ch)
    return update_key

key="commonlounge"
secret_key=create_key(key)
key=np.array(secret_key).reshape(5,5)
#file=open("file1.txt",'r')
#text=file.read().lower()
text=input("Enter Plain Text:")
text=text.lower()
text=new_text(text)
print("Modified Plain Text :",text)
print("Cipher Text :",playfair_cipher(key,text))
