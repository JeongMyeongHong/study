from configparser import ConfigParser
from cryptography.fernet import Fernet
import base64


def decrypt_dbconninfo(file_name='./dbConnInfo.cfg'):
    cfg = ConfigParser()
    cfg.read(file_name)
    cfg_dict = {s: dict(cfg.items(s)) for s in cfg.sections()}
    fernet = Fernet(base64.b64decode(cfg_dict['DBConnInfo'].pop('key')))
    return {k: fernet.decrypt(v.encode()).decode()for (k, v) in cfg_dict['DBConnInfo'].items()}

