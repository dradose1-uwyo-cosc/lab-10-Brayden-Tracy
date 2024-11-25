# Brayden Tracy
# UWYO COSC 1010
# 11/24/2024
# Lab 10
# Lab Section: 15
# Sources, people worked with, help given to: google and copilot
# your
# comments
# here

from hashlib import sha256
from pathlib import Path

def get_hash(to_hash):
    """Hashes a string using SHA-256 and returns the uppercase hexadecimal hash."""
    return sha256(to_hash.encode('utf-8')).hexdigest().upper()

try:
    with open('hash', 'r') as hash_file:
        password_hash = hash_file.read().strip()
except FileNotFoundError:
    print("The hash file was not found.")
    password_hash = None
except IOError:
    print("Error occurred while reading the hash file.")
    password_hash = None

if password_hash:
    try:
        with open('rockyou.txt', 'r') as password_file:
            passwords = password_file.readlines()
    except FileNotFoundError:
        print("The passwords file was not found.")
    except IOError:
        print("Error occurred while reading the passwords file.")
    else:
        for password in passwords:
            password = password.strip()
            if get_hash(password) == password_hash:
                print(f"The password is: {password}")
                break
        else:
            print("No matching password found.")
