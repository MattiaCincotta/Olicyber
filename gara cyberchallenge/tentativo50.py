import pyshark
import os
import re

PCAP_FILE = '/home/mattia/Downloads/vgallery.pcap'  # <-- cambia se serve
OUTPUT_DIR = "/home/mattia/Videos/video_finale.mp4"
FINAL_FILE = '/home/mattia/Videos/video_ricostruito.mp4'

os.makedirs(OUTPUT_DIR, exist_ok=True)

cap = pyshark.FileCapture(PCAP_FILE, display_filter='mp4')

count = 0
for pkt in cap:
    try:
        # pyshark identifica mp4 e il payload si trova in mp4.box
        if hasattr(pkt, 'mp4') and hasattr(pkt.mp4, 'box'):
            data_hex = pkt.mp4.box.replace(':', '')
            data = bytes.fromhex(data_hex)
            filename = f'packet_{count:02d}.bin'
            with open(os.path.join(OUTPUT_DIR, filename), 'wb') as f:
                f.write(data)
            print(f'Salvato pacchetto {count} in {filename}')
            count += 1
    except Exception as e:
        print(f'Errore: {e}')

cap.close()

