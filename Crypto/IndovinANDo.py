from pwn import remote


conn = remote('segreto.challs.olicyber.it', 33000)


def reconstruct_secret(conn):
    secret = [0] * 8  # Array per memorizzare i byte del segreto

    # Invia una serie di maschere e combina i risultati per dedurre il segreto
    for mask in range(1, 16):  # Partiamo da 1 per evitare la maschera tutta zero
        conn.sendline(str(mask).encode())  # Invia la maschera al server
        response = conn.recvline().strip().decode()  # Ottieni la risposta dal server
        
        if response.startswith('>'):
            response = response[1:]
        
        print(f'mask: {mask}, response: {response}')

        try:
            partial = bytes.fromhex(response)  # Converte la risposta in un array di byte
        except ValueError:
            print(f"Formato non valido per mask={mask}: {response}")
            continue

        # Combina i risultati per dedurre il segreto
        for j in range(8):  # Per ogni byte della risposta
            secret[j] |= partial[j]  # Aggiorna il byte combinando i bit

    return bytes(secret)  # Converte l'array in bytes


# Leggi messaggi iniziali
print(conn.recvline().decode())
print(conn.recvline().decode())
print(conn.recvline().decode())

# Ciclo per i 10 round
for i in range(10):
    print(f"Round {i + 1} di 10")

    # Ricostruisci il segreto
    secret = reconstruct_secret(conn)

    # Fase di guess
    conn.sendline(b"g")  # Comando per iniziare il guess
    conn.sendline(secret.hex().encode())  # Invia il segreto in formato esadecimale

    # Leggi la risposta del server
    response = conn.recvline().decode().strip()
    print(f"Secret ricostruito: {secret.hex()}")
    print(f"Risposta server: {response}")

    # Verifica successo o fallimento
    if "errato" in response.lower():
        print("Guess fallito. Esci.")
        conn.close()
        exit(1)

# Chiudi la connessione
conn.close()
