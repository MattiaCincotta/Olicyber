import requests

# URL della risorsa
url = 'http://web-08.challs.olicyber.it/login'

# Dati da inviare nel formato application/x-www-form-urlencoded
data = {
    'username': 'admin',
    'password': 'admin'
}

# Esegui una richiesta POST
response = requests.post(url, data=data)

# Stampa il testo della risposta
print(response.text)
