import zipfile
import os

def extract_zip(zip_path, extract_to, password):
    """
    Estrae un file ZIP protetto da password.

    :param zip_path: Percorso del file ZIP.
    :param extract_to: Directory di destinazione per l'estrazione.
    :param password: Password per decriptare il file ZIP.
    :return: True se l'estrazione è riuscita, False altrimenti.
    """
    # Verifica se il file ZIP esiste
    if not os.path.exists(zip_path):
        print(f"Il file {zip_path} non esiste.")
        return False

    # Crea la directory di destinazione se non esiste
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)

    try:
        # Apri il file ZIP
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # Estrai tutti i file usando la password
            zip_ref.extractall(extract_to, pwd=password.encode())
            print(f"File estratti con successo da {zip_path} usando la password: {password}")
            return True
    except RuntimeError as e:
        # Password errata
        return False
    except zipfile.BadZipFile:
        # File ZIP corrotto o non valido
        return False
    except Exception as e:
        # Altri errori
        print(f"Errore imprevisto durante l'estrazione di {zip_path}: {e}")
        return False

# Path al file delle password
password_file = 'rockyou.txt'

# Path alla directory contenente i file ZIP
zip_directory = '/home/mattia/Downloads/temp/'
extract_to = '/home/mattia/Downloads/temp'

# Elenco dei file ZIP da testare
zip_files = [f'{i}.zip' for i in range(100, -1, -1)]

# Leggi le password dalla wordlist
with open(password_file, 'r', encoding='latin-1') as file:
    passwords = [line.strip() for line in file]

# Prova a estrarre ogni file ZIP con ogni password
for zip_filename in zip_files:
    zip_path = os.path.join(zip_directory, zip_filename)
    print(f"Provando a estrarre {zip_path}...")
    for password in passwords:
        if extract_zip(zip_path, extract_to, password):
            break  # Esce dal loop delle password se l'estrazione ha avuto successo
