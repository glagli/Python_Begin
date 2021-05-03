# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно
# данные. При этом английские числительные должны заменяться на русские. Новый блок строк
# должен записываться в новый текстовый файл.
mySlov = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open("my_file.txt", 'r', encoding='utf-8') as f:
    content = f.readlines()
with open("my_file_rus.txt", 'w', encoding='utf-8') as f2:
    for lines in content:
        number = lines[0:lines.find(' ')]
        f2.write(f"{mySlov[number]} {lines.strip()[lines.find(' ') + 1:]}\n")
