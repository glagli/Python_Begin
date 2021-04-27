# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой

class OwnError(Exception):
    def __init__(self, text):
        self.text = text


try:
    myNumber = float(input("Введите чилсо: "))
    myNumber2 = float(input("Введите на сколько поделим это число: "))
    if myNumber2 == 0:
        raise OwnError("На ноль делить нельзя")
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
else:
    print(f'Результат {round(myNumber / myNumber2, 2)}')
