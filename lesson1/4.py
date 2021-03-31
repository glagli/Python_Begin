# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
number = int(input("Ведите число: "))
listik = []
while number != 0:
    a = number % 10
    listik.append(a)
    number = number // 10
print('Cамая большая цифра в числе ', max(listik))