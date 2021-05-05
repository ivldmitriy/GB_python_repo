"""
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв
и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием.
В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(string_var):
    string_var = string_var.capitalize()
    return string_var


def splitter(string_var):
    list_var = string_var.split()
    return list_var


def latin_checker(word):
    for letter in list(word):
        if ord(letter) < 97 or ord(letter) > 122:
            print('Это не латинские буквы в нижнем регистре')
            return False
    return True


print('Введите строку из слов, разделенных пробелом.')
print('Каждое слово состоит из латинских букв в нижнем регистре.')
proc_var = []
field = input('Поле ввода: ')
var = splitter(field)
for wrd in var:
    if latin_checker(wrd) is False:
        break
    proc_var.append(int_func(wrd))
print(f"Итого: {' '.join(proc_var)}")
