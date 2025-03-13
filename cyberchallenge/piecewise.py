from pwn import *

conn = remote('piecewise.challs.cyberchallenge.it', 9110)
flag = ''

while True:
    response = conn.recvuntil('(').decode().split()[:-1]
    conn.recvuntil(')')
    payload = ''

    print(f'response: {response}')

    if response[4] == 'number':
        print('porco diooooooooooooooooooooooooooooooooooooooooooooo')
        payload = ''
        
        number = int(response[5])  

        if response[9] == 'big-endian':
            print('big-endian')
            byteorder = 'big'
        else:
            print('little-endian')
            byteorder = 'little'

        if response[8] == '32-bit':
            print('32-bit')
            payload = number.to_bytes(4, byteorder=byteorder)
        else:  
            print('64-bit')
            payload = number.to_bytes(8, byteorder=byteorder)
        
        print(f'payload: {payload}')
        conn.send(payload)
                
    else:
        print('dio caneeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')
        conn.sendline(b'')
        

    response2 = conn.recvline(':')
    print(f'------------------response2 = {response2}------------------')
    flag += conn.recvline().decode()
    print(f'flag: {flag}')
    print('-------------------------------------------------------------')


