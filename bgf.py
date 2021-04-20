from cryptography.fernet import Fernet

message = "Hi Bitch"

key = Fernet.generate_key()

ferent = Fernet(key)

encMessage = ferent.encrypt(message.encode())

print(encMessage)

decMessage = ferent.decrypt(encMessage).decode()

print(decMessage)

