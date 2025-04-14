import random
import string

LENGTH = 32

def genrate_api_keys():
    random_string = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(LENGTH)])
    return random_string