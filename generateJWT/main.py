import random
import string
import jwt

def generate_token():
    random_string = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16))
    random_secret = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16))
    random_username = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16))
    random_password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16))
    dict = {'username': random_username, 'password': random_password, 'random_string': random_string}
    token = jwt.encode(dict, random_secret, algorithm='HS256')
    return token


if __name__ == '__main__':
    print(generate_token())
    input('')