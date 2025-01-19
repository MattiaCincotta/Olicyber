from pwn import xor

# Dati cifrati in formato esadecimale
enc_flag = bytes.fromhex("27893459dc8772d66261ff8633ba1e5097c10fba257293872fd2664690e975d2015fc4fd3c")

# Calcolare la chiave parziale basata su una stringa conosciuta
known_prefix = b"flag{"
key_length = len(known_prefix)
key = bytearray(xor(known_prefix, enc_flag[:key_length]))
print(f"Initial Key Length: {len(key)}")

# Brute-force sui possibili valori dei byte successivi della chiave
for i in range(256):
    key.append(i)  # Aggiungi un byte alla fine della chiave
    decrypted_data = xor(enc_flag, key)  # Decifra i dati cifrati
    print(f"Attempted Key: {key}")
    print(f"Decrypted Data: {decrypted_data}")
    key.pop()  # Rimuovi l'ultimo byte per il prossimo tentativo
