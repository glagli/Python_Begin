# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
# __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.

# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
# объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
# строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join('\t'.join([str(line) for line in lines]) for lines in self.matrix)

    # def __add__(self, other):
    #     result = []
    #     for i in range(len(self.matrix)):
    #         result.append([])
    #         for j in range(len(self.matrix[0])):
    #             result[i].append(self.matrix[i][j] + other.matrix[i][j])
    #     return Matrix(result)

    def __add__(self, other):
        result = [[int(self.matrix[line][itm]) + int(other.matrix[line][itm]) for itm in range(len(self.matrix[line]))]
                  for
                  line in range(len(self.matrix))]
        return Matrix(result)


matrix1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix2 = Matrix([[7, 8], [9, 10], [11, 12]])

print(f"Матрица 1:\n{matrix1}\n")
print(f"Матрица 2:\n{matrix2}\n")
print(f"Сумма матриц:\n{matrix1 + matrix2}")
