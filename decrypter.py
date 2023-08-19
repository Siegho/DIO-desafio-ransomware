import os
import pyaes

def decrypt_file(file_name, key):
    with open(file_name, "rb") as file:
        file_data = file.read()

    aes = pyaes.AESModeOfOperationCTR(key)
    decrypt_data = aes.decrypt(file_data)

    os.remove(file_name)

    new_file_name = file_name.replace(".ransomwaretroll", "")
    with open(new_file_name, "wb") as new_file:
        new_file.write(decrypt_data)

if __name__ == "__main__":
    key = b"testeransomwares"
    encrypted_file_name = "teste.txt.ransomwaretroll"
    decrypt_file(encrypted_file_name, key)
