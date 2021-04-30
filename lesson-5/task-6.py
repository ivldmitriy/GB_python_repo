"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка
описывает учебный предмет и наличие  лекционных, практических и лабораторных занятий
по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
schedule = {}

try:
    with open("file_for_t6", "r", encoding='utf-8') as file:
        for line in file:
            lesson = line.split()[0]
            lesson = ''.join(smb for smb in list(lesson) if smb.isalpha())
            for smb in line:
                if not smb.isnumeric():
                    line = line.replace(smb, ' ')
            hours = sum(map(int, line.split()))
            schedule[lesson] = hours
    print('Учебная нагрузка по предметам:\n'
          f'{schedule}')
except (IOError, ValueError) as err:
    print(err)
