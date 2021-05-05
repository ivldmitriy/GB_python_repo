"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""
import random


class Car:

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print(f'Машина {self.name} поехала.')
        return 1

    def stop(self):
        print(f'Машина {self.name} остановилась.')
        return 0

    def turn(self, direction):
        if direction:
            print(f'Машина {self.name} повернула направо.')
        elif not direction:
            print(f'Машина {self.name} повернула налево.')
        return direction

    def show_speed(self):
        print(f'Машина {self.name} едет со скоростью {float(self.speed):.1f} км/ч.')
        return self.speed


class TownCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = False

    def show_speed(self):
        print(f'Машина {self.name} едет со скоростью {float(self.speed):.1f} км/ч.')
        if self.speed > 60:
            print(f'Машина {self.name} превысила скорость!')
        return self.speed


class SportCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = False


class WorkCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = False

    def show_speed(self):
        print(f'Машина {self.name} едет со скоростью {float(self.speed):.1f} км/ч.')
        if self.speed > 40:
            print(f'Машина {self.name} превысила скорость!')
        return self.speed


class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


car1 = TownCar(60, 'red', 'Peters car')
car2 = TownCar(80, 'blue', 'Maggies car')
car3 = WorkCar(50, 'light blue', 'Post car')
car4 = SportCar(90, 'red', 'Formula 1')
car5 = PoliceCar(30, 'grey', 'Squad #1')

autopark = [car1, car2, car3, car4, car5]

for car in autopark:
    print(f'***** Атрибуты для {car.name}:')
    print(f'Имя: {car.name}')
    print(f'Цвет: {car.color}')
    print(f'Скорость: {car.speed}')
    print(f'{car.name} это полиция: {car.is_police}')
    print(f'***** Методы для {car.name}:')
    car.go()
    car.turn(random.randint(0, 1))
    car.turn(random.randint(0, 1))
    car.show_speed()
    car.speed = 200 * random.random()
    car.show_speed()
    car.stop()
