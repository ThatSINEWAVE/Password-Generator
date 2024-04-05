import string
import secrets
import random


def generate_password(length, include_numbers, include_mixed_case, include_symbols):
    characters = string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation
    if include_mixed_case:
        password = ''.join(secrets.choice(characters) for i in range(length))
    else:
        password = ''.join(random.choice(string.ascii_lowercase) for i in range(length))
    return password


def generate_passwords(length, include_numbers, include_mixed_case, include_symbols, num_passwords):
    passwords = []
    for i in range(num_passwords):
        password = generate_password(length, include_numbers, include_mixed_case, include_symbols)
        passwords.append(password)
    return passwords
