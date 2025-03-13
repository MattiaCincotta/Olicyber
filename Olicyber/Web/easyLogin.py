import requests

# URL della richiesta
url = 'http://easylogin.challs.olicyber.it/flag'

# Imposta il cookie
cookies = {
    'session': 'd6f816cd031715f733539affe057b5103530c23ff9aa01c5c4e71990ac2ae2ac'
}

# Esegui la richiesta GET
response = requests.get(url, cookies=cookies)

# Stampa il contenuto della risposta
print(response.text)
