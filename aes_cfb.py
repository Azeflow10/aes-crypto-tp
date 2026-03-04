from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def cfb():
    key = get_random_bytes(16)
    iv  = get_random_bytes(16)
    message = b"Bonjour, comment allez-vous?"

    print("CFB")
    print("Message original:", message.decode())

    cipher = AES.new(key, AES.MODE_CFB, iv)
    ciphertext = cipher.encrypt(message)
    print("Message chiffre:", ciphertext.hex())

    decipher = AES.new(key, AES.MODE_CFB, iv)
    decrypted = decipher.decrypt(ciphertext)
    print("Message dechiffre:", decrypted.decode())