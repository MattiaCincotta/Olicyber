import requests

# URL della risorsa
url = 'http://web-09.challs.olicyber.it/login'

# Dati da inviare in formato JSON
data = {
    'username': 'admin',
    'password': 'admin'
}

# Esegui una richiesta POST con i dati in formato JSON
response = requests.post(url, json=data)

# Stampa il testo della risposta
print(response.text)
