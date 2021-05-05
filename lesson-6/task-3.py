"""
3. Реализовать базовый класс Worker (работник),
в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
 оклад и премия, например, {"wage": wage, "bonus": bonus}.
 Создать класс Position (должность) на базе класса Worker.
 В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
 и дохода с учетом премии (get_total_income).
 Проверить работу примера на реальных данных
 (создать экземпляры класса Position, передать данные,
 проверить значения атрибутов, вызвать методы экземпляров).
"""

accounting = {'wage': [50000.00, 154000.00, 34000.00], 'bonus': [25000.00, 56000.00, 0.00]}


class Worker:

    employee_count = 0

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = (accounting['wage'][Worker.employee_count], accounting['bonus'][Worker.employee_count])
        Worker.employee_count += 1


class Position(Worker):

    def get_full_name(self):
        res = f'{self.name} {self.surname}'
        return res

    def get_total_income(self):
        res = sum(self._income)
        return res


lab_manager = Position('Ivan', 'Petrov', 'Lab manager')
lab_head = Position('Sergey', 'Dyadin', 'Head')
lab_tech = Position('Artem', 'Praslov', 'Technician')

personalities = [lab_head, lab_manager, lab_tech]

for people in personalities:
    print(f'Проверка атрибутов класса {people.position}:')
    print(f'Имя сотрудника: {people.name}')
    print(f'Фамилия сотрудника: {people.surname}')
    print(f'Должность сотрудника: {people.position}')
    print(f'Доходы сотрудника ({list(accounting.keys())[0]}, {list(accounting.keys())[1]}): {people._income}')
    print(f'Проверка методов класса {people.position}:')
    print(f'Полное имя сотрудника: {people.get_full_name()}')
    print(f'Доход сотрудника с учетом премии: {people.get_total_income()}')
