import hashlib
# sha256은 단방향 해시 알고리즘으로서 256비트로 구성, 64자리 문자열을 반환한다.
# SHA-2 계열중 하나이며 블록체인에서 현재 22년12월 가장 많이 채택하여 사용하고 있다.
if __name__ == '__main__':
    password = 'abc1234!'
    encrypt_password = hashlib.sha256(password.encode()).hexdigest()
    print(encrypt_password)

