import requests
from bs4 import BeautifulSoup, Comment

# Scaricare la pagina web
url = 'http://web-14.challs.olicyber.it/'
response = requests.get(url)

# Controlla che la richiesta sia stata eseguita con successo
if response.status_code == 200:
    # Analizzare il contenuto HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # Trovare i commenti HTML
    comments = soup.find_all(string=lambda text: isinstance(text, Comment))

    # Estrarre e visualizzare i commenti
    for comment in comments:
        print(comment)
else:
    print("Errore nella richiesta della pagina:", response.status_code)
