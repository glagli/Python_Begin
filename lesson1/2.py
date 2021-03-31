# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и
# выведите в формате чч:мм:сс. Используйте форматирование строк.
time = int(input('Введите время в секундах: '))
hour = int(time//3600)
minut = int((time - (hour*3600))//60)
second = int(time-(hour*3600)-(minut*60))

print('0'+str(hour) if hour < 10 else hour, end=':')
print('0'+str(minut) if minut < 10 else minut, end=':')
print('0'+str(second) if second < 10 else second)