"""
3. Реализовать программу работы с органическими клетками.
Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам
 и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
 В методе деления должно осуществляться округление значения до целого числа.
"""


class Cell:
    def __init__(self, cell):
        self.cell = cell
        if self.cell <= 0:
            raise ValueError('Cell size must be bigger then 0')
        if not isinstance(self.cell, int):
            raise TypeError('The int is required for cell size')

    def __add__(self, other):
        if not isinstance(other, Cell):
            raise TypeError('Only cells required for operation')
        res = self.cell + other.cell
        return Cell(res)

    def __sub__(self, other):
        if not isinstance(other, Cell):
            raise TypeError('Only cells required for operation')
        res = self.cell - other.cell
        if res < 0:
            raise ValueError('The cell #1 must be bigger then cell #2')
        return Cell(res)

    def __mul__(self, other):
        if not isinstance(other, Cell):
            raise TypeError('Only cells required for operation')
        res = self.cell * other.cell
        return Cell(res)

    def __truediv__(self, other):
        if not isinstance(other, Cell):
            raise TypeError('Only cells required for operation')
        res = round(self.cell / other.cell)
        if res == 0:
            raise ValueError('Cell division resulted in zero-sized cell')
        return Cell(res)

    def make_order(self, row):
        cell_proc = [(i, '*') for i in range(self.cell)]
        res = ''
        for num, part in cell_proc:
            if num % row == 0 and num != 0:
                res = res + '\n'
            res = res + part
        return res


c1 = Cell(15)
c2 = Cell(4)
c3 = Cell(3)
c_spoiled = 21
print(f'Размер клетки c1: {c1.cell}')
print(f'Размер клетки c2: {c2.cell}')
print(f'Размер клетки c3: {c3.cell}')
print('Клетка c_spoiled - испорченная')

try:
    c_add = c1 + c2
    c_sub = c1 - c3
    c_mul = c2 * c3
    c_div = c1 / c2

    print(f'Результат сложения c1 и c2: {c_add.cell}')
    print(f'Результат вычитания c1 и c3: {c_sub.cell}')
    print(f'Результат умножения c2 и c3: {c_mul.cell}')
    print(f'Результат деления c1 и c2: {c_div.cell}')

    print(f'Раскладка c_add по рядам размера 5:\n{c_add.make_order(5)}')
    print(f'Раскладка c_sub по рядам размера 5:\n{c_sub.make_order(5)}')
    print(f'Раскладка c_mul по рядам размера 5:\n{c_mul.make_order(5)}')
    print(f'Раскладка c_div по рядам размера 5:\n{c_div.make_order(5)}')

    # spoiled block
    # Cell with zero size
    # c_spoiled2 = Cell(0)

    # cell division resulted in zero-sized cell
    # c_div2 = c2 / c1
    # print(c_div2.cell)

    # c_spoiled is not a cell at all
    # c_add2 = c1 + c_spoiled
    # print(c_add2.cell)

    # subtracting the bigger one from smaller one
    # c_sub2 = c2 - c1
    # print(c_sub2.cell)

    # cell made order by zero row
    # print(c2.make_order(0))

except (TypeError, ValueError, ZeroDivisionError) as err:
    print(f'ERROR! \n{err}')
