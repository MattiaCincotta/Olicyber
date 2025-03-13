import requests

# Crea una sessione
session = requests.Session()

# URL della risorsa di login
login_url = 'http://web-11.challs.olicyber.it/login'

# Dati da inviare in formato JSON
login_data = {
    'username': 'admin',
    'password': 'admin'
}

# Esegui una richiesta POST con i dati in formato JSON
login_response = session.post(login_url, json=login_data)

# Verifica lo status della risposta
if login_response.status_code == 200:   #se la risposta è 200 è andata a buon fine
    # Decodifica il corpo della risposta JSON
    login_response_json = login_response.json() #converte da formato json a dizionario di python
    csrf_token = login_response_json.get('csrf')    #prende il valore con la chiave corrispondente chiamata csrf

    # Verifica se il token CSRF è stato ottenuto
    if csrf_token:
        flag_pieces = []
        # URL della risorsa dei pezzi della flag
        flag_piece_url = 'http://web-11.challs.olicyber.it/flag_piece'

        # Ottieni i 4 pezzi della flag
        for index in range(4):
            # Esegui una richiesta GET con il token CSRF e il parametro index
            flag_piece_response = session.get(flag_piece_url, params={'index': index, 'csrf': csrf_token})

            # Verifica lo status della risposta
            if flag_piece_response.status_code == 200:  #se la risposta è 200 è andata a buon fine
                # Decodifica la risposta JSON
                flag_piece_json = flag_piece_response.json()
                # Aggiungi il pezzo della flag alla lista
                flag_pieces.append(flag_piece_json['flag_piece'])
                
                # Aggiorna il token CSRF per la prossima richiesta
                csrf_token = flag_piece_json.get('csrf')
            else:
                print(f"Errore nella richiesta del pezzo {index}: {flag_piece_response.status_code}")
                break

        # Stampa la flag completa
        if len(flag_pieces) == 4:
            flag = ''.join(flag_pieces)
            print(f"Flag completa: {flag}")
        else:
            print("Non è stato possibile ottenere tutti i pezzi della flag.")
    else:
        print("Token CSRF non trovato nella risposta di login.")
else:
    print(f"Errore nella richiesta di login: {login_response.status_code}")
