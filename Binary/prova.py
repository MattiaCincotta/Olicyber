#a1: array utilizzato come destinazione per i dati alternati.
#a2: array da cui prendere i caratteri da alternare.
#a3: array da cui prendere i caratteri da alternare insieme a quelli di a2.
#a4: la lunghezza dei segmenti da alternare. Indica quante volte si volgiono alternare i caratteri tra a2 e a3.

'''
Cosa fa la funzione pair_strings: Per ogni ciclo del while, prima viene preso un carattere da a2 e poi uno da a3, 
questi vengono copiati in a1 finché non sono stati alternati un totale di a4 caratteri.
'''

def pair_strings(a1, a2, a3, a4):
    i, j, k = 0, 0, 0
    
    while k < a4:
        if i < a4:
            a1[k] = a2[i]
            i += 1
            k += 1
        if j < a4:
            a1[k] = a3[j]
            j += 1
            k += 1
    return a1

'''a2 = list("abcdefgh")  
a3 = list("12345678")  
a4 = 8  
a1 = [''] * 16  # array vuoto di 16 elementi
result = pair_strings(a1, a2, a3, a4)
print(''.join(result))  '''


def make_serial(user_id):
    a2 = [''] * 48  
    a1 = list(user_id)  

    print(f"a1: {a1}")  # Stampa a1 prima della chiamata    ==> Giusto
    
    provaA = pair_strings(a2, a1[18:], a1[9:18], 8)  # Copia 8 byte da a1[18:] e a1[9:18] in a2
    print(f'prova A: {provaA}')
    
    provaB = pair_strings(a2[16:], a1[:9], a1[18:], 8)  # Copia 8 byte da a1[:9] e a1[18:] in a2[16:]
    print(f'prova B: {provaB}')
    provaC = pair_strings(a2[32:], a1[9:], a1[:9], 8)  # Copia 8 byte da a1[9:] e a1[:9] in a2[32:]
    print(f'Prova C: {provaC}')
    
    print(''.join(provaA) + ''.join(provaB) + ''.join(provaC))
    
    return ''.join(a2)  #ritorna come str


user_id = "z96uhBfh-yxMToeev-t1kMab4R"  # User ID
key = make_serial(user_id)
print("Chiave:", key)
