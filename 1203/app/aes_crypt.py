import json

from cryptography.fernet import Fernet


class AESCipher(object):
    def __init__(self):
        key = bytes(self.__get_key())
        self.fernet = Fernet(key)

    @staticmethod
    def __generate_key():
        """Generates and returns fernet key

        :return: str - key
        """
        key = Fernet.generate_key()
        return key

    def __get_key(self):
        try:
            fp = open('/store/secrets.json', 'r')
        except Exception:
            fp = open('/store/secrets.json', 'w')
            data = {
                'secret_key': self.__generate_key()
            }
            json.dump(data, fp)
        else:
            data = json.load(fp)

        return data.get('secret_key')

    def encrypt(self, raw):
        enc = self.fernet.encrypt(bytes(raw))
        return enc

    def decrypt(self, enc):
        return self.fernet.decrypt(bytes(enc))


if __name__ == '__main__':
    # Test scripts
    cipher = AESCipher()
    data = 'qwerty'
    enc = cipher.encrypt(data)
    print(enc)

    cipher = AESCipher()
    raw = cipher.decrypt(enc)
    print(raw)
