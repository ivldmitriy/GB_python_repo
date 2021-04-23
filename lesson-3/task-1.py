"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление.
Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.
"""


def divider(num_1, num_2):
    try:
        quot = num_1/num_2
    except ZeroDivisionError:
        print('Деление на ноль!')
        return 'ошибка деления'
    return quot


try:
    var1 = float(input('Введите первое число - делимое: '))
    var2 = float(input('Введите второе число - делитель: '))
    res = divider(var1, var2)
except ValueError:
    print('Введены не числа')
    res = 'ошибка типов'
print(f'Результат деления: {res}')
Ы