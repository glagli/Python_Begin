# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @staticmethod
    def valid(obj):
        if obj.month > 12 or obj.month < 1:
            return "Введён некорректный месяц"
        elif obj.day < 1 or obj.day > 31:
            return "Введён некорректный день"
        elif obj.year < 1 or obj.year > 9999:
            return "Введён некорректный год"
        else:
            return f"Сейчас {obj.day} {obj.month} {obj.year} года"

    @classmethod
    def modify(cls, data):
        d, m, y = data.split('-')
        return cls(int(d), int(m), int(y))


one = Data.modify("23-11-2021")
print(Data.valid(one))
