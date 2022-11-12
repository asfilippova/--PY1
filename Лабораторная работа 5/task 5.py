import random
import string

def get_random_password() -> str:
    password = string.ascii_uppercase + string.ascii_lowercase + string.digits
    random_pass = ''.join(random.sample(password, 8))
    return random_pass

print(get_random_password())
