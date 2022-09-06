import hashlib
from uuid import uuid4

password = input("Введите пароль: ")

salt = uuid4().hex


def hash_pass(data, sal):
    res = hashlib.sha256(sal.encode() + data.encode()).hexdigest()
    pass_2 = input("Введите пароль повторно: ")
    exp_res = hashlib.sha256(sal.encode() + pass_2.encode()).hexdigest()
    if exp_res == res:
        return res, print(res)
    else:
        return print("Неверный пароль")


hash_password = hash_pass(password, salt)