import random  # импортируем инструмент для генерации случайных выборок
import string  # импортируем методы для str


def get_random_password() -> str:
    """
    This function generates random passwords, length n.
    Characters used: uppercase letters (A - Z),
    lowercase letters (a - z), numbers: 0 - 9

    :return:
    password
    """
    n = 8  # задаем длину пароля
    low_ltrs = string.ascii_lowercase.strip()  # строка с буквами нижнего регистра
    upper_ltrs = string.ascii_uppercase.strip()  # строка с буквами верхнего регистра
    num = string.digits  # строка цифр
    items = (low_ltrs + upper_ltrs + num)

    while True:  # проверка наличия всех символов

        all_bool = list()
        password = random.sample(population=items, k=n)
        all_bool.append(any(x in password for x in low_ltrs))  # проверяем пароль на наличие букв с нижним регистром
        all_bool.append(any(x in password for x in upper_ltrs))  # проверяем пароль на наличие букв с верхним регистром
        all_bool.append(any(x in password for x in num))  # проверяем пароль на наличие цифр

        if all(all_bool):
            return "".join(password)


print(get_random_password())
