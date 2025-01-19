import requests

# URL della risorsa
url = 'http://web-10.challs.olicyber.it/'

# Esegui una richiesta OPTIONS per determinare i verbi supportati
options_response = requests.options(url)

# Stampa gli header della risposta per vedere i verbi supportati
print("Header della risposta OPTIONS:")
print(options_response.headers)

# Estrarre l'elenco dei verbi supportati dallo header Allow
allowed_methods = options_response.headers.get('Allow', '')
print("\nVerbi HTTP supportati:", allowed_methods)

# Prova a utilizzare un verbo poco comune, ad esempio PATCH
patch_response = requests.post(url)

# Stampa lo stato e il contenuto della risposta alla richiesta PATCH
print("\nRisposta alla richiesta PATCH:")
print("Status Code:", patch_response.status_code)
print("Response Text:", patch_response.text)

# Esegui una richiesta patch
response = requests.patch(url)

# Stampa gli header restituiti
print("Headers:")
for header, value in response.headers.items():
    print(f"{header}: {value}")
