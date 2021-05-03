# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и
# возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Сделать
# вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо
# использовать написанную ранее функцию int_func().
Latin = ''
for i in list(range(97, 123)):
    Latin += chr(i)


# print(Latin)


def int_func(lines):
    result = []
    lines = lines.split()
    # print(lines)
    for line in lines:
        """ 
        Если строка входит в переменную Latin то изменяем на заглавную букву
        использовал difference как разницу между множествами
        
        """
        result.append(line.title()) if not set(line).difference(Latin) else ''
    return result


# myLine = 'nice авп ъghj jапро hjjпаро вапрghgh cool cool'
myLine = input("Введите строку из слов, разделенных пробелом в нижнем регистре : ")
print(*int_func(myLine))
