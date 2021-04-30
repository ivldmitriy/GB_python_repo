"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
# Создаем словарь числительных

ru_numbers = ['Один', 'Два', 'Три', 'Четыре', 'Пять', 'Шесть', 'Семь', 'Восемь', 'Девять', 'Ноль']
en_numbers = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Zero']
num_dict = dict(zip(en_numbers, ru_numbers))


def transformer(string):
    for en_number in num_dict:
        if en_number in string:
            string = string.replace(en_number, num_dict[en_number])
    return string


try:
    with open("file_for_t4", "r", encoding='utf-8') as file_r:
        with open("file_from_t4", "w+") as file_w:
            while True:
                line = file_r.readline()
                if not line:
                    break
                proc_line = transformer(line)
                file_w.writelines(proc_line)
except FileNotFoundError:
    print("Файл не найден.")
