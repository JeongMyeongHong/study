from configparser import ConfigParser
from Crypto.Cipher import PKCS1_v1_5 as Cipher
from Crypto.Random import get_random_bytes
from base64 import b64decode
from make_dbConnInfo import read_key


def decrypt_dbconninfo(file_name='./dbConnInfo.cfg'):
    cfg = ConfigParser()
    cfg.read(file_name)
    cfg_dict = {s: dict(cfg.items(s)) for s in cfg.sections()}
    pri_key = read_key('./private_rsa_key.pem')
    cipher = Cipher.new(pri_key)

    return {k: cipher.decrypt(b64decode(v.encode()), get_random_bytes(16)).decode() for (k, v) in cfg_dict['DBConnInfo'].items()}


if __name__ == '__main__':
    print(decrypt_dbconninfo())
