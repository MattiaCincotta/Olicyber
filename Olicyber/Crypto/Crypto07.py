from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os
print('hex_key: ')
hexkey = input()
# Dati forniti
key = bytes.fromhex(hexkey)
plaintext = 'La lunghezza di questa frase non è divisibile per 8'
mode = DES.MODE_CBC
iv = b'\x00' * 8  # IV di default (inizializzato a zero, non specificato nel problema)

# Crea il cifrario DES in modalità CBC
cipher = DES.new(key, mode, iv)

# Applica il padding X.923
# Nota: in X.923, il padding aggiunge byte di valore 0 eccetto l'ultimo byte, che indica il numero di byte di padding aggiunti
padded_plaintext = pad(plaintext.encode('utf-8'), DES.block_size, style='x923')

# Cifra il testo
ciphertext = cipher.encrypt(padded_plaintext)

# Ottieni il risultato in esadecimale
ciphertext_hex = ciphertext.hex()
print("Testo cifrato (esadecimale):", ciphertext_hex, "iv:", iv)




# Dati forniti
print('hex_key:')
key_hex = input()
key = bytes.fromhex(key_hex)
plaintext = 'Mi chiedo cosa significhi il numero nel nome di questo algoritmo.'
block_size = 16
segment_size = 24

# Genera un IV casuale
iv = os.urandom(block_size)  # 16 byte per AES

# Crea il cifrario AES256 in modalità CFB con dimensione segmento specifica
cipher = AES.new(key, AES.MODE_CFB, iv=iv, segment_size=segment_size)

# Applica il padding PKCS7 al plaintext
padded_plaintext = pad(plaintext.encode('utf-8'), block_size, style='pkcs7')

# Cifra il testo
ciphertext = cipher.encrypt(padded_plaintext)

# Risultati
print("IV (esadecimale):", iv.hex())
print("Ciphertext (esadecimale):", ciphertext.hex())

from Crypto.Cipher import ChaCha20

# Dati forniti
key_hex = '8a82fd75c0e43861ef6061eddd1ac0d82c254f15b09ab716951f61b2af255899'
ciphertext_hex = '7c41f3311bd8fd34678343f9007118b7c9755a807cc82caf0854a43f'
nonce_hex = '000e0363edc1b917'

# Conversione in byte
key = bytes.fromhex(key_hex)
ciphertext = bytes.fromhex(ciphertext_hex)
nonce = bytes.fromhex(nonce_hex)

# Creazione del cifrario ChaCha20
cipher = ChaCha20.new(key=key, nonce=nonce)

# Decifrazione
plaintext = cipher.decrypt(ciphertext)

# Risultato
print("Testo in chiaro (ASCII):", plaintext.decode('ascii'))
