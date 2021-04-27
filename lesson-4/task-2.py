"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка, 
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. 
Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""

old_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(f'Исходный список: {old_list}')
print('Поиск элементов списка, значения которых больше значения предыдущего...')

new_list = [old_list[el] for el in range(1, len(old_list)) if old_list[el] > old_list[el-1]]
print(f'Новый список: {new_list}')
