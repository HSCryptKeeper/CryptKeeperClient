import os
import random

def check_dot_ignore():
    ignore_text = '\n# Added by CryptMaster\n.crypt_file'
    file = '.gitignore'
    if os.path.isfile(file):
        with open(file, 'r') as f:
            git_ignore = f.read()
        if not '.crypt_file' in git_ignore:
            with open(file, 'a') as f:
                f.write(ignore_text)
    else:
        with open(file, 'w') as f:
            f.write(ignore_text[1:])



def get_create_config():
    crypt_file = '.crypt_file'
    if not os.path.isfile(crypt_file):
        ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        salt = ''
        for i in range(32):
            salt += (random.choice(ALPHABET))
        with open(crypt_file, 'w+') as f:
            f.write(salt)
        check_dot_ignore()
    with open(crypt_file, 'r') as f:
        crypt_config = f.readline()
    return crypt_config

SALT = get_create_config()

