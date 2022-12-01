from cryptography.fernet import Fernet


# cryptography는 대칭키 알고리즘을 사용한다.


class Secret:
    def __init__(self, fernet):
        self.fernet = fernet

    def encrypt(self, key, value):
        print(f'{key} : ', self.fernet.encrypt(value))


if __name__ == '__main__':
    # 키 생성(매번 키가 바뀌니 다시 복호화 하기 위해서는 키를 저장해두자)
    # key = Fernet.generate_key()
    # print('key: ', key)
    # key = b'A_3A8jy8zYdduHDn-u_gXHwjnZb0XhHw9Hirs5wC3q4='
    # fernet = Fernet(key)
    #
    # password = b'abc1234!'
    # # encrypt_password = fernet.encrypt(password)
    # # print('encrypt_password: ', encrypt_password)
    # encrypt_password = b'gAAAAABjiEYHv8iDp06mBETaAE1ZZeFVUsCL2kJLKg_XLLOjGfESTBYlkrP76W7Z1PiA0gVhD7XPtma8eadJe_VH6xs8OclaYw=='
    # decrypt_password = fernet.decrypt(encrypt_password)
    # print('origin_password :', password.decode())
    # print('decrypt_password:', decrypt_password.decode())
    #
    # print(password == decrypt_password)

    dict = {'url': '0.0.0.0', 'dbname': 'study', 'user': 'hjm', 'password': '1234'}
    for (k, v) in dict.items():
        print(k, v)
