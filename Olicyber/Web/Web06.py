import requests

# Crea una sessione
session = requests.Session()

# Esegui la prima richiesta per ottenere il cookie di sessione
token_url = 'http://web-06.challs.olicyber.it/token'
response = session.get(token_url)

# Stampa i cookie ricevuti per conferma (opzionale)
print("Cookies ricevuti:", session.cookies)

# Esegui la seconda richiesta usando la stessa sessione
flag_url = 'http://web-06.challs.olicyber.it/flag'
response = session.get(flag_url)

# Stampa il contenuto della risposta per vedere la flag
print("Risposta:", response.text)
