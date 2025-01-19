from sympy import isprime, nextprime
from random import getrandbits
from sympy.ntheory import primitive_root

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

from Crypto.Util.number import getPrime, isPrime

from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.hashes import SHA256
import os

# Generate a 1024-bit prime number and generator
parameters = dh.generate_parameters(generator=2, key_size=1024)

# Extract prime and generator
p = parameters.parameter_numbers().p
g = 5

print(f"Prime (p): {p}")
print(f"Generator (g): {g}")

import random
# Genera una chiave privata casuale
private_key = random.randint(2, p - 2)

# Calcola la chiave pubblica
public_key = pow(g, private_key, p)  # g^a % p

print(f"Chiave privata (a): {private_key}")
print(f"Chiave pubblica (A): {public_key}")

B = int(input('chiave pubblica B: '), 16)

S = pow(B, private_key, p)
print(f'Segreto condiviso: {hex(S)}')