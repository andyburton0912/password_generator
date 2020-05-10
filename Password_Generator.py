
import random

chars = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#?"
length = input("Length of password: ")
length = int(length)
amount = input("Number of passwords: ")
amount = int(amount)


for p in range(amount):
    password = " "
    for c in range(length):
        password += random.choice(chars)
    print(password)
