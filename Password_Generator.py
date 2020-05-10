
import random

chars = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#"
length = input("Length of password: ")

length = int(length)

password = " "
for c in range(length):
    password += random.choice(chars)

print(password)
