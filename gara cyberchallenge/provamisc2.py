'''from typing import List, Tuple

def ricomponi_video(pezzi: List[Tuple[int, bytes]], output_file: str):
    """
    Ricostruisce il video a partire da pezzi parziali.
    
    :param pezzi: lista di tuple (offset, dati_bytes)
                  offset = indice di partenza nel file video
                  dati_bytes = chunk binario
    :param output_file: nome del file video finale da creare
    """

    # Ordino i pezzi in base all'offset
    pezzi_ordinati = sorted(pezzi, key=lambda x: x[0])

    # Trovo la dimensione totale massima in base all'ultimo pezzo
    ultima_posizione = pezzi_ordinati[-1][0] + len(pezzi_ordinati[-1][1])

    # Preparo un bytearray vuoto della dimensione totale
    video_completo = bytearray(ultima_posizione)

    # Inserisco i dati nei posti giusti
    for offset, dati in pezzi_ordinati:
        video_completo[offset:offset+len(dati)] = dati

    # Salvo su file
    with open(output_file, 'wb') as f:
        f.write(video_completo)

    print(f"Video ricostruito e salvato in '{output_file}'")

# --- Esempio d'uso ---

# Supponiamo che tu abbia estratto questi pezzi:
# (offset_inizio, dati_binari_del_pezzo)
pezzi_estratti = [
    (0, b'\x00\x00\x00...'),          # Primo pezzo (esempio)
    (10000, b'\x12\x34\x56...'),      # Secondo pezzo
    (20000, b'\xAB\xCD\xEF...'),      # Terzo pezzo
    # ... altri pezzi
]

# Chiamiamo la funzione con questi dati
ricomponi_video(pezzi_estratti, 'video_ricostruito.mp4')
'''
import pyshark
import os

def salva_pezzi_video(pcap_file, output_dir):
    cap = pyshark.FileCapture(pcap_file, display_filter='http.response.code == 206')

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    contatore = 0
    for pkt in cap:
        try:
            if hasattr(pkt, 'http') and hasattr(pkt.http, 'file_data'):
                data_hex = pkt.http.file_data.replace(':', '')
                dati = bytes.fromhex(data_hex)

                # Salva con indice progressivo
                filepath = os.path.join(output_dir, f"pezzo_{contatore:04d}.bin")
                with open(filepath, 'wb') as f:
                    f.write(dati)
                print(f"[+] Salvato: {filepath}")
                contatore += 1
        except Exception as e:
            print(f"[!] Errore nel pacchetto: {e}")

    cap.close()

if __name__ == "__main__":
    pcap_path = "/home/mattia/Downloads/vgallery.pcap"
    output_dir = "/home/mattia/Videos/pezzi_video"
    salva_pezzi_video(pcap_path, output_dir)

