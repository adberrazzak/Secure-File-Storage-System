import os
from encryption import encrypt_file, decrypt_file
from storage import save_file, retrieve_file

def upload_file(file_path, storage_dir):
    encrypted_file_path = encrypt_file(file_path)
    save_file(encrypted_file_path, storage_dir)

def download_file(file_name, storage_dir, output_dir):
    encrypted_file_path = retrieve_file(file_name, storage_dir)
    decrypted_file_path = decrypt_file(encrypted_file_path, output_dir)
    print(f"File downloaded and decrypted to: {decrypted_file_path}")

if __name__ == "__main__":
    storage_dir = "./secure_storage"
    output_dir = "./downloads"
    os.makedirs(storage_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)

    # Upload a file
    file_to_upload = "sample.txt"
    upload_file(file_to_upload, storage_dir)

    # Download a file
    file_to_download = "sample.txt.enc"
    download_file(file_to_download, storage_dir, output_dir)
