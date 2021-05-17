import random
import string


# printing lowercase
def generate_lowercase_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))
