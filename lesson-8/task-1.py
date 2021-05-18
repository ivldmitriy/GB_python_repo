"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
формата «день-месяц-год». В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
(например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""

# число дней в каждом месяце
calendar = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


class Date:
    def __init__(self, date_string):
        self.date_string = date_string

    @classmethod
    def extract(cls, date_string):
        date_list = []
        for el in date_string.split('-'):
            date_list.append(int(el))
        return date_list

    @staticmethod
    def validate(date_list):
        day = date_list[0]
        month = date_list[1]
        year = date_list[2]

        # внутренняя функция для проверки, висоскный ли введеный год
        def check_year(y):
            is_leap = False
            if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
                is_leap = True
            return is_leap

        validator = True
        valid_msg = ''

        # блок проверки реалистичности введенных данных
        if year < 0:
            validator = False
            valid_msg = valid_msg + 'Год введен не корректно. '
        if month < 1 or month > 12:
            validator = False
            valid_msg = valid_msg + 'Месяц введен не корректно. '
        if day < 1 or day > calendar[month]:
            validator = False
            valid_msg = valid_msg + 'День введен не корректно. '
        elif not check_year(year) and month == 2 and day > calendar[month] - 1:
            validator = False
            valid_msg = valid_msg + 'День введен не корректно. '
        else:
            valid_msg = 'Дата введена корректно. '

        print(valid_msg)
        return validator


date1 = Date('08-03-2021')
date2 = Date('23-02-2021')
date3 = Date('29-02-2021')
date4 = Date('29-02-2020')
date5 = Date('00-13-0000')

Date.validate(Date.extract(date1.date_string))
Date.validate(Date.extract(date2.date_string))
Date.validate(Date.extract(date3.date_string))
Date.validate(Date.extract(date4.date_string))
Date.validate(Date.extract(date5.date_string))
