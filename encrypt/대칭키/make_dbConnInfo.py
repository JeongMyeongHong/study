from cryptography.fernet import Fernet
import base64
import configparser


def generate_key():
    return Fernet.generate_key().decode()


def encrypt_key(key):
    return base64.b64encode(key.encode())


def encrypt(dict):
    key = dict.pop('KEY')
    fernet = Fernet(key)
    for (k, v) in dict.items():
        dict[k] = fernet.encrypt(str(v).encode())
    dict['KEY'] = encrypt_key(key)
    return dict


def save_cfg(file_name='./dbConnInfo.cfg', dict=None):
    config = configparser.ConfigParser()
    config['DBConnInfo'] = {k: v.decode() for (k, v) in encrypt(dict).items()}
    with open(file_name, 'w', encoding='utf-8') as configfile:
        config.write(configfile)
    print('encrypt complete!!')


if __name__ == '__main__':
    # key는 필수요소
    dict = {'KEY': generate_key(),
            'HOST': '172.17.28.175',
            'DBNAME': 'cai',
            'USER': 'postgres',
            'PASSWORD': 'qhdks@00'}

    file_path = 'HongJM/encrypt/'
    file_name = 'dbConnInfo.cfg'
    save_cfg(file_path + file_name, dict)
