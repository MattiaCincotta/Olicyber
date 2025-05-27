
import string

def caesar_unshift_char(c, shift):
    if c in string.ascii_lowercase:
        alpha = string.ascii_lowercase
        return alpha[(alpha.index(c) - shift) % 26]
    elif c in string.ascii_uppercase:
        ALPHA = string.ascii_uppercase
        return ALPHA[(ALPHA.index(c) - shift) % 26]
    else:
        # numeri, parentesi, underscore, puntini, ecc. li lasci invariati
        return c

def decrypt_variable_caesar(ciphertext):
    """
    Decifra una stringa in cui il carattere in posizione i
    è stato cifrato con Caesar shift +i.
    """
    plaintext = []
    for i, ch in enumerate(ciphertext):
        plaintext.append(caesar_unshift_char(ch, i))
    return "".join(plaintext)

if __name__ == "__main__":
    encrypted = "fmcj{yo_ackyzb_ihruvcvjam}" 
    clear = decrypt_variable_caesar(encrypted)
    print("In chiaro:", clear)
