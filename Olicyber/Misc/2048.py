from pwn import *
from math import *
from Crypto.Util.number import bytes_to_long 
# Creare una connessione TCP
conn = remote("2048.challs.olicyber.it", 10007)

conn.recvuntil(b":") #skip delle prime linee


for i in range(2048):
    
    
    t = conn.recvuntil(b" ").decode().strip()
    a = conn.recvuntil(b" ").decode().strip()
    b = conn.recvuntil(b" ").decode().strip()
    
    print(a, b, t, i)
    

    if(len(t) == 10):  #differenza

        a = int(a)
        b = int(b)
        result = a-b
        conn.send(str(result).encode() + b"\n")
        

    elif(len(t) == 5):     #somma

        a = int(a)
        b = int(b)
        result = a+b
        conn.send(str(result).encode()  + b"\n")

    elif(len(t) == 8):  #prodotto
        
        a = int(a)
        b = int(b)
        result = a*b
        conn.send(str(result).encode()  + b"\n" )
           
    elif(len(t) == 16):  #divisione_intera
                
        a = int(a)
        b = int(b)
        result = a//b
        conn.send(str(result).encode()  + b"\n" )

    
    elif(len(t) == 7):  #potenza
        a = int(a)
        b = int(b)
        result = a**b
        conn.send(str(result).encode()  + b"\n" )
        
        
conn.interactive()
        
        
    
