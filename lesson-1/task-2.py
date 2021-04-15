"""
2. Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""
# Запрос времени в секундах
current_time = int(input('Введите произвольное время в секундах: '))

# Расчет количества часов
hours_count = current_time // 3600

# Расчет количества часов
minutes_count = (current_time - hours_count * 3600) // 60

# Расчет остатка в секундах
seconds_count = current_time - hours_count * 3600 - minutes_count * 60

# Вывод на экран времени в новом формате
print(f'Время в новом формате "чч:мм:сс": {hours_count}:{minutes_count}:{seconds_count}')
