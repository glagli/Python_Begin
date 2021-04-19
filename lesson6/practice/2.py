# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width
# (ширина). Значения данных атрибутов должны передаваться при создании экземпляра
# класса. Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна. Использовать формулу:
# длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в
# 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т

from random import randint


class Road:
    weight = 25
    density = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphaltCalc(self):
        result = (self._length * self._width * Road.weight * Road.density) / 1000
        print(f"{int(result)} т")


b = Road(20, 5000)
b.asphaltCalc()

r = Road(randint(1, 10000), randint(1, 5000))
r.asphaltCalc()
