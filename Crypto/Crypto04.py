m1 = '158bbd7ca876c60530ee0e0bb2de20ef8af95bc60bdf'
m2 = '73e7dc1bd30ef6576f883e79edaa48dcd58e6aa82aa2'

def xor(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])

# Convertiamo le stringhe esadecimali in byte
m1_bytes = bytes.fromhex(m1)
m2_bytes = bytes.fromhex(m2)

# Applichiamo la funzione xor
result = xor(m1_bytes, m2_bytes)

# Stampiamo il risultato come stringa esadecimale
print(result)
