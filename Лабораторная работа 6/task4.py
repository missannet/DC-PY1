import json

INPUT_FILE = "input.csv"

def csv_to_list_dict(filename) -> list[dict]:
    '''
    Функция конвертер из csv в json формат

    :param filename: str
    :return: list_dict: list
    '''

    with open(filename, 'r') as f:  # открываем файл на чтение
        headers = f.readline()  # читаем первую строку
        headers = headers.split(",")    # разделяем элементы по символу и добавляем в список
        head = [elem.rstrip() for elem in headers]  # перебираем список по элементам, убирая конечные символы
        list_dict = []
        for line in f:  # перебираем все остальные непрочитанные элементы
            line = line.split(',')  # разделяем элементы по символу и добавляем в список
            line = [x.rstrip() for x in line]  # перебираем список по элементам, убирая конечные символы
            line = dict(zip(head, line))  # объединяем 2 списка и добавляем их в словарь
            list_dict.append(line)  # добавляем словарь в список
        return list_dict  # возвращаем собранный список


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
