from pwn import remote

# Connessione al server
conn = remote('chooseyourotp.challs.olicyber.it', 38302)

# Funzione per inviare un numero e ricevere la risposta
def get_otp_response(n):
    conn.sendline(str(n).encode())  # Invia il numero come byte
    response = conn.recvline().decode().strip()  # Leggi la risposta e rimuovi eventuali spazi
    response = response.lstrip('>')  # Rimuove il simbolo '>' all'inizio della risposta
    print(f"Risposta per {n}: {response}")
    
    # Assicurati che la risposta sia un numero esadecimale valido
    try:
        return int(response, 16)  # Converte la risposta in intero esadecimale
    except ValueError:
        print(f"Errore: la risposta '{response}' non è un numero esadecimale valido.")
        return None

# Funzione per ottenere la flag bit per bit
def leak_flag_bits():
    # I primi 5 caratteri della flag che sappiamo sono: "flag{"
    flag = ['f', 'l', 'a', 'g', '{']
    flag_bytes = [ord(c) for c in flag]  # Converti i caratteri iniziali della flag in byte

    leaked_bits = []

    # Estrai i bit dei caratteri "flag{" (primi 5 caratteri)
    for i, byte in enumerate(flag_bytes):
        print(f"Esplorando il byte per il carattere {chr(byte)}: {byte:#x}")
        
        # Prova a ottenere la risposta per ogni numero (fino a 19 come da esempio precedente)
        for n in range(1, 20):
            otp_response = get_otp_response(n)
            if otp_response is not None:
                # Estrai il bit i-esimo della risposta
                bit = otp_response & (1 << i)
                leaked_bits.append(bit)
                print(f"Bit leakato per il byte {chr(byte)}: {bit}")

    # Verifica che il numero totale di bit sia un multiplo di 8, altrimenti completa
    if len(leaked_bits) % 8 != 0:
        # Aggiungi i bit di padding per completare l'ultimo byte (aggiungi 0 se necessario)
        padding_bits = 8 - (len(leaked_bits) % 8)
        leaked_bits.extend([0] * padding_bits)
        print(f"Aggiunti {padding_bits} bit di padding.")

    # Ricostruisci la flag
    reconstructed_flag = reconstruct_flag_from_bits(leaked_bits)

    return reconstructed_flag

# Funzione per ricostruire la flag dai bit
def reconstruct_flag_from_bits(leaked_bits):
    flag_bytes = []
    # Raggruppa i bit in byte (8 bit per byte)
    for i in range(0, len(leaked_bits), 8):
        byte = 0
        for j in range(8):
            byte |= leaked_bits[i + j] << j  # Aggiungi ogni bit al byte
        flag_bytes.append(byte)

    # Converte i byte in caratteri
    reconstructed_flag = ''.join(chr(b) for b in flag_bytes)
    return reconstructed_flag

# Chiama la funzione per leakare e ricostruire la flag
reconstructed_flag = leak_flag_bits()

# Stampa la flag ricostruita
print("Flag ottenuta:", reconstructed_flag)

# Chiudi la connessione
conn.close()
