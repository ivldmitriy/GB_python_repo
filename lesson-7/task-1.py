from itertools import zip_longest


class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        res = []
        for raw_el in self.data:
            raw = ' '.join(map(str, raw_el))
            res.append(raw)
        return '\n'.join(res)

    def __add__(self, other):
        res = []
        try:
            for (raw_el1, raw_el2) in zip_longest(self.data, other.data, fillvalue=[]):
                res_el = []
                for (el1, el2) in zip_longest(raw_el1, raw_el2, fillvalue=None):
                    res_el.append(el1+el2)
                res.append(res_el)
            return Matrix(res)
        except TypeError:
            print('Matrix objects must be the same size for "add" operation!')
            return 'Error'


m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = Matrix([[7, 8, 9, 0], [4, 5, 6, 0], [1, 2, 3, 0]])
m3 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [0, 0, 0]])
m4 = Matrix([[7, 8, 9], [4, 5, 6], [1, 2, 3]])

print('Первая матрица:')
print(m1)
print('\nВторая матрица:')
print(m2)
print('\nРезультат сложения:')
m = m1 + m2
print(m)

print('\nПервая матрица:')
print(m1)
print('\nВторая матрица:')
print(m3)
print('\nРезультат сложения:')
m = m1 + m3
print(m)

print('\nПервая матрица:')
print(m1)
print('\nВторая матрица:')
print(m4)
print('\nРезультат сложения:')
m = m1 + m4
print(m)
