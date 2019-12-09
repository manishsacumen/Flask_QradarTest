import json

from cryptography.fernet import Fernet


def random_word():
    return Fernet.generate_key()


def get_flask_keys():
    try:
        fp = open('/store/flask_secrets.json', 'r')
    except Exception:
        fp = open('/store/flask_secrets.json', 'w')
        data = {
           'secret_key': random_word(),
           'token': random_word(),
        }
        json.dump(data, fp)
    else:
        data = json.load(fp)

    return data
