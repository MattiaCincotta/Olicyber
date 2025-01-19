import requests
from bs4 import BeautifulSoup

# URL della pagina web
url = 'http://web-15.challs.olicyber.it/'

# Esegui la richiesta GET per scaricare la pagina
response = requests.get(url)

# Verifica che la richiesta sia stata eseguita con successo
if response.status_code == 200:
    html_content = response.content
else:
    print("Errore nella richiesta della pagina:", response.status_code)
    exit()

# Analizzare il contenuto HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Trovare tutti i tag <link> e <script>
links = soup.find_all('link', href=True)
scripts = soup.find_all('script', src=True)

# Estrai gli URL delle risorse esterne
external_resources = []

# Aggiungi gli href dei tag <link>
for link in links:
    external_resources.append(link['href'])

# Aggiungi gli src dei tag <script>
for script in scripts:
    external_resources.append(script['src'])

flag = None

# Itera su ciascun URL delle risorse esterne e scarica il contenuto
for resource in external_resources:
    resource_url = url + resource
    resource_response = requests.get(resource_url)
    
    if resource_response.status_code == 200:
        resource_content = resource_response.text
        
        # Verifica se la flag è presente nel contenuto della risorsa
        if 'flag{' in resource_content:
            flag = resource_content
            break
    else:
        print(f"Errore nel download della risorsa: {resource}, Status Code: {resource_response.status_code}")

# Stampa la flag se trovata
if flag:
    print("Flag trovata:", flag)
else:
    print("Flag non trovata nelle risorse esterne.")
