import os
import itertools

def ricomponi_permutazioni(cartella_pezzi, output_dir):
    files = sorted(f for f in os.listdir(cartella_pezzi) if f.endswith('.bin'))
    
    # Genera tutte le permutazioni dei file
    permutazioni = list(itertools.permutations(files))

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i, perm in enumerate(permutazioni):
        output_file = os.path.join(output_dir, f"video_perm_{i+1}.mp4")
        with open(output_file, 'wb') as f_out:
            for filename in perm:
                path = os.path.join(cartella_pezzi, filename)
                with open(path, 'rb') as f_in:
                    dati = f_in.read()
                    f_out.write(dati)
        print(f"[✓] Creata permutazione {i+1}: {perm} -> {output_file}")

if __name__ == "__main__":
    cartella = "/home/mattia/Videos/temp2"  # Cartella con i pezzi
    output_dir = "/home/mattia/Videos/permutazioni"
    ricomponi_permutazioni(cartella, output_dir)
