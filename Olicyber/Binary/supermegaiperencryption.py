#Obiettivo: costruire il codice reversato partendo dalla funzione v3 e andando avanti fino alla funzione v1, challenge fornisce l'input iniziale 

def lvl1(input_flag):   # entra una stringa di caratteri e secondo le condizioni che seguono vengono aumentati i valori ascii
    flag = []
    
    for char in input_flag:
        v3 = ord(char) 
         
        if v3 > 99:
            v4 = v3 - 100  
        else:
            v4 = v3 + 20 
            
        flag.append(chr(v4))  
    return ''.join(flag)

def lvl2(input_flag):   #entra la stringa di numeri ruotata ed esce il corrispettivo in caratteri ascii
    flag = ""
    i = 0

    while i < len(input_flag):
        length = int(input_flag[i])  
        i += 1  
        ascii_value = int(input_flag[i:i+length])  
        i += length  
        flag += chr(ascii_value)  
    return flag
        
    
def lvl3(encrypted_flag, v4):   #entra una stringa di numeri che viene ruotata
    decrypted_part = encrypted_flag[:v4][::-1] 
    rest = encrypted_flag[v4:]  
    
    return decrypted_part + rest  

    
def decryptData(input_flag):
    flag = lvl3(input_flag, len(input_flag))
    print(f'lv3: {flag}')
    
    flag = lvl2(flag)
    print(f'lv2: {flag}')
    
    flag = lvl1(flag)
    print(f'lv1: {flag}')

def main():
    input_flag = '6423522322238023102381231023652522102341238229023572002300237725721123462522002313213201235725725729023752902340233223302377280232023'
    decryptData(input_flag)

if __name__ == "__main__":
    main()