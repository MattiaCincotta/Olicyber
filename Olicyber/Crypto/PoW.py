from pwn import remote
import hashlib

cached_hashes = {}

def incremental_hex_string(length, start=0):
    hex_value = hex(start)[2:].zfill(length)
    return hex_value[-length:]

for i in range(10**9):
    x = incremental_hex_string(64, start=i)
    sha256_hash = hashlib.sha256(bytes.fromhex(x)).hexdigest()

    cached_hashes[sha256_hash[:6]] = x

conn = remote('pow.challs.olicyber.it', 12209)

challenge = conn.recvline().decode()
print("String: ", challenge)


def find_x_with_prefix(prefix):
    
    if cached_hashes.get(prefix) is not None:
        print('prova')
        return cached_hashes.get(prefix)
        
    return None

while True:
    
        prefix = challenge.split()[-1]

        x = find_x_with_prefix(prefix)

        if x:
            print(f"Trovato x: {x}")
            conn.sendline(x.encode('utf-8'))
        else:
            print("Nessun valore trovato.")
            break

        response = conn.recvline().decode()
        print("Risposta dal server:", response)
        challenge = response

conn.close()

