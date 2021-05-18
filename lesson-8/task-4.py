"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь

6. Продолжить работу над вторым заданием.
Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров,
отправленных на склад, нельзя использовать строковый тип данных.
"""


class Company:

    def __init__(self, name, *divisions):
        self.name = name
        self.divisions = list(divisions)
        self.equipment = {}
        for elem in divisions:
            self.equipment[elem] = {}

    def balance_in(self, division, device, count):
        if device.index in self.equipment[division]:
            self.equipment[division][device.index][1] += count
        else:
            self.equipment[division][device.index] = [device, count]

    @property
    def structure(self):
        return self.divisions

    @property
    def inventory(self):
        return self.equipment

    @property
    def show(self):
        for key1 in self.inventory.keys():
            for key2 in self.inventory[key1]:
                yield f'{key1} {key2}: {self.inventory[key1][key2][0].about}, {self.inventory[key1][key2][1]} шт'


class Warehouse:
    def __init__(self, **equipment):
        self.equipment = dict(equipment)

    @property
    def inventory(self):
        return self.equipment

    @property
    def show(self):
        for key in self.inventory.keys():
            yield f'{key}: {self.inventory[key][0].about}, {self.inventory[key][1]} шт'

    def transfer(self, device, count):
        if self.equipment[device.index][1] - count < 0:
            print(f'Такого количества товара №{device.index} "{device.model}" нет на складе!')
            return device, 0
        else:
            self.equipment[device.index][1] -= count
        if self.equipment[device.index][1] == 0:
            print(f'Товар №{device.index} "{device.model}" закончился!')
        return device, count

    def receive(self, device, count):
        if count >= 0:
            if device.index in self.equipment:
                self.equipment[device.index][1] += count
            else:
                self.equipment[device.index] = [device, count]
        else:
            print(f' Некорректное количество товара №{device.index} "{device.model}" для передачи!')


class OfficeEquipment:
    equip_count = 0

    def __init__(self, code, model, producer):
        OfficeEquipment.equip_count += 1
        self.index = OfficeEquipment.equip_count
        self.code = code
        self.model = model
        self.firm = producer

    @property
    def about(self):
        return dict([(attribute, value) for attribute, value in self.__dict__.items()])


class Printer(OfficeEquipment):
    def __init__(self, code, model, producer, is_color=False):
        super().__init__(code, model, producer)
        self.is_color = is_color


class Scanner(OfficeEquipment):
    def __init__(self, code, model, producer, core_tech, paper_format='A4'):
        super().__init__(code, model, producer)
        self.paper_format = paper_format
        self.tech = core_tech


class Xerox(OfficeEquipment):
    def __init__(self, code, model, producer, is_color=False, is_standalone=False):
        super().__init__(code, model, producer)
        self.is_color = is_color
        self.is_standalone = is_standalone


# Объявляем компанию
gb = Company('Geek Brains', 'methodical', 'video', 'financial', 'management')
print(f'Добро пожаловать в программу учета оргтехники компании {gb.name}!')
print(f'В компании есть такие отделы: {gb.structure}')
print(f'Сейчас они оснащены так: {gb.inventory}')

# Создаем склад
storage = Warehouse()
print(f'Мы открыли склад оргтехники. Сейчас там пусто. Вот так: {storage.inventory}')

# Закупаем технику
hp1 = Printer(5043680004, 'VH504LJP', 'HP')
hp2 = Printer(5043680005, 'VH908LJPc', 'HP', True)
x1 = Xerox(5043680006, 'x745bw', 'Xerox', False, True)
hp3 = Scanner(5043680007, 'zm643m', 'HP', 'CIS')
c1 = Scanner(5043680008, 'c3458daq', 'Canon', 'CCD', 'A3')
model_range = [hp1, hp2]

# Добавляем технику на склад
storage.receive(hp1, 0)
storage.receive(hp1, 0)
storage.receive(hp2, 0)
storage.receive(x1, 0)
storage.receive(hp3, 0)
storage.receive(c1, 0)
print(f'Мы можем закупить следующую оргтехнику для оснащения отделов: ')
for item in storage.inventory.values():
    print(f'{item[0].about}')

print('Давайте закупать!')
print('Чтобы завершить закупку и перейти к оснащению отделов, введите stop')
while True:
    var = input('Введите индекс оргтехники для закупки и количество единиц через пробел: ')
    if var == 'stop':
        break
    try:
        var = var.split()
        if len(var) != 2:
            raise ValueError
        inp = []
        for el in var:
            if el.isnumeric():
                el = int(el)
                inp.append(el)
            else:
                raise ValueError
        storage.receive(storage.inventory[inp[0]][0], inp[1])
        print('Состояние склада:')
        for item in storage.show:
            print(item)
    except ValueError:
        print('Ввод некорректный!')

print('Давайте оснащать компанию!')
print('Чтобы завершить процесс, введите stop')
while True:
    var = input('Введите название отдела, индекс оргтехники для передачи, количество единиц через пробел: ')
    if var == 'stop':
        break
    try:
        var = var.split()
        if len(var) != 3:
            raise ValueError
        inp = []
        div = var[0]
        if div not in gb.structure:
            raise ValueError
        del var[0]
        for el in var:
            if el.isnumeric():
                el = int(el)
                inp.append(el)
            else:
                raise ValueError
        gb.balance_in(div, *storage.transfer(storage.inventory[inp[0]][0], inp[1]))
        print('Состояние склада:')
        for item in storage.show:
            print(item)
    except ValueError:
        print('Ввод некорректный!')

print('Компания оснащена так: ')
for item in gb.show:
    print(item)
