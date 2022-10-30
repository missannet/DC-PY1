ef get_count_char(str_):
    dict_ = {}
    proc_s = 0
    for a in str_.lower():
        if a.isalpha():
            if a in dict_:
                dict_[a] += 1
            else:
                dict_[a] = 1
        else:
            proc_s += 1 * 100 / len(str_)
    dolya(dict_, str_, proc_s)
    return dict_

def dolya(dict_, str_, proc_s):
    dict2 = {}
    proc = 0
    for k, v in dict_.items():
        func = v * 100 / len(str_)
        dict2[v] = func
        proc += func
        print(k, "-", round(func, 2), end='%  ')
    prop = proc + proc_s
    print("\n", int(prop), "%")

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print("\n", get_count_char(main_str))
