import socket
from math import gcd as bltin_gcd

def checkcoprime(p,q):
    return bltin_gcd(p, q) == 1

def numtostr(mssg):
    new_text = ''
    for i in range(int(len(mssg)/2)):
        temp = mssg[i*2:i*2+2]
        temp = int(temp)
        temp = temp + 97
        temp = chr(temp)
        new_text = new_text + temp
    return new_text

def decmssg(mssg, private_key):
    mssg = int(mssg)
    mssg = (pow(mssg, private_key[0])) % private_key[1]
    mssg = str(mssg)
    return mssg

def RSA_Key_Generation():
    p = int(input("Select P "))
    q = int(input("Select Q "))
    while((checkcoprime(p,q)) == False):
    	print("P and Q are not coprime")
    	q = int(input("Again Select Q ")) 
    
    n = p*q
    phi = (p-1)*(q-1)
    e = int(input("Select E "))
    while(checkcoprime(e,phi) == False):
    	print("(P-1)*(Q-1) and E are not coprime")
    	e = int(input("Again Select E "))

    i = 1
    while(True):
        if((e*i)%phi == 1):
            break
        else:
            i += 1
    
    d = i
    public_key = (e,n)
    private_key = (d,n)

    return (public_key,private_key)




HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    public_key, private_key = RSA_Key_Generation()
    #sending public key to other pc
    #print(public_key[1])
    s.sendall(str(public_key[0]).encode())
    con = s.recv(1024)
    s.sendall(str(public_key[1]).encode())
    print("public key = {}".format(public_key))
    print("private_key = {}".format(private_key))
    while(True):
        mssg = s.recv(1024)
        mssg = str(mssg.decode())
        print('Message before decryption = ' + mssg)
        mssg = decmssg(mssg,private_key)
        print("Message after decryption = {}".format(mssg))
        mssg = numtostr(mssg)
        print("Message after converting it into char = {}".format(mssg))
        

