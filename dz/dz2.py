import re


def pas(a):
    return re.findall("^[A-Za-z0-9_@-]{3,16}$", a)


print(pas(input("Введите пароль")))
