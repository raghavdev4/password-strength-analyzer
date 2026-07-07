import random
import string

def generate_password():
    characters = (
        string.ascii_uppercase +
        string.ascii_lowercase +
        string.digits +
        "!@#$%^&*"
    )

    password = ""

    for i in range(12):
        password += random.choice(characters)

    return password