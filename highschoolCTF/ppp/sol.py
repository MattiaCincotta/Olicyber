from Crypto.Cipher import DES3
from Crypto.Util.Padding import unpad

def isascii(char:str):
    return 32 <= ord(char) < 127

def decrypt(cipher: bytes, key: str):
    key = bytes.fromhex(key.removeprefix("0x"))
    if(len(key != 16)):
        return ''
    
    cipher = DES3.new(key, DES3.MODE_ECB)
    return cipher.decrypt(cipher.decrypt(ciphertext))
    
    

ciphertext = bytes.fromhex("44616d6d69206c6120666c6167212121")

for key in range(1 << 50):
    try:
        res = unpad(decrypt(ciphertext, hex(key)).decode())
    except:
        continue
    
    if all([isascii(char) for char in res]):
        print(res)