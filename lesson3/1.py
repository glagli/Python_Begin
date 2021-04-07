# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def div(delm, delit):
    try:
        result = delm / delit
        print(round(result, 2))
    except ZeroDivisionError:
        print("Делить на ноль нельзя")


delimoe = input("Введите число: ")
delitel = input("Введите на что будем делить число: ")
div(float(delimoe), float(delitel)) if delimoe.isdigit() is True and delitel.isdigit() is True else print("Программа работает только с числами")
