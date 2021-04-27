"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция 
расчета заработной платы сотрудника. 
В расчете необходимо использовать формулу: 
(выработка в часах * ставка в час) + премия. 
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv


def account_func(output, wage, bonus):
    try:
        salary = float(output) * float(wage) + float(bonus)
        return float(salary)
    except ValueError:
        print("Проверьте формат ввода: выработка в часах, ставка в час в рублях, премия в месяц в рублях")
        exit()    


try:
    script_name, var_1, var_2, var_3 = argv
    salary_var = account_func(var_1, var_2, var_3)
    print(f'Заработная плата сотрудника составляет {salary_var:.2f} рублей в месяц')
except ValueError:
    print("Вы не ввели корректно нужные данные о сотруднике: выработка в часах, ставка в час, премия")
    exit()
