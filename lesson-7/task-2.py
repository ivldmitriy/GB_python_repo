"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда,
которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod

log = []
accounting = 0


class Clothes:

    cloth_count = 0

    def __init__(self, title=None):
        self.title = title
        Clothes.cloth_count += 1
        self.index = Clothes.cloth_count
        if not self.title:
            self.title = 'Untitled'

    @property
    def calculate(self):
        res = None
        return res


class Coat(Clothes):
    def __init__(self, size, title=None):
        super().__init__(title)
        self.size = size

    @property
    def calculate(self):
        res = self.size / 6.5 + 0.5
        log.append((self.index, self.title, 'Coat', res))
        return res


class Costume(Clothes):
    def __init__(self, height, title=None):
        super().__init__(title)
        self.height = height

    @property
    def calculate(self):
        res = 2 * self.height + 0.3
        log.append((self.index, self.title, 'Costume', res))
        return res


cloth0 = Costume(1.8, 'Arnies').calculate
cloth1 = Coat(74.4, 'Bens').calculate
cloth2 = Coat(54.3).calculate
cloth3 = Costume(1.75).calculate

for item in log:
    print(f'{item[0]}. {item[1]} {item[2]} needs {item[3]:.2f} metres of matter to be produced')
    accounting += item[3]

print(f'The overall needs of matter is {accounting} metres')


class Base(ABC):
    def __init__(self, p=None):
        self.p = p

    @abstractmethod
    def method(self):
        pass


class SubClass1(Base):
    def __init__(self, p1, p=None):
        super().__init__(p)
        self.p1 = p1

    @property
    def method(self):
        print('method1')
        return self.p1


class SubClass2(Base):
    def __init__(self, p2, p=None):
        super().__init__(p)
        self.p2 = p2

    @property
    def method(self):
        print('method2')
        return self.p2


print('\nABC interface test')
mc1 = SubClass1('SC1')
mc2 = SubClass2('SC2')
var1 = mc1.method
var2 = mc2.method
print(var1)
print(var2)
