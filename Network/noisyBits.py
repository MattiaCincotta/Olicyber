from PIL import Image
import numpy as np
import zipfile
import os

def image_to_zip(image_path, output_zip_path):
    # Apri l'immagine e convertila in bianco e nero
    img = Image.open(image_path).convert('1')
    data = np.array(img)
    
    # Converti i dati dell'immagine in una stringa di bit
    binary_data = ''.join(['1' if bit else '0' for bit in data.flatten()])
    
    # Converti la stringa di bit in byte
    byte_data = int(binary_data, 2).to_bytes((len(binary_data) + 7) // 8, byteorder='big')
    
    # Scrivi i byte in un file ZIP
    with zipfile.ZipFile(output_zip_path, 'w') as zipf:
        # Aggiungi un file fittizio dentro il file ZIP
        zipf.writestr('data.bin', byte_data)

# Specifica i percorsi
image_path = '/home/mattia/Downloads/bits.bmp'  # Cambia questo con il percorso corretto dell'immagine se necessario
output_zip_path = '/home/mattia/Downloads/output.zip'  # Cambia questo con il percorso corretto per il file ZIP

image_to_zip(image_path, output_zip_path)
print(f"File ZIP creato con successo: {output_zip_path}")
