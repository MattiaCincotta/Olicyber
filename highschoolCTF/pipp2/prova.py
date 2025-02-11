def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    key_index = 0  # conta solo i caratteri alfabetici
    for char in ciphertext:
        if char.isalpha():
            # assumiamo minuscolo
            c_val = ord(char) - ord('a')
            k_val = ord(key[key_index % len(key)]) - ord('a')
            # Decriptazione: sottraiamo il valore della chiave
            p_val = (c_val - k_val) % 26
            plaintext += chr(p_val + ord('a'))
            key_index += 1
        else:
            # lasciamo invariati spazi, underscore, parentesi, ecc.
            plaintext += char
    return plaintext

# Il testo cifrato:
ciphertext = "yrof{dmmnv_dpa_wkt_wgxtfqe}"

# Sappiamo che le prime 4 lettere (yrof) devono diventare "flag".
# Calcoliamo la chiave dai primi 4 caratteri:
plaintext_known = "flag"
key = ""
for i in range(4):
    c_val = ord(ciphertext[i]) - ord('a')
    p_val = ord(plaintext_known[i]) - ord('a')
    k_val = (c_val - p_val) % 26
    key += chr(k_val + ord('a'))

print("Chiave derivata:", key)
print("Flag decriptato:", vigenere_decrypt(ciphertext, key))
