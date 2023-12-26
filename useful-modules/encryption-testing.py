from cryptography.fernet import Fernet
key = 'wn7Nz2jV5wdG_i5tRZ0ZS_bPGDVQHU0_0TaQEVeIyrU='
# key = Fernet.generate_key()
print(f'Key: {key}')
f = Fernet(key)

message = 'hello'
encoded = f.encrypt(message.encode())
print(f'encoded: {encoded}')

decoded = bytes.decode(f.decrypt(encoded))
print(f'Decoded: {decoded}')