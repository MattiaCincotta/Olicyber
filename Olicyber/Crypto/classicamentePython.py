def decrypt(flag, n):
    
    #calcola il numero di righe
    num_rows = len(flag) // n
    
    # Crea una lista vuota di righe
    grid = ['' for _ in range(num_rows)]
    
    # Riempie la griglia con i caratteri
    for i in range(num_rows):   #numero di righe
        for j in range(n):      #numero di colonne
            grid[i] += flag[j * num_rows + i]
    
    # Combina le righe per ottenere la stringa originale
    decrypted_data = ''.join(grid)  # ==> concatena più stringhe in una sola
    
    # Rimuove il padding se presente
    decrypted_data = decrypted_data.rstrip('_') #.rstrip() ==> rimuove il carattere specificato alla fine
    
    return decrypted_data

def encrypt(data):  #data = flag
    n = 4           #numero colonne griglia
    
    # Aggiungi padding per fare in modo che la lunghezza dei dati sia un multiplo di n (len(flag) = 48 che è multiplo di 4)
    data += "_"*(n - (len(data) % n))
    
    cols = [data[i::n] for i in range(n)]
    return "".join(cols)

# Test di cifratura e decifratura
flag = "f{anuiraaso_lfltnfi_sin_aime_rotpze_gne_ca_roi}_"


flag = decrypt(flag, 4)
print("Decrypted:", flag)
