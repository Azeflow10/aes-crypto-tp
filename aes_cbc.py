from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def cbc():
    key = get_random_bytes(16)
    iv  = get_random_bytes(16)
    message = b"Bonjour, comment allez-vous?"

    print("CBC")
    print("Message original:", message.decode())

    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(message, AES.block_size))
    print("Message chiffre :", ciphertext.hex())

    decipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(decipher.decrypt(ciphertext), AES.block_size)
    print("Message dechiffre:", decrypted.decode())