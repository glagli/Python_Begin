# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
# сущность (класс) этого проекта — одежда, которая может иметь определенное название. К
# типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
# параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
# H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
# (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
# знания: реализовать абстрактные классы для основных классов проекта, проверить на
# практике работу декоратора @property.
from abc import ABC, abstractmethod


class clothes(ABC):
    result = 0

    def __init__(self, parameter):
        self.parameter = parameter

    @property
    @abstractmethod
    def expense(self):
        pass

    def __add__(self, other):
        clothes.result += self.expense + other.expense
        return suit(0)

    def __str__(self):
        res = clothes.result
        clothes.result = 0
        return f'{res}'


class coat(clothes):
    @property
    def expense(self):
        return round(self.parameter / 6.5) + 0.5


class suit(clothes):
    @property
    def expense(self):
        return round((self.parameter * 2 + 0.3)/100)


a = suit(186)
b = coat(45)
print(a + b + b + a)
