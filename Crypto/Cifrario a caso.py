import random

out = '088596df93697e62d71cb143352ccb45be15463219c6cc917f9be83c1aa1f7d0217b4586c1058009'


def decrypt_flag(out_hex):
    out = bytes.fromhex(out_hex)
    
    for key in range(256):  
        random.seed(key)
        decrypted = bytearray()
        
        for c in out:
            decrypted.append(c ^ random.randint(0, 255))
        
        try:
            text = decrypted.decode()
            if "flag{" in text:  
                return text
        except UnicodeDecodeError:
            continue  # Se la decodifica fallisce, passa alla prossima chiave
    
    return "Flag non trovata"

out = decrypt_flag(out)


print(out)