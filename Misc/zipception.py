import zipfile
import os

def extract_zip(zip_path, extract_to):
    """
    Estrae un file ZIP.

    :param zip_path: Percorso del file ZIP.
    :param extract_to: Directory di destinazione per l'estrazione.
    """
    # Verifica se il file ZIP esiste
    if not os.path.exists(zip_path):
        print(f"Il file {zip_path} non esiste.")
        return

    # Crea la directory di destinazione se non esiste
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)

    # Apri il file ZIP
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # Estrai tutti i file
        zip_ref.extractall(extract_to)
        print(f"File estratti con successo in {extract_to}")

# Esempio di utilizzo
for i in range(3000, -1, -1):
    zip_path = f'/home/mattia/Downloads/temp/flag{i}.zip'
    extract_to = '/home/mattia/Downloads/temp'
    extract_zip(zip_path, extract_to)


