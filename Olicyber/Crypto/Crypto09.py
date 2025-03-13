def extended_gcd(a, b):
    # Caso base
    if b == 0:
        return a, 1, 0  # GCD, x, y
    # Ricorsione
    gcd, x1, y1 = extended_gcd(b, a % b)
    # Calcola x e y
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

# Esempio con a = 112, b = 137
a = 158
b = 99
gcd, x, y = extended_gcd(a, b)

print(f"GCD({a}, {b}) = {gcd}")
print(f"x = {x}, y = {y}")
print(f"Verifica: {a} * {x} + {b} * {y} = {gcd}")
