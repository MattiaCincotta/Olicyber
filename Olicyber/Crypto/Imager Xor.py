import sys

def xor(a: bytes, b: bytes) -> bytes:
    return bytes([x ^ y for x, y in zip(a, b)])

def decrypt_image(encrypted_image_path: str, key_path: str, output_path: str):
    with open(encrypted_image_path, "rb") as enc_file, open(key_path, "rb") as key_file:
        encrypted_data = enc_file.read()
        key = key_file.read(len(encrypted_data))  # Use only as much key data as needed

    decrypted_data = xor(encrypted_data, key)
    
    with open(output_path, "wb") as output_file:
        output_file.write(decrypted_data)
    
    print(f"Decrypted image saved as: {output_path}")

def create_black_file(output_path: str):
    size = 1000000  # 1MB = 1,000,000 bytes
    with open(output_path, "wb") as f:
        f.write(b'\x00' * size)
    print(f"Black file saved as: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) == 4:
        decrypt_image(sys.argv[1], sys.argv[2], sys.argv[3])
    elif len(sys.argv) == 2 and sys.argv[1] == "--black":
        create_black_file("black_file")
    else:
        print("Usage: python script.py <encrypted_image> <key> <output_image> OR python script.py --black")
        sys.exit(1)
