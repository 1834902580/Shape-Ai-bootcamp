import hashlib

inp = input('what do u want to hash: ')
hashing = hashlib.md5(inp.encode())
print(('Hashed String : ')+(hashing.hexdigest()))