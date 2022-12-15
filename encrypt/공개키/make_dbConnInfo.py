from cryptography.fernet import Fernet
import configparser
from Crypto.PublicKey import RSA


def make_key(plane_key):
    # generate RSA object (2048 bit)
    key = RSA.generate(2048)

    # generate encrypted_key
    # encryption algorithms reference : https://pycryptodome.readthedocs.io/en/latest/src/io/pkcs8.html
    encrypted_key = key.exportKey(passphrase=plane_key, pkcs=8, protection="PBKDF2WithHMAC-SHA1AndAES256-CBC")

    # generate private key and save
    with open('./private_rsa_key.pem', 'wb') as f:
        f.write(encrypted_key)

    # generate public key and save
    with open('./public_rsa_key.pem', 'wb') as f:
        f.write(key.publickey().exportKey())


def read_key(path):
    f = open(path, 'r')
    key = RSA.importKey(f.read())
    f.close()
    return key


def encrypt(dict):
    key = read_key('./public_rsa_key.pem')
    fernet = Fernet(key)
    for (k, v) in dict.items():
        dict[k] = fernet.encrypt(str(v).encode())
    return dict


def save_cfg(file_name='./dbConnInfo.cfg', dict=None):
    config = configparser.ConfigParser()
    config['DBConnInfo'] = {k: v.decode() for (k, v) in encrypt(dict).items()}
    with open(file_name, 'w', encoding='utf-8') as configfile:
        config.write(configfile)
    print('encrypt complete!!')


if __name__ == '__main__':
    # make_key('secret_key')
    dict = {'HOST': '172.17.28.175',
            'DBNAME': 'cai',
            'USER': 'postgres',
            'PASSWORD': 'qhdks@00'}

    file_path = './'
    file_name = 'dbConnInfo.cfg'
    save_cfg(file_path + file_name, dict)
