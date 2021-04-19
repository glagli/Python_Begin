# Реализовать базовый класс Worker (работник).
#
# ●	определить атрибуты: name, surname, position (должность), income (доход);
# ●	последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus};
# ●	создать класс Position (должность) на базе класса Worker;
# ●	в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учётом премии (get_total_income);
# ●	проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    def __init__(self, name, surname, position, wage, bonus=0.2):
        self._income = {"wage": wage, "bonus": bonus * wage}
        self.fullNameEmployee = [name, surname, position]


class Position(Worker):
    def get_full_name(self):
        return f"{self.fullNameEmployee[0]} {self.fullNameEmployee[1]}"

    def get_total_income(self):
        return f"Доход с учётом премии {self._income['wage'] + self._income['bonus']}\n"


person1 = Position("Vlad", "Glagolev", "engineer", 50550)
print(person1.get_full_name())
print(person1._income)
print(person1.get_total_income())

person2 = Position("Oleg", "Zemskov", "director", 102000.22, 1)
print(person2.get_full_name())
print(person2._income)
print(person2.get_total_income())

person3 = Position("Maria", "Barinova", "analyst", 75050.55, 0.7)
print(person3.get_full_name())
print(person3._income)
print(person3.get_total_income())