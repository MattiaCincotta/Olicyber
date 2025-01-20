from pwn import remote

conn = remote('chooseyourotp.challs.olicyber.it', 38302)
conn.recvline()
conn.recvline()

def get_ciphertext(n):
    conn.sendline(f"{n}")
    response = conn.recvline().decode().strip() 
    response = response
    return int(response)  

target_chars = ['f', 'l', 'a', 'g', '{']
flag = ""

for char in target_chars:
    for n in range(2, 100):   
        ciphertext = get_ciphertext(n)
        
        for r in range(256):
            decrypted = chr(ciphertext ^ r)
            if decrypted == char:
                flag += char
                print(f"Carattere trovato: {char} per n={n} e r={r}")
                break
        if flag and flag[-1] == char:
            break

print(f"Flag parziale: {flag}")

conn.close()
