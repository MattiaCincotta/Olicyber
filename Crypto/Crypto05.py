ciphertext = "104e137f425954137f74107f525511457f5468134d7f146c4c"

def xor_single_byte(ciphertext_bytes, key):
    return bytes([b ^ key for b in ciphertext_bytes])

ciphertext_bytes = bytes.fromhex(ciphertext)

for key in range(256):
    plaintext = xor_single_byte(ciphertext_bytes, key)
    try:
        plaintext_str = plaintext.decode('ascii')
        if plaintext_str.isprintable():
            print(f"Key: {key:02x} => Plaintext: {plaintext_str}")
    except UnicodeDecodeError:
        continue

