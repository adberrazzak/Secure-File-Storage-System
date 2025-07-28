from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_file(file_path):
    key = generate_key()
    fernet = Fernet(key)
    
    with open(file_path, 'rb') as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(file_path + '.enc', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    
    return file_path + '.enc'

def decrypt_file(encrypted_file_path, output_dir):
    with open(encrypted_file_path, 'rb') as enc_file:
        encrypted = enc_file.read()
    
    key = generate_key()  # Replace this with key management implementation
    fernet = Fernet(key)

    decrypted = fernet.decrypt(encrypted)

    output_path = os.path.join(output_dir, os.path.basename(encrypted_file_path).replace('.enc', ''))
    with open(output_path, 'wb') as dec_file:
        dec_file.write(decrypted)

    return output_path
