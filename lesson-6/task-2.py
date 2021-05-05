"""
2. Реализовать класс Road (дорога),
в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * число см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""

# thickness of the road in sm
thick = 5.0

# mass of asphalt needed for 1 square metre of the road coverage with 1 sm thickness
mass = 25.0


class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def check(self):
        res = self._width * self._length * mass * thick / 1000
        return res


print('Hello! Lets calculate the mass of asphalt needed for your road coverage')
print(f'The thickness of coverage is {thick} sm')
print(f'For the one square metre of road with 1 sm thickness the {mass} kg of asphalt needed')
try:
    wdth = float(input('Please, type the width of your road in metres: '))
    lngth = float(input('Please, type the length of your road in metres: '))
    road = Road(lngth, wdth)
    asphalt_mass = road.check()
    print(f'You need the {asphalt_mass} tons of asphalt for your road')
except ValueError:
    print('There is not number typed!')
