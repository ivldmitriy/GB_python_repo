"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def user_id(**kwargs):
    user_card = []
    for k in kwargs:
        user_stat = f'{k}: {kwargs.get(k)}'
        user_card.append(user_stat)
        res = ', '.join(user_card)
    return res


about = user_id(id_name='Иван', id_year='1990', id_city='Тверь', id_mail='example.mail.ru', id_phone='84822123456')

print(about)
