# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года
# относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

userMonth = int(input("Введите номер месяца: "))

monthZim = [12, 1, 2]
monthVes = [3, 4, 5]
monthLet = [6, 7, 8]
monthOs = [9, 10, 11]

slMonth = dict(зима=monthZim, весна=monthVes, лето=monthLet, осень=monthOs)
if userMonth in slMonth['зима']:
    print('Сейчас зима')
elif userMonth in slMonth['весна']:
    print('Сейчас весна')
elif userMonth in slMonth['лето']:
    print('Сейчас лето')
elif userMonth in slMonth['осень']:
    print('Сейчас осень')


