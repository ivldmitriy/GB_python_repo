"""
1. Создать класс TrafficLight (светофор) и
определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться
только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""
import time
import random

colors = [None, 'red', 'yellow', 'green']
timing = [None, 7, 2, 7]
# From 0 (no mistakes) to 1 (100% traffic light crush)
little_gremlin_power = 0.05
# looks like there is not regime checking, but possibility of system crushing :(
# please, forgive me this trick


class TrafficLight:

    def __init__(self):
        self.__name = 'Traffic_Light'
        self.__color = 0

    def running(self, number):

        def little_gnome(color):
            print(colors[color])
            return timing[color]

        def little_gremlin(color):
            if random.random() < little_gremlin_power:
                return -1
            else:
                return color

        for i in range(number * (len(colors) - 1)):
            if self.__color == 0:
                self.__color = 1
                time.sleep(little_gnome(self.__color))
                self.__color = little_gremlin(self.__color)
            elif self.__color == 1:
                self.__color = 2
                time.sleep(little_gnome(self.__color))
                self.__color = little_gremlin(self.__color)
            elif self.__color == 2:
                self.__color = 3
                time.sleep(little_gnome(self.__color))
                self.__color = little_gremlin(self.__color)
            elif self.__color == 3:
                self.__color = 1
                time.sleep(little_gnome(self.__color))
                self.__color = little_gremlin(self.__color)
            else:
                print(f'{self.__name} has broken! Try again.')
                exit()


print('Hello! Lets make the traffic light!')
try:
    cycles = int(input('Please, type the count of light work cycles: '))
    light = TrafficLight()
    light.running(cycles)
except ValueError:
    print('There is not number typed!')
