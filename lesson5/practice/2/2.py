# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
# подсчет количества строк, количества слов в каждой строке.

with open("my_file.txt", 'r', encoding='utf-8') as f:
    content = f.readlines()
    print('Количества строк - ', len(content))

quantity = [len(i.replace('—', '').split()) for i in content]

for i in range(len(quantity)):
    print('{}-й строка - {} сл.'.format(i + 1, quantity[i]))
