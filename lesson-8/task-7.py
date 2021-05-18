"""
7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class ComplexNum:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __add__(self, other):
        re = self.re + other.re
        im = self.im + other.im
        return ComplexNum(re, im)

    def __mul__(self, other):
        re = self.re * other.re - self.im * other.im
        im = self.re * other.im + other.re * self.im
        return ComplexNum(re, im)

    def __str__(self):
        res = f'({self.re}) + ({self.im}i)'
        return res


n1 = ComplexNum(1, 3)
n2 = ComplexNum(3, -2)
print(f'Первое число: {n1}')
print(f'Второе число: {n2}')
ns = n1 + n2
print(f'Их сумма: {ns}')
nm = n1 * n2
print(f'Их произведение: {nm}')
