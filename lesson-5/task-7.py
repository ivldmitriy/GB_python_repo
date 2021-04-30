"""
7. Создать (не программно) текстовый файл,
в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл,
вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список.
Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
"""

import json

try:
    with open("file_for_t7", "r", encoding='utf-8') as file:
        aver_profit = 0.0
        about_firm = {}
        about_profit = {}
        waste_count = 0
        for line in file:
            (name, org, gain, cost) = (' '.join(line.split()[:-3]), line.split()[-3],
                                       line.split()[-2], line.split()[-1])
            (gain, cost) = map(float, (gain, cost))
            profit = gain - cost
            if profit >= 0:
                aver_profit += profit
            else:
                waste_count += 1
            about_firm[name] = profit
    aver_profit = aver_profit / (len(about_firm) - waste_count)
    about_profit["average_profit"] = aver_profit
    data = [about_firm, about_profit]
    with open("analytic_from_t7.json", "w", encoding='utf-8') as analytic:
        json.dump(data, analytic, indent=2, ensure_ascii=False)
except (IOError, ValueError) as err:
    print(err)
