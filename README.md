# Secure File Storage System

## Overview
This project implements a secure file storage system that allows users to securely upload, store, and download files. The files are encrypted using AES encryption before being stored, ensuring that they remain secure.

## Features
- **File Encryption:** Files are encrypted using AES encryption before being stored.
- **Secure Storage:** Encrypted files are securely stored in the specified directory.
- **File Retrieval:** Encrypted files can be retrieved and decrypted.

## Files
- `main.py`: The main script to upload and download files.
- `encryption.py`: Handles file encryption and decryption.
- `storage.py`: Manages file saving and retrieval.

## Setup
1. Install dependencies: `pip install cryptography`
2. Run the script:
   - To upload a file: `python main.py`
   - To download a file: `python main.py`
