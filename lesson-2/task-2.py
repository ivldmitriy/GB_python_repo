"""
2. Для списка реализовать обмен значений
 соседних элементов, т.е.
 Значениями обмениваются элементы
 с индексами 0 и 1, 2 и 3 и т.д.
 При нечетном количестве элементов
 последний сохранить на своем месте.
 Для заполнения списка элементов
 необходимо использовать функцию input().
"""

my_list = []
print("Please, help the Dasha to fill the empty list")
print("Type 'mutabor' to start the list transformation")

while True:
    elem_var = input('Enter one more element: ')
    if elem_var == 'mutabor':
        break
    my_list.append(elem_var)

print(f"Now list is {my_list}")
print("OK, here we go")

for i in range(0, len(my_list)-1, 2):
    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]

print(f"Now list is {my_list}")
