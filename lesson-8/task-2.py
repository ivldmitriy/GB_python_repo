"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
и не завершиться с ошибкой.
"""


class ZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt


class NumError(Exception):
    def __init__(self, txt):
        self.txt = txt


print('Добро пожаловать в место, где делят число 12 на разные числа!')
print('Чтобы покинуть это место, введите stop')
while True:
    var = input('Введите целое число, на которое хотите поделить число 12: ')
    if var == 'stop':
        break
    try:
        var = int(var)
        res = 12 / var
        print(f'12/{var}={res}')
    except ValueError:
        try:
            raise NumError("Вы ввели не число!") from None
        except NumError as err:
            print(err)
            continue
    except ZeroDivisionError:
        try:
            raise ZeroError("На ноль делить нельзя!") from None
        except ZeroError as err:
            print(err)
            continue
