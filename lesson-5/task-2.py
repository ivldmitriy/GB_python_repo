"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке."""

wrd_counter = []
try:
    with open("file_for_t2", "r") as file:
        str_num = sum(1 for line in file)
        file.seek(0)
        for line in file:
            wrd_counter.append(len(line.split()))
    print(f'Число строк в файле: {str_num}')
    for i, item in enumerate(wrd_counter):
        print(f'Число слов в {i+1}й строке: {item}')
except FileNotFoundError:
    print("Файл не найден!")
