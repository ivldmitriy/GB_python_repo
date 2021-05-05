"""
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки.')


class Pen(Stationery):

    def draw(self):
        print(f'Запуск отрисовки ручкой {self.title}.')


class Pencil(Stationery):

    def draw(self):
        print(f'Запуск отрисовки карандашом {self.title}.')


class Handle(Stationery):

    def draw(self):
        print(f'Запуск отрисовки маркером {self.title}.')


st = Stationery('My_stationeries')
st1 = Pen('Parker')
st2 = Pencil('Koh-i-Noor')
st3 = Handle('Berlingo')

st.draw()
st1.draw()
st2.draw()
st3.draw()
