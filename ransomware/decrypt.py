import os
from cryptography.fernet import Fernet

files = []
key = Fernet.generate_key()

with open ("chave.key", "rb") as chave:
    secretKey = chave.read()

for file in os.listdir():
    if file == "encrypt.py" or file == "chave.key" or file == "encrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

for file in files:
    with open(file, "rb") as arquivo:
        conteudo = arquivo.read()
    conteudo_decrypt = Fernet(secretKey).decrypt(conteudo)
    with open(file, "wb") as arquivo:
        arquivo.write(conteudo_decrypt)