#!/usr/local/bin/python3

import string
import random
import os
import time

os.system("clear" if os.name == "posix" else "cls")

# api

char = "".join(string.printable.split())
name = "Password Generator"
passwd = ""

# tilte

print(name)

# text

pass_number = int(input("\nHow many passwords do you want to generate: "))
pass_length = int(input("How many characters do you want the password to be: "))

print("\nGenerating your password/s")
time.sleep(2)

# code

for _ in range(pass_number):
    for _ in range(pass_length):
        passwd += random.choice(char)
    print("Your generated password/s is/are: " + passwd)
    passwd = ""
    time.sleep(0.5)
print()