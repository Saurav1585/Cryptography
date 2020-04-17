punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''' ' 

def new_text(text):
    temp=""                
    for i in range(0,len(text)):
        if text[i] not in punctuations: 
               temp=temp+text[i]     
    return temp


def vigenere_cipher(text,key):
    cipher_text=""
    for i in range(0,len(text)):
        cipher_text+=chr(((ord(text[i])-97)+(ord(key[i%len(key)])-97))%26+97)
    return cipher_text    
                

text=input("Enter Plain Text:")
text=text.lower()
key="pascal"
text=new_text(text)
print(text)
print("Cipher Text:",vigenere_cipher(text,key))
