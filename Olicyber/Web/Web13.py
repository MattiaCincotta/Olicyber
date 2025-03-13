import requests
from bs4 import BeautifulSoup

# Step 1: Scaricare la pagina web
url = 'http://web-13.challs.olicyber.it/'
response = requests.get(url)

# Controlla che la richiesta sia stata eseguita con successo
if response.status_code == 200:
    # Step 2: Analizzare il contenuto HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # Step 3: Trovare le lettere evidenziate
    # Supponiamo che le lettere evidenziate siano in un tag specifico, ad esempio <span class="highlight">
    highlighted_letters = soup.find_all(class_='red')

    # Step 4: Estrarre e concatenare le lettere
    flag = ''.join([letter.get_text() for letter in highlighted_letters])

    # Step 5: Aggiungere il prefisso e il suffisso della flag
    flag = f"flag{{{flag}}}"
    
    print("Flag:", flag)
else:
    print("Errore nella richiesta della pagina:", response.status_code)
