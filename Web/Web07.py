import requests

# URL della risorsa
url = 'http://web-07.challs.olicyber.it/'

# Esegui una richiesta HEAD
response = requests.head(url)

# Stampa gli header restituiti
print("Headers:")
for header, value in response.headers.items():
    print(f"{header}: {value}")
