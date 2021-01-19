from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(key)
cipher_suite = Fernet(key)
ciphered_text = cipher_suite.encrypt(b"supersecretpassword")
print(ciphered_text)

