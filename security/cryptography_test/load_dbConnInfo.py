from configparser import ConfigParser
from cryptography.fernet import Fernet
import base64


def read_dbconninfo(file_name):
    cfg = ConfigParser()
    cfg.read(file_name)
    HOST = cfg['DBConnInfo']['HOST']
    USER = cfg['DBConnInfo']['USER']
    PASSWORD = cfg['DBConnInfo']['PASSWORD']
    KEY = cfg['DBConnInfo']['KEY']
    return HOST, USER, PASSWORD, KEY


def decrypt_dbconninfo(file_name):
    HOST, USER, PASSWORD, KEY = read_dbconninfo(file_name)
    key = base64.b64decode(KEY)
    fernet = Fernet(key)
    decrypt_password = fernet.decrypt(PASSWORD.encode()).decode()
    decrypt_user = fernet.decrypt(USER.encode()).decode()
    key = key.decode()

    return HOST, decrypt_user, decrypt_password, key


if __name__ == '__main__':
    HOST, USER, PASSWORD, KEY = decrypt_dbconninfo('dbConnInfo.cfg')
    print('HOST: ', HOST)
    print('decrypt_password: ', USER)
    print('decrypt_password: ', PASSWORD)
    print('decrypt_key: ', KEY)
