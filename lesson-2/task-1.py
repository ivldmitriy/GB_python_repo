"""
1. Создать список и заполнить его элементами
 различных типов данных.
 Реализовать скрипт проверки типа
 данных каждого элемента.
 Использовать функцию type() для проверки типа.
 Элементы списка можно не запрашивать у
 пользователя, а указать явно, в программе.
"""

test_list = []  # create blank list
test_elem = 1.23
test_list.append(int(test_elem))
test_list.append(float(test_elem))
test_list.append(str(test_elem))
test_list.append(bool(test_elem))
test_list.append(bytes(int(test_elem)))
print(f'Test list contains: {test_list}')
i = 0
for element in test_list:
    i += 1
    tp_var = type(element)
    print(f"Type of {i} element is {tp_var}")
