"""
7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. 
При вызове функции должен создаваться объект-генератор. 
Функция должна вызываться следующим образом: for el in fact(n). 
Функция отвечает за получение факториала числа,
а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.

Подсказка: факториал числа n — произведение чисел от 1 до n. 
Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""

from itertools import count
from functools import reduce


def fact(n):
    num_list = []
    for num in count(1):
        if num > n:
            break
        else:
            num_list.append(num)
        res = reduce(lambda x, y: x * y, num_list)
        yield res
    

try:
    num_var = int(input('Введите целое число, вплоть до которого нужно исчислить факториалы: '))
    print(f'Мы создали генератор для ваших нужд: {fact(num_var)}')
    i = 0
    for el in fact(num_var):
        i += 1
        print(f'Факториал от {i} равен {el}')
except ValueError:
    print('Вы ввели не целое число!')
