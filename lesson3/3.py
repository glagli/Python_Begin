# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и
# возвращает сумму наибольших двух аргументов
def my_func(a, b, c):
    myList = [a, b, c]
    """Ну вот теперь то уже можно использовать sort и reverse ))"""
    myList.sort(reverse=True)
    return round((myList[0] + myList[1]), 2)


one = float(input('Введите число №1: '))
two = float(input('Введите число №2: '))
three = float(input('Введите число №3: '))

print(my_func(one, two, three))
