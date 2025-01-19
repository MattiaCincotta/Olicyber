from sympy.ntheory import discrete_log
print(discrete_log(97, 24, 5))

# Parametri pubblici
p = 137
g = 2

# La tua chiave segreta (scegli un valore segreto a caso)
b = 19  # ad esempio

# Calcolo della chiave pubblica B
B = pow(g, b, p)
print(f"La tua chiave pubblica è: {B}")

# Parametri
p = 137
g = 2

# Funzione per trovare il logaritmo discreto
def discrete_log(g, h, p):
    for x in range(p):
        if pow(g, x, p) == h:
            return x
    return None

# Trova la tua chiave segreta (a) dato g^a mod p = 19
a = discrete_log(g, 19, p)

# Trova la mia chiave segreta (b) dato g^b mod p = 126
b = discrete_log(g, 126, p)

# Calcola il segreto condiviso
shared_secret_1 = pow(126, a, p)  # Usando la tua chiave pubblica
shared_secret_2 = pow(19, b, p)   # Usando la mia chiave pubblica

print(f"La tua chiave segreta (a) è: {a}")
print(f"La mia chiave segreta (b) è: {b}")
print(f"Il segreto condiviso calcolato da te è: {shared_secret_1}")
print(f"Il segreto condiviso calcolato da me è: {shared_secret_2}")
