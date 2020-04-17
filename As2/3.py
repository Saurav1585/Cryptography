#key = 17
#key = 25
def additive_cipher(text,key):
    string=""
    for element in text:
        if element !=' ':
            ch=chr((ord(element)-97-key)%26+97)
            string+=ch
    return string

text=input("Enter cipher text:")
text.lower()
for key in range(1,26):
	print("Key = ",key,"  Plain Text =  ",additive_cipher(text,key))
