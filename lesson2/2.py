# Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются
# элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний
# сохранить на своем месте. Для заполнения списка элементов необходимо использовать
# функцию input().
number = int(input("Введите кол-во элементов в списке: "))
myList = []
for i in range(1, number + 1):
    element = input(f'Введите {i}-й элемент: ')
    myList.append(element)

print(myList)
if number % 2 == 0:
    for i in range(0, number, 2):
        myList[i + 1], myList[i] = myList[i], myList[i + 1]
else:
    for i in range(0, number - 1, 2):
        myList[i + 1], myList[i] = myList[i], myList[i + 1]
print(myList)
