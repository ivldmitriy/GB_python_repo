"""
5. Создать (программно) текстовый файл,
записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

print('Программа служит для записи в файл набора чисел.')
print('Об окончании ввода данных свидетельствует пустая строка.')
print('На экране появится сумма введенных вами чисел.')

try:
    with open("file_from_t5", "w+") as file:
        while True:
            inp = input('Введите число для записи в файл: ')
            if not inp:
                break
            num = float(inp)
            file.writelines(f'{num} ')
        file.seek(0)
        otp = file.read()
    res = sum(map(float, otp.strip().split()))
    print(f'Сумма чисел, записанных в файле: {res}')
except (IOError, ValueError) as err:
    print(err)
