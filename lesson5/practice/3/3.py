# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
# величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
# 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода
# сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32
with open("my_file.txt", 'r', encoding='utf-8') as f:
    content = f.readlines()
    # print(content)
sum = 0
for line in content:
    cash = float(line[line.find(' '):].strip())
    sum += cash
    if cash < 20000:
        print(line[:line.find(' ')].strip(), f'- получает {cash} $')
print('Cредняя величина дохода сотрудников = {} $'.format(round(sum / len(content), 2)))
