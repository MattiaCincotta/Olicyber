from pwn import *
from Crypto.Util.number import bytes_to_long, long_to_bytes
import base64
import json

# Creare una connessione TCP
conn = remote("based.challs.olicyber.it", 10600)

conn.recvuntil(b"\n") #skip delle prime linee
conn.recvuntil(b"\n") #skip delle prime linee
conn.recvuntil(b"\n") #skip delle prime linee
conn.recvuntil(b"\n") #skip delle prime linee


def binario_a_stringa(valore_binario):

    valore_intero = int(valore_binario, 2)
    return long_to_bytes(valore_intero).decode()


count = 0
stringa1 = '{"answer": "'
stringa2 = '"}'

while True:
    count+=1
    print(count)
    
    conn.recvuntil(b"Converti questo ")
    direction = conn.recvuntil(b" ")
    base = conn.recvuntil(b"!").decode() #prendo fino allo spazio dopo il punto esclamativo
    
    conn.recvuntil(b": \"")
    message = conn.recvuntil(b'"')
    message = message[0:len(message)-1]
    
    #print(base.decode(), len(base), direction.decode(), len(direction), message.decode())
    
        
                
    if base == "base64!":  #base64        
        
        #print("base64")
                
        if len(direction) == 3:   #da 
            
            #print("sono dentro  da")

            
            result = base64.b64decode(message).decode()

        elif len(direction) == 2:  #a      
            
            #print("sono dentro  a")
            
            
            result = base64.b64encode(message).decode()
            
            #print("risultato = " + result)

    
    elif len(base) > 17 or base == "binario!": #caso binario
        
        #print("bin")


        if len(direction ) == 3:   #da         #TOFIX
            
            #print("sono dentro  da")
  

            result = binario_a_stringa(message)
            

        elif len(direction) == 2:  #a          
            
            #print("sono dentro  a")

            
            result = ''.join(format(byte, '08b') for byte in message)
            while result[0] == "0":
                result = result[1:]
        
        
    elif base == "esadecimale!": #caso esadecimale
        
        #print("hex")


        if len(direction) == 3:   #da             
            
            #print("sono dentro  da")

            message = int(message, 16)
            result = long_to_bytes(message).decode()
            
            

        elif len(direction) == 2:  #a   
                       
            #print("sono dentro  a")

            #trasformi message in int e lo converti ad hex
            message = bytes_to_long(message)
            #trasforma message in bytes e poi in stringa
            result = hex(message)[2:]
        
    
    
    Finalresult ={
            "answer": result,
        }
    
    print(Finalresult)
    
    conn.sendline(json.dumps(Finalresult))