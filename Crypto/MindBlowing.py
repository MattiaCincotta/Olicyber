#!/usr/bin/env python3
from pwn import *
from ast import literal_eval

def main():

    r = remote('mindblowing.challs.pascalctf.it', 420)

    r.recvuntil(b"> ")
    r.sendline(b"1")

    r.recvuntil(b"Gimme the index of a sentence:")
    r.sendline(b"2")

    r.recvuntil(b"Gimme the number of seeds:")
    n = 512
    r.sendline(str(n).encode())

    for i in range(n):
        prompt = f"Seed of the number {i+1}: ".encode()
        r.recvuntil(prompt)
        seed = 1 << i
        r.sendline(str(seed).encode())

    data = r.recvline().strip()
    if not data.startswith(b"Result: "):
        log.error("Output inatteso: " + data.decode())
        return

    list_str = data[len(b"Result: "):].strip().decode()
    try:
        results = literal_eval(list_str)
    except Exception as e:
        log.error("Errore nel parsing della lista: " + str(e))
        return

    flag_int = 0
    for num in results:
        flag_int |= num

    nbytes = (flag_int.bit_length() + 7) // 8
    flag_bytes = flag_int.to_bytes(nbytes, 'big')

    try:
        flag = flag_bytes.decode()
    except UnicodeDecodeError:
        flag = flag_bytes.hex()

    log.info("Flag ricostruita: " + flag)

    r.interactive()

if __name__ == '__main__':
    main()
