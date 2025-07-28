import os
import shutil

def save_file(file_path, storage_dir):
    if not os.path.exists(storage_dir):
        os.makedirs(storage_dir)
    shutil.move(file_path, os.path.join(storage_dir, os.path.basename(file_path)))

def retrieve_file(file_name, storage_dir):
    return os.path.join(storage_dir, file_name)
