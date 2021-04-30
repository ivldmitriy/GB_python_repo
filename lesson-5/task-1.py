"""
1. Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
print('Программа служит для записи строк текста в файл.')
print('Об окончании ввода данных свидетельствует пустая строка.')

try:
    with open("file_from_t1", "w+") as file:
        while True:
            new_string = input('Введите строку для записи в файл: ')
            if not new_string:
                break
            print(new_string, file=file)
        file.seek(0)
        content = file.read()
        print(f"Содержимое файла:\n{content}")
except IOError:
    print("Ошибка ввода-вывода")
