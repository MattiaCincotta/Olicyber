import sys
from hashlib import sha256
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import os

def get_chunk_number(filename):
    """Extract the chunk number from a chunk filename."""
    base = os.path.splitext(filename)[0]
    return int(base.split('_')[-1])

def main():
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <original filename>')
        sys.exit(1)
    
    original_filename = sys.argv[1]
    key = sha256(original_filename.encode()).digest()
    
    chunk_dir = 'encrypted_chunks'
    if not os.path.exists(chunk_dir):
        print(f"Error: Directory '{chunk_dir}' not found.")
        sys.exit(1)
    
    chunk_base = f"{original_filename}_"
    chunk_files = []
    for filename in os.listdir(chunk_dir):
        if filename.startswith(chunk_base) and filename.endswith('.enc'):
            chunk_files.append(filename)
    
    if not chunk_files:
        print(f"No encrypted chunks found for '{original_filename}'.")
        sys.exit(1)
    
    # Sort the chunk files by their chunk number
    chunk_files.sort(key=get_chunk_number)
    chunks = [os.path.join(chunk_dir, f) for f in chunk_files]
    
    decrypted_data = b''
    for chunk_path in chunks:
        with open(chunk_path, 'rb') as f:
            encrypted_chunk = f.read()
        
        iv = b'\x00' * 16
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_chunk = cipher.decrypt(encrypted_chunk)
        
        try:
            unpadded_chunk = unpad(decrypted_chunk, AES.block_size)
        except ValueError as e:
            print(f"Error decrypting chunk {chunk_path}: {e}")
            sys.exit(1)
        
        decrypted_data += unpadded_chunk
    
    # Write the decrypted data to the original filename
    with open(original_filename, 'wb') as f:
        f.write(decrypted_data)
    
    print(f"Successfully decrypted to '{original_filename}'.")

if __name__ == '__main__':
    main()