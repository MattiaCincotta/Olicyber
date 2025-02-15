from pwn import *

def main():

    conn = remote('ihc.challs.olicyber.it', 34008)
    
    conn.recvuntil('premi invio!')
    conn.sendline('')
    res = ''
    pos = ''
    pos_list = ''
    flag= ''
    
    while(True):
        response = conn.recvline().decode()[:-1].split(' ')
        
        lettera = response[5]


        if 'Quante' in response:            
            stringa = response[8][:-1]
                        
            res = stringa.count(lettera)
            
        elif 'Restituiscimi' in response:
            res = lettera[::-1]
            
        elif 'Qual' in response:
            try:
                a = int(lettera)
            except:
                pass
            op = response[6]
            try:
                b = int(response[7][:-1])
            except:
                pass    
            if op == '-':
                res = a - b
                
            elif op == '+':
                res = a + b
                
            elif op == '*':
                res = a * b
                
            else:
                a = int(response[6])
                b = int(response[8][:-1])
                res = a // b
                
        elif 'Quali' in response:
            i = 6
            while True:
                if response[i] == 'nella': 
                    break
                pos+= response[i]  
                i += 1

            pos_string = " ".join(pos_list).replace('[', '').replace(']', '')

            
            pos_list = [int(num.replace(',', '')) for num in pos_string.split()]

            stringa = response[-1][:-1]

            for i in pos_list:
                res += stringa[i]
                
        conn.sendline(str(res).encode())
        response = conn.recvline()
        flag += response.decode()
        print(flag)
        
        
        
if __name__ == "__main__":
    main()