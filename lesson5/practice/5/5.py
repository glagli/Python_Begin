# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить
# ее на экран.
from random import randint

mySum = 0
with open("my_file.txt", 'w+', encoding='utf-8') as f:
    for i in range(10):
        f.write(str(randint(0, 100)) + ' ')
    f.seek(0)
    numbers = f.read().split()
    for i in numbers:
        mySum += int(i)
    print('Сумма чисел в файле ', mySum)
