from math import gcd

p = 19
q = 5

e = 65537

n = p*q
print(f'n:  {n}')

phi = (p-1)*(q-1)
print(f'phi: {phi}')

c = 12**e % n 
d = pow(e, -1, phi)

m = c**d % n
print(f'm: {m}')


# Dati
p = 61
q = 53
phi_n = (p - 1) * (q - 1)

# Trova un e valido
def find_e(phi_n):
    for e in range(2, phi_n):
        if gcd(e, phi_n) == 1:
            return e

e = find_e(phi_n)
print(f"e = {e}")


# Dati
m = 12  # base
e = 7   # esponente

# Calcolo con esponenziazione modulare
c = pow(m, e, n)
print(f"c = {c}")

d = pow(e, -1, phi)
print(f'd: {d}')