"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме
и после этого завершить программу.
"""

mode = True
big_sum = 0.0


def sum_maker(string_var):
    global mode
    res = 0
    arg_list = string_var.split()
    for arg in arg_list:
        if arg == ':wq':
            print('Введен спецсимвол. Завершение работы.')
            mode = False
            return res
        try:
            res += float(arg)
        except ValueError:
            print('Некорректный ввод. Сумма не изменилась')
            return 0.0
    return res


print('Программа суммирует введенные через пробел числа.')
print('Для выхода наберите в поле ввода :wq')
while mode is True:
    string_var = input('Поле ввода: ')
    big_sum += sum_maker(string_var)
    print(f'На текущий момент накопилась сумма: {big_sum}')
