from cryptography.fernet import Fernet
import base64
import configparser


# def generate_key():
#     # 키 생성(매번 키가 바뀌니 다시 복호화 하기 위해서는 키를 저장해두자)
#     key = Fernet.generate_key()
#     print('key: ', key)
#     key = b'A_3A8jy8zYdduHDn-u_gXHwjnZb0XhHw9Hirs5wC3q4='
#     return key.decode()

def encode_key(key):
    return base64.b64encode(key.encode())


def encrypt(dict):
    key = dict.pop('KEY')
    encode_dict = dict
    print(key)
    fernet = Fernet(key)
    for (k, v) in dict.items():
        encode_dict[k] = fernet.encrypt(str(v).encode())
    encode_dict['KEY'] = encode_key(key)
    return encode_dict


def save_cfg(file_name, dict):
    config = configparser.ConfigParser()
    config['DBConnInfo'] = {}
    config['DBConnInfo']['HOST'] = dict.pop('HOST')
    for (key, value) in encrypt(dict).items():
        config['DBConnInfo'][key] = value.decode()
    with open(file_name, 'w', encoding='utf-8') as configfile:
        config.write(configfile)
    print('complete!!')


if __name__ == '__main__':
    dict = {'HOST': '0.0.0.0',
            'KEY': 'A_3A8jy8zYdduHDn-u_gXHwjnZb0XhHw9Hirs5wC3q4=',
            'USER': 'hjm',
            'PASSWORD': 'abc1234!'}
    file_name = 'dbConnInfo.cfg'
    save_cfg(file_name, dict)
