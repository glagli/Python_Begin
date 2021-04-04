# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и
# выведите в формате чч:мм:сс. Используйте форматирование строк.

time = int(input('Введите время в секундах: '))
hour = time // 3600
minut = (time - (hour * 3600)) // 60
second = (time - (hour * 3600)) - (minut * 60)

# if hour < 10:
#     hour = '0' + str(hour)
# if minut < 10:
#     minut = '0' + str(minut)
# if second < 10:
#     second = '0' + str(second)

print(f'{hour:02}:{minut:02}:{second:02}') # Хороший способ использование f формата

# print('0'+str(hour) if hour < 10 else hour, end=':')
# print('0'+str(minut) if minut < 10 else minut, end=':')
# print('0'+str(second) if second < 10 else second)

