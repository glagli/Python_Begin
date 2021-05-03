# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный
# предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их
# количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по
# нему. Вывести словарь на экран.
# Информатика: 100(л) 50(пр) 20(лаб)
# Физика: 30(л) 10(лаб)
# Физкультура: 30(пр)
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
lesson = []
lectures = []
practice = []
lab = []

with open("my_file.txt", 'r', encoding='utf-8') as f:
    numbers = f.readlines()
    for number in numbers:
        lesson.append(number[:number.find(':')])
        lectures.append(number[number.find('(л)') - 3:number.find('(л)')].strip(
            ')').strip()) if '(л)' in number else lectures.append('0')
        practice.append(number[number.find('(пр)') - 3:number.find('(пр)')].strip(
            ')').strip()) if '(пр)' in number else practice.append('0')
        lab.append(number[number.find('(лаб)') - 2:number.find('(лаб)')].strip(
            ')').strip()) if '(лаб)' in number else lab.append('0')

# print(lesson)
# print(lectures)
# print(practice)
# print(lab)

result = {lesson[i]: (int(lectures[i]) + int(practice[i]) + int(lab[i])) for i in range(len(lesson))}
print('Cловарь:', result)
print(type(result))
