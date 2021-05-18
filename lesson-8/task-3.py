"""
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере.
Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
"""


class NumError(Exception):
    def __init__(self, txt):
        self.txt = txt


print('Добро пожаловать в место, где числа добавляют в список!')
print('Чтобы покинуть это место, введите stop')
lst = []
while True:
    var = input('Введите число, которое хотите добавить к списку: ')
    if var == 'stop':
        break
    try:
        if var.isnumeric():
            lst.append(float(var))
        else:
            try:
                var = float(var)
                lst.append(var)
                try:
                    raise Exception()
                except Exception:
                    continue
            except ValueError:
                raise NumError("Вы ввели не число!") from None
    except NumError as err:
        print(err)
        continue
print(lst)
