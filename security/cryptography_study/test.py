from configparser import ConfigParser
from cryptography.fernet import Fernet

if __name__ == '__main__':
    file_name = './test.cfg'

    config = ConfigParser()
    config.read(file_name)

    fernet = Fernet(config['security']['KEY'].encode())
    decrypt_password = fernet.decrypt(config['security']['PASSWORD'].encode())
    print('decrypt_password: ', decrypt_password.decode())
    password = 'abc1234!'
    print(password == decrypt_password.decode())
