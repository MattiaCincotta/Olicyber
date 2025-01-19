import requests

# URL della risorsa che desideri ottenere
url = 'http://web-05.challs.olicyber.it/flag'

# Specifica i cookie da inviare
cookies = {
    'password': 'admin'
}

# Invia la richiesta GET con i cookie
response = requests.get(url, cookies=cookies)   #qui il primo cookies è il parametro dei cookies

# Stampa il contenuto della risposta
print(response.text)
