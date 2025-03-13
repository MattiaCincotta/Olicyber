import requests
from bs4 import BeautifulSoup

# Step 1: Scaricare la pagina web
url = 'http://web-12.challs.olicyber.it/'
response = requests.get(url)

# Controlla che la richiesta sia stata eseguita con successo
if response.status_code == 200:
    # Step 2: Analizzare il contenuto HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # Step 3: Trovare tutti i paragrafi nella pagina
    paragraphs = soup.find_all('p')

    # Step 4: Estrarre il secondo paragrafo e ottenere il testo
    if len(paragraphs) > 1:
        second_paragraph = paragraphs[1].get_text()
        print("Secondo paragrafo:", second_paragraph)
    else:
        print("Non ci sono abbastanza paragrafi nella pagina.")
else:
    print("Errore nella richiesta della pagina:", response.status_code)
