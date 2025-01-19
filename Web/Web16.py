import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# URL della pagina iniziale
base_url = 'http://web-16.challs.olicyber.it/'

# Set per mantenere traccia delle pagine visitate
visited_pages = set()

# Lista per le pagine da visitare
pages_to_visit = [base_url]

flag = None

# Funzione per scaricare e analizzare una pagina
def visit_page(url):
    global flag
    # Effettua una richiesta GET per scaricare la pagina
    response = requests.get(url)
    
    # Verifica che la richiesta sia stata eseguita con successo
    if response.status_code == 200:
        html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Cerca il tag <h1> per trovare la flag
        h1_tag = soup.find('h1')                #cerca il tag h1 nella pagina
        if h1_tag and 'flag{' in h1_tag.text:   #Controlla se il tag <h1> esiste e se il testo all'interno di questo tag contiene la stringa 'flag{
            flag = h1_tag.text                  #in caso positivo ritorno la flag
            return
        
        # Trova tutti i tag <a> e aggiunge i link relativi alle pagine da visitare
        for link in soup.find_all('a', href=True):  #cerca i tag <a> che contengono un href
            full_url = urljoin(url, link['href'])   #costruisco l'url della pagina
            if full_url not in visited_pages:       #controlla se l'url non è già presente nelle pagine visitate
                pages_to_visit.append(full_url)     #in caso lo aggiunge
    else:
        print(f"Errore nella richiesta della pagina: {url}, Status Code: {response.status_code}")   #errore nella richiesta get

# Loop per visitare tutte le pagine
while pages_to_visit and not flag:  #fnchè ci sono pagine da visitare e la flag non è stata trovata continuo
    current_page = pages_to_visit.pop(0)    #prendo la pagina da visitare
    if current_page not in visited_pages:   #se la pagina da visitare bon è stata visitata entro
        visited_pages.add(current_page)     #aggiungo la pagina alle pagine visitate
        visit_page(current_page)            #chiamo la funzione visit_page

# Stampa la flag se trovata
if flag:
    print("Flag trovata:", flag)
else:
    print("Flag non trovata nella rete di pagine.")
