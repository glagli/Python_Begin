# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Complex:
    def __init__(self, complex1, complex2):
        self.c1 = complex1
        self.c2 = complex2

    def __add__(self, other):
        s1 = sum(self.c1) + sum(other.c1)
        s2 = sum(self.c2) + sum(other.c2)
        if s2 < 0:
            return f"Результат сложения множеств: {s1}{s2}j"
        else:
            return f"Результат сложения множеств: {s1}+{s2}j"

    def __mul__(self, other):
        a = self.c1[0]
        c = other.c1[0]
        b = self.c2[0]
        d = other.c2[0]
        if (a * d + b * c) < 0:
            return f"Результат умножения множеств: {a * c - b * d}{a * d + b * c}j"
        else:
            return f"Результат умножения множеств: {a * c - b * d}+{a * d + b * c}j"

    @classmethod
    def modify(cls, data):
        list_, list_i = [], []
        dataCop = data

        '''Собираю действительные числа'''
        if dataCop[0] == '-':
            dataCop = dataCop.lstrip("-")
            if '-' in dataCop:
                c = dataCop[:dataCop.find("-")]
                c = "-" + c
            elif '+' in dataCop:
                c = dataCop[:dataCop.find("+")]
            else:
                c = '0'
        else:
            if '-' in dataCop:
                c = dataCop[:dataCop.find("-")]
            elif '+' in dataCop:
                c = dataCop[:dataCop.find("+")]
            else:
                c = '0'
        list_.append(int(c))

        '''Отделяю мнимое число от действительного'''
        if '-' in dataCop:
            d = dataCop[dataCop.find("-"):].rstrip('j')
        elif '+' in dataCop:
            d = dataCop[dataCop.find("+"):].rstrip('j')
        else:
            d = data[:data.find("j")]
        if d == '-' or d == '+':
            d += '1'
        list_i.append(int(d))
        return cls(list_, list_i)


c1 = Complex.modify('5+12j')
c2 = Complex.modify('7-4j')

print(c1 + c2)
print(c1 * c2)
