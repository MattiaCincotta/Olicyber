from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
import binascii

# Parametri forniti
key = bytes.fromhex('a5de64934abb2cf0')
plaintext = 'La lunghezza di questa frase non è divisibile per 8'

# Padding x923
def pad_x923(data, block_size):
    padding_len = block_size - (len(data) % block_size)
    padding = bytes([0] * (padding_len - 1) + [padding_len])
    return data + padding

# Cifra il testo
def encrypt_des_cbc(key, plaintext):
    cipher = DES.new(key, DES.MODE_CBC)
    padded_text = pad_x923(plaintext.encode(), DES.block_size)
    ciphertext = cipher.encrypt(padded_text)
    return cipher.iv, ciphertext

# Ottieni l'IV e il testo cifrato
iv, ciphertext = encrypt_des_cbc(key, plaintext)

# Converti IV e testo cifrato in esadecimale
iv_hex = binascii.hexlify(iv).decode()
ciphertext_hex = binascii.hexlify(ciphertext).decode()

# Stampa i risultati
print(f"Testo cifrato in esadecimale: {iv_hex}{ciphertext_hex}")
print(f"IV (in esadecimale): {iv_hex}")
print(f"Testo cifrato (in esadecimale): {ciphertext_hex}")
