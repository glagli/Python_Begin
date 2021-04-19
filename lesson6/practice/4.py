# 4.	Реализуйте базовый класс Car.
# ●	у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда)
# ●	опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# ●	добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# ●	для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.
from random import choice, randint


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.colorName = [color, name]
        self.Police = is_police
        self.go()

    def go(self):
        print(f"{self.colorName[1]} {self.colorName[0]} цвета поехала")

    def stop(self):
        print(f"{self.colorName[1]} {self.colorName[0]} цвета остановилась")

    def turn(self, direction):
        print(f"{self.colorName[1]} {self.colorName[0]} цвета повернула {direction}")

    def show_speed(self):
        print(f"Текущая скорость автомобиля {self.speed} км/ч.")


class TownCar(Car):
    def show_speed(self):
        print(f"Текущая скорость автомобиля {self.speed}" if self.speed < 60
              else f"Текущая скорость автомобиля {self.speed} км/ч. Вы превысили скорость")


class SportCar(Car):
    def fastAcceleration(self):
        print("Разгон за 4 сек")


class WorkCar(Car):
    def show_speed(self):
        print(f"Текущая скорость автомобиля {self.speed}" if self.speed < 40
              else f"Текущая скорость автомобиля {self.speed} км/ч. Вы превысили скорость")


class PoliceCar(Car):
    def lightMode(self):
        print("Мигалка включена") if self.Police == True else print("Мигалка выключена")


color = ['белого', 'черного', 'красного', 'серебрянного', 'зелёного', 'небесного']

KIA = TownCar(randint(40, 150), choice(color), "KIA")
KIA.turn(choice(['направо', 'налево']))
KIA.show_speed()
KIA.stop()
print()

LADA = WorkCar(randint(35, 100), choice(color), "LADA")
LADA.turn(choice(['направо', 'налево']))
LADA.show_speed()
LADA.stop()
print()

sport = SportCar(randint(50, 250), choice(color), "Audi R8")
sport.turn(choice(['направо', 'налево']))
sport.fastAcceleration()
sport.show_speed()
sport.stop()
print()

Police = PoliceCar(randint(40, 170), choice(color), "BMW", True)
Police.turn(choice(['направо', 'налево']))
Police.lightMode()
Police.show_speed()
Police.turn(choice(['направо', 'налево']))
Police.speed = 50
Police.show_speed()
Police.Police = False
Police.lightMode()
Police.stop()
