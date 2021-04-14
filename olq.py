import random
import string

def get_random_password(lenght):
    letters = string.ascii_lowercase
    password = "".join(random.choice(letters) for i in range(lenght))
    print(password)
get_random_password(8)

