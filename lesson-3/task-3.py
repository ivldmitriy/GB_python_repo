"""
3. Реализовать функцию my_func(),
которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(arg_1, arg_2, arg_3):
    arg_list = [arg_1, arg_2, arg_3]
    arg_list.pop(arg_list.index(min(arg_list)))
    res = sum(arg_list)
    return res


print(my_func(1, 2, 3))
print(my_func(3, 2, 2))
print(my_func(1, 1, 1))
