print("FILE PROTECTION UTILITY")

key = 5

text = input("Enter file content: ")

# Encryption
encrypted = ""

for char in text:
    encrypted += chr(ord(char) + key)

print("Encrypted Content:", encrypted)

# Decryption
decrypted = ""

for char in encrypted:
    decrypted += chr(ord(char) - key)

print("Decrypted Content:", decrypted)

print("File Protection Completed!")
