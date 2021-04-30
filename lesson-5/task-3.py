"""3. Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников."""

from functools import reduce

gen_led = {}

try:
    with open("file_for_t3", "r") as file:
        # Заполняем словарь сотрудников из файла
        for line in file:
            line = line.replace(',', '.')
            (name, salary) = (line.split()[0], line.split()[1:])
            name = ''.join(smb for smb in list(name) if smb.isalpha())
            salary = ''.join(num for num in salary if not num.isalpha())
            try:
                gen_led[name] = float(salary)
            except ValueError:
                print('Ошибка типов! Не удается перевести оклад в численный формат')
    # Ищем тех, у кого оклад менее 20 000 рублей
    print('Список сотрудников с окладом менее 20 000.00 рублей:')
    for name in gen_led:
        if gen_led[name] < 20000:
            print(name)
    # Расчитываем средний оклад сотрудников
    avr_salary = reduce(lambda a, b: a + b, [gen_led[name] for name in gen_led])/len(gen_led)
    print(f'Средний оклад сотрудников {avr_salary:.2f} рублей')
except FileNotFoundError:
    print("Файл не найден.")
